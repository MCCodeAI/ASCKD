import os
import json
import xxhash
import time
from typing import Dict, List, Tuple, Set, Union, Any
from pathlib import Path
from dotenv import load_dotenv
try:
    from backend.utils.structured_docs_wv import WVStructuredDocsManager
except ImportError:
    # Fallback for when running directly from utils dir (though not recommended with relative imports in dependencies)
    import sys
    # Add project root to sys.path to allow 'from backend.utils...' import
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from backend.utils.structured_docs_wv import WVStructuredDocsManager
from markdown_it import MarkdownIt
from tqdm import tqdm

# Load environment variables from backend/.env file
# This loads VOYAGEAI_APIKEY and other keys needed for Weaviate
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
print(f"Loaded environment from: {env_path}")

def calculate_file_hash(filepath: str) -> str:
    """Calculates the XXH64 hash of a file's content."""
    hasher = xxhash.xxh64()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def calculate_directory_hash(dirpath: str, children_names: List[str]) -> str:
    """Calculates the XXH64 hash of a directory based on its sorted children names."""
    hasher = xxhash.xxh64()
    for name in sorted(children_names):
        hasher.update(name.encode('utf-8'))
    return hasher.hexdigest()

def scan_structured_docs(root_dir: str, previous_state: Dict[str, Any] = None, wv_manager: WVStructuredDocsManager = None) -> Dict[str, Dict[str, Any]]:
    """
    Scans the structured docs directory recursively.
    Returns a dictionary where keys are relative paths and values are dicts with hash and metadata.
    """
    state = {}
    previous_state = previous_state or {}
    
    # Pre-scan to count total files for progress bar
    total_files = 0
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.md'):
                total_files += 1
    
    md_parser = MarkdownIt()
    
    # Walk top-down
    pbar = tqdm(total=total_files, desc="Scanning docs", unit="file")
    
    for root, dirs, files in os.walk(root_dir):
        rel_root = os.path.relpath(root, root_dir)
        if rel_root == ".":
            rel_root = ""
            
        # 1. Hash the directory itself based on immediate children
        all_children = dirs + files
        dir_hash = calculate_directory_hash(root, all_children)
        
        if rel_root:
             # Directories don't really have mtime/size optimization in the same way as files 
             # (mtime on dir changes when children added/removed, but we already hash children names).
             # We'll just store the hash.
             state[rel_root] = {'hash': dir_hash, 'type': 'dir'}
             
             if wv_manager:
                 # Create sddir
                 level = rel_root.count(os.sep) + 1
                 dirname = os.path.basename(root)
                 sddir_name = f"d{level}_{dirname}"
                 dir_uuid = wv_manager.create_sddir(sddir_name, rel_root, level)
                 # Store uuid in state if needed, or just use it for files
                 state[rel_root]['uuid'] = dir_uuid
        
        # 2. Hash MD files
        for f in files:
            if f.endswith('.md'):
                full_path = os.path.join(root, f)
                rel_path = os.path.join(rel_root, f)
                
                # Get metadata
                try:
                    stat = os.stat(full_path)
                    mtime = stat.st_mtime
                    size = stat.st_size
                except OSError:
                    # If file vanished or unreadable, skip
                    continue
                
                file_hash = None
                
                # Check optimization
                if rel_path in previous_state:
                    prev_entry = previous_state[rel_path]
                    # Handle backward compatibility (if prev entry was just a string hash)
                    if isinstance(prev_entry, dict):
                        if prev_entry.get('mtime') == mtime and prev_entry.get('size') == size:
                            file_hash = prev_entry.get('hash')
                
                if file_hash is None:
                    file_hash = calculate_file_hash(full_path)
                
                state[rel_path] = {
                    'hash': file_hash,
                    'mtime': mtime,
                    'size': size,
                    'type': 'file'
                }
                
                if wv_manager:
                    # Determine parent dir UUID
                    parent_dir_uuid = None
                    if rel_root in state:
                        parent_dir_uuid = state[rel_root].get('uuid')
                    
                    # Create sdfile
                    # Use .html extension for the path property in Weaviate
                    html_rel_path = os.path.splitext(rel_path)[0] + ".html"
                    file_uuid = wv_manager.create_sdfile(f, html_rel_path, parent_dir_uuid)
                    state[rel_path]['uuid'] = file_uuid
                    
                    # Check if we need to process content (new or modified)
                    # Simple check: if hash changed or not in previous state
                    process_content = True
                    if rel_path in previous_state:
                         prev_entry = previous_state[rel_path]
                         if isinstance(prev_entry, dict) and prev_entry.get('hash') == file_hash:
                             process_content = False
                    
                    if process_content:
                        print(f"Processing content for {rel_path}...")
                        start_time = time.time()
                        
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f_obj:
                            content = f_obj.read()
                        
                        # Time the file processing - pass html_rel_path as file_path
                        wv_manager.process_file_content(file_uuid, content, html_rel_path)
                        
                        elapsed = time.time() - start_time
                        # print(f"  ✓ Completed in {elapsed:.2f}s") # Reduced verbosity for tqdm
                
                # 3. Generate HTML if not exists
                html_path = os.path.splitext(full_path)[0] + ".html"
                if not os.path.exists(html_path):
                    # If we haven't read content yet, read it now
                    if 'content' not in locals():
                         with open(full_path, 'r', encoding='utf-8', errors='ignore') as f_obj:
                            content = f_obj.read()
                    
                    html_content = md_parser.render(content)
                    with open(html_path, 'w', encoding='utf-8') as f_html:
                        f_html.write(html_content)
                
                # Clear content variable for next iteration if it was set
                if 'content' in locals():
                    del content
                
                pbar.update(1)
    
    pbar.close()
    return state

def save_state(state: Dict[str, Any], filepath: str):
    """Saves the state dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(state, f, indent=2, sort_keys=True)

def load_state(filepath: str) -> Dict[str, Any]:
    """Loads the state dictionary from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def detect_changes(current_state: Dict[str, Any], previous_state: Dict[str, Any]) -> Tuple[List[str], List[str], List[str]]:
    """
    Compares current and previous state.
    Returns (added, modified, deleted) lists of keys.
    """
    added = []
    modified = []
    deleted = []
    
    current_keys = set(current_state.keys())
    previous_keys = set(previous_state.keys())
    
    for key in current_keys - previous_keys:
        added.append(key)
        
    for key in previous_keys - current_keys:
        deleted.append(key)
        
    for key in current_keys & previous_keys:
        curr_val = current_state[key]
        prev_val = previous_state[key]
        
        curr_hash = curr_val['hash'] if isinstance(curr_val, dict) else curr_val
        prev_hash = prev_val['hash'] if isinstance(prev_val, dict) else prev_val
        
        if curr_hash != prev_hash:
            modified.append(key)
            
    return added, modified, deleted

if __name__ == "__main__":
    # Example usage
    import sys
    
    # Start timing
    script_start_time = time.time()
    
    # Default paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STRUCTURED_DOCS_DIR = os.path.join(BASE_DIR, "structured_docs")
    STATE_FILE = os.path.join(STRUCTURED_DOCS_DIR, "structured_docs_state.json")
    
    print(f"Scanning {STRUCTURED_DOCS_DIR}...")
    previous_state = load_state(STATE_FILE)
    
    # Initialize WV Manager
    wv_manager = None
    current_state = None
    
    try:
        voyage_api_key = os.environ.get("VOYAGEAI_APIKEY")
        if not voyage_api_key:
            raise ValueError("VOYAGEAI_APIKEY environment variable not set.")
        
        wv_manager = WVStructuredDocsManager(voyageai_key=voyage_api_key)
        
        # If state file didn't exist (previous_state is empty), reset schema
        if not previous_state:
            print("No state file found. Resetting Weaviate schema...")
            wv_manager.reset_schema()
            
        current_state = scan_structured_docs(STRUCTURED_DOCS_DIR, previous_state, wv_manager)
        
    except Exception as e:
        print(f"Error with WV: {e}")
        print("Proceeding without WV update...")
        current_state = scan_structured_docs(STRUCTURED_DOCS_DIR, previous_state)
        
    finally:
        # Always close connection if it was opened
        if wv_manager is not None:
            try:
                wv_manager.close()
            except Exception as e:
                print(f"Warning: Error closing WV connection: {e}")
    
    added, modified, deleted = detect_changes(current_state, previous_state)
    
    if added or modified or deleted:
        print("Changes detected:")
        if added: print(f"  Added: {added}")
        if modified: print(f"  Modified: {modified}")
        if deleted: print(f"  Deleted: {deleted}")
        
        print(f"Saving new state to {STATE_FILE}...")
        save_state(current_state, STATE_FILE)
    else:
        print("No changes detected.")
    
    # Show total time
    total_time = time.time() - script_start_time
    print(f"\n⏱️  Total execution time: {total_time:.2f}s")
