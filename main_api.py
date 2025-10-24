# main_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_command

app = FastAPI(title="Jarvis AI Assistant")

# Pydantic model for incoming commands
class Command(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Jarvis AI Assistant is running!"}

@app.post("/command")
def handle_command(cmd: Command):
    """
    Accepts a user command and returns Jarvis's response.
    """
    response = process_command(cmd.text)
    return {"response": response}
