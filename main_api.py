# main_api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

app = FastAPI(title="Jarvis AI API")

# === CORS Configuration ===
origins = [
    "https://personal-ai-front.vercel.app",  # Your frontend URL
    "http://127.0.0.1:5500",                 # VS Code Live Server
    "http://localhost:5500"                  # Local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Only allow these origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Request Model ===
class Command(BaseModel):
    text: str

# === API Endpoints ===
@app.post("/ask")
async def ask_jarvis(cmd: Command):
    """
    Receive a command from the frontend, process it using agent.py,
    and return the response.
    """
    try:
        response = process_command(cmd.text)
    except Exception as e:
        response = f"❌ Jarvis AI: Error processing command: {str(e)}"
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Jarvis AI API is running!"}
