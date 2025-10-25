# app.py - RENDER AUTO-DETECTS THIS
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
    return {"message": "🎉 JARVIS BACKEND IS WORKING!"}

@app.get("/test")
def test():
    return {"status": "success", "message": "API is fully operational"}

@app.post("/ask")
def ask():
    return {"response": "Hello! I'm JARVIS and ready to assist you!"}