import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "ASCK Chatbot"
    WEAVIATE_URL: str = os.getenv("WEAVIATE_URL", "http://localhost:8080")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
