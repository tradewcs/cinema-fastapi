from fastapi import FastAPI
import config.settings as settings


app = FastAPI(
    title="Project Title",
    description="Description of project"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
