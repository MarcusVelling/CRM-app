from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",  # Local development
    "https://crm-frontend.onrender.com",  # Production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 