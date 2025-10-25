# main_api.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

# === Load environment variables ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

# === FastAPI app ===
app = FastAPI(title="Jarvis AI API")

# === CORS middleware ===
# Allows frontend to communicate with backend without errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # You can replace "*" with your frontend URL for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Request model ===
class Command(BaseModel):
    text: str

# === Root endpoint ===
@app.get("/")
async def root():
    return {"message": "Jarvis AI API is running!"}

# === Test endpoint ===
@app.get("/test")
async def test_jarvis():
    try:
        test_response = process_command("Hello, who are you?")
        return {
            "status": "success",
            "message": "Jarvis is working!",
            "test_response": test_response
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# === Main POST endpoint ===
@app.post("/ask")
async def ask_jarvis(cmd: Command):
    try:
        response = process_command(cmd.text)
        return {"response": response}
    except Exception as e:
        return {"response": f"I encountered an error: {str(e)}"}
