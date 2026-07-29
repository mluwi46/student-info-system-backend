from fastapi import FastAPI, UploadFile
import boto3

app = FastAPI()

s3 = boto3.client("s3")
BUCKET_NAME = "student-assignments-bucket"

@app.post("/upload-assignment/")
async def upload_assignment(file: UploadFile):
    s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
    return {"message": f"{file.filename} uploaded successfully"}
