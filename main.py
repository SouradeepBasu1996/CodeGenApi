from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "FastAPI wrapper for CodeLlama is running!"}


@app.post("/generate")
async def generate_code(request: PromptRequest):
    """
    Calls the local Ollama instance running CodeLlama to generate code based on the given prompt.
    """
    model_name = "codellama:7b"  # Ensure this model is available in Ollama
    response = ollama.chat(
        model=model_name, messages=[{"role": "user", "content": request.prompt}]
    )

    return {"response": response["message"]}
