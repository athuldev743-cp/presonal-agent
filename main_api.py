# main_api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

app = FastAPI(title="Jarvis AI API")

# === CORS Configuration ===
origins = [
    "https://personal-ai-front.vercel.app",  # frontend deployed on Vercel
    "http://127.0.0.1:5500",                 # local testing (Live Server)
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # you can use ["*"] for testing only
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
    Receive a command from frontend, process with agent.py, return response.
    """
    try:
        response = process_command(cmd.text)
    except Exception as e:
        response = f"❌ Jarvis AI: Error processing command: {str(e)}"
    return {"response": response}

@app.get("/test")
async def test_jarvis():
    """
    Test if Jarvis is working
    """
    try:
        test_response = process_command("Hello, who are you?")
        return {
            "status": "success", 
            "message": "Jarvis is working!",
            "test_response": test_response
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Jarvis test failed: {str(e)}"
        }