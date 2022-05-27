import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

FULLSTACK_FRONTEND = os.getenv("FULLSTACK_FRONTEND", "")

origins = [
    FULLSTACK_FRONTEND,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root(num: int = 0):
    return "Returning data from FastAPI"