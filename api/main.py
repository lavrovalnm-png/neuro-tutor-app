from fastapi import FastAPI
app = FatAPI()

@app.get("/")
async def root():
return {"message": "Работает!"}
