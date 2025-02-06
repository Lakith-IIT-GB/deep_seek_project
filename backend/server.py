import uvicorn
from websock import app

if __name__ == "__main__":
    uvicorn.run(
        "websock:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )