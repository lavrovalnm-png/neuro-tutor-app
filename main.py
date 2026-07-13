
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NeuroTutor AI")

class ChatRequest(BaseModel):
subject: str
message: str

@app.get("/")
async def root():
return {"message": "Нейрорепетитор запущен!"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
return {"response": f"Привет! Я твой репетитор по {request.subject}. Ты сказал: {request.message}"}

# Это самая важная часть для Vercel!
if __name__ == "__main__":
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
