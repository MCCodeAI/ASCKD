import sys
import os

# Add the backend directory to sys.path so we can import 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
# Vercel looks for a variable named 'app' in the file specified in vercel.json
