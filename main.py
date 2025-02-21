from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Define request model
class DataRequest(BaseModel):
    data: List[str]

# User details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.post("/bfhl")
def process_data(request: DataRequest):
    try:
        numbers = sorted([x for x in request.data if x.isdigit()], key=int)
        alphabets = sorted([x for x in request.data if x.isalpha()], key=str.lower)
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
