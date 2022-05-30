import boto3
import psycopg2
from psycopg2 import Error

from typing import List
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI, UploadFile

from fastapi.middleware.cors import CORSMiddleware

S3_BUCKET_NAME = "video-app-upload-13"


class VideoModel(BaseModel):
    id: int
    video_title: str
    video_url: str


app = FastAPI(debug=True)
# allow requests between back/frontends
app.add_middleware(
    CORSMiddleware,
    # anyone
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    conn = psycopg2.connect( 
        database="videoStorage", user="docker", password="docker", host="0.0.0.0"
    )

    cursor = conn.cursor()
    # add id auto-increment sequence
    sequence = "CREATE SEQUENCE cateogry_id_seq; ALTER TABLE videos ALTER COLUMN id SET DEFAULT nextval('cateogry_id_seq');"
    cursor.execute(sequence)
    conn.commit()
    print("Table updated successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")


@app.get("/status")
async def check_status():
    return "Hello World!"


@app.get("/videos", response_model=List[VideoModel])
async def get_videos():
    # Connect to our database
    conn = psycopg2.connect( 
        database="videoStorage", user="docker", password="docker", host="0.0.0.0"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM videos ORDER BY id DESC")
    rows = cur.fetchall()

    formatted_videos = []
    for row in rows:
        formatted_videos.append(
            VideoModel(id=row[0], video_title=row[1], video_url=row[2])
        )

    cur.close()
    conn.close()
    return formatted_videos


@app.post("/videos", status_code=201)
async def add_photo(file: UploadFile):
    # Upload file to AWS S3
    s3 = boto3.resource("s3")
    # s3.create_bucket(Bucket=S3_BUCKET_NAME)
    bucket = s3.Bucket(S3_BUCKET_NAME)
    bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL": "public-read"}) # lets anyone who watches download

    uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file.filename}"

    # Store URL in database
    conn = psycopg2.connect(
        database="videoStorage", user="docker", password="docker", host="0.0.0.0"
    )
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO videos (video_title, video_url) VALUES ('{file.filename}', '{uploaded_file_url}' )"
    )
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)