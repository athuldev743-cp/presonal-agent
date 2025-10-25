# app.py - ULTRA SIMPLE
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ JARVIS BACKEND WORKING!"}

@app.post("/ask")
def ask():
    return {"response": "I'm alive! 🎉"}