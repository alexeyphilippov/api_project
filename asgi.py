import uvicorn

if __name__ == "__main__":
    uvicorn.run('app:create_app', host="localhost", factory=True, port=8070, workers=1)  # noQA
