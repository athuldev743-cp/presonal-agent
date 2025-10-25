# main_api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

app = FastAPI(title="Jarvis AI API")

# CORS configuration
origins = [
    "https://personal-ai-front.vercel.app",
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Jarvis AI API is running!"}

@app.get("/test")
async def test_jarvis():
    test_response = process_command("Hello, who are you?")
    return {
        "status": "success", 
        "message": "Jarvis is working!",
        "test_response": test_response
    }

@app.post("/ask")
async def ask_jarvis(cmd: Command):
    response = process_command(cmd.text)
    return {"response": response}