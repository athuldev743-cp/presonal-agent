# simple_test.py - Minimal working API
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
async def root():
    return {"message": "JARVIS API is working!"}

@app.get("/test")
async def test():
    return {"status": "success", "message": "Test endpoint working"}

@app.post("/ask")
async def ask():
    return {"response": "Hello from JARVIS!"}