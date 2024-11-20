import os
from typing import List, Optional, Union
from pydantic import BaseModel
from fastapi import FastAPI, Request
from typing import Optional, List, Dict

import json
import uvicorn


app = FastAPI(title="RAG-Link-api")


@app.get("/")
async def health(request: Request):
    return "Server up and running"



if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        api,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        debug=os.getenv("DEBUG", False),
        log_level=os.getenv("LOG_LEVEL", "info"),
        proxy_headers=True,
    )
