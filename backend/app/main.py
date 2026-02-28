from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="ASCK Chatbot API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api import chat

app.include_router(chat.router, prefix="/api")

# Mount static files for documentation access
# Files in backend/structured_docs will be accessible at /docs/
docs_path = Path(__file__).parent.parent / "structured_docs"
if docs_path.exists():
    app.mount("/docs", StaticFiles(directory=str(docs_path), html=True), name="docs")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
