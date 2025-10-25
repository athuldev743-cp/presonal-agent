# main_api.py - COMPLETE FIXED VERSION
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

app = FastAPI(title="Jarvis AI API")

# === PERMISSIVE CORS CONFIGURATION ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow ALL origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow ALL methods
    allow_headers=["*"],  # Allow ALL headers
)

class Command(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Jarvis AI API is running!"}

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
        return {
            "status": "error",
            "message": f"Jarvis test failed: {str(e)}"
        }

@app.post("/ask")
async def ask_jarvis(cmd: Command):
    try:
        response = process_command(cmd.text)
        return {"response": response}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

# Explicit OPTIONS handler for CORS preflight
@app.options("/{rest_of_path:path}")
async def preflight_handler():
    return {}

@app.options("/ask")
async def ask_options():
    return {"message": "OK"}