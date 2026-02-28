#!/bin/bash

# Get the root directory of the project
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BACKEND_DIR="$ROOT_DIR/backend"

# 1. Environment Check (Outside subshell)
if [ ! -d "$BACKEND_DIR/.venv" ]; then
    echo "Error: Virtual environment not found at $BACKEND_DIR/.venv"
    echo "Please run _init.sh first."
    exit 1
fi

# 2. Execution (Inside subshell for total isolation)
(
    # Activate the virtual environment (only affects this subshell)
    if [ -f "$BACKEND_DIR/.venv/bin/activate" ]; then
        source "$BACKEND_DIR/.venv/bin/activate"
    else
        echo "Error: Activation script not found."
        exit 1
    fi

    # Change directory (only affects this subshell)
    cd "$BACKEND_DIR"

    # Execute the scanner script
    echo "Starting structured docs scanner..."
    python utils/structured_docs_scanner.py "$@"
    
    # Subshell ends here: directory and venv are automatically cleared
)
