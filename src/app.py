#!/usr/bin/env python3
"""
cloud-node-app - Agrarian Application
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {
        "name": "cloud-node-app",
        "version": "1.0.0",
        "status": "running",
        "description": "Agrarian cloud-node-app application"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
