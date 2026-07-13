from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
return {"message": "Ура! Работает! 🎉"}

@app.post("/chat")
async def chat_endpoint(request_data: dict):
return {"response": f"Привет! Я твой нейрорепетитор. Ты написал: {request_data}"}
