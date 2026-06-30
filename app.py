from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "GlobalScart 360",
        "status": "Running on AWS EC2",
        "developer": "CH V Sai Girish"
    }
