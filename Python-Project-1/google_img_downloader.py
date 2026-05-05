import os
import requests
from googleapiclient.discovery import build
from PIL import Image
from io import BytesIO

API_KEY="AIzaSyCXiUva3JSadah63mFlaEh8CpxNH78HP6s"
SEARCH_ENGINE_ID="074f430f43bfe4e45"

def download_image(query,num_images=5):
    service=build("customsearch","v1",developerKey=API_KEY)
    results=service.cse().list(q=query,cx=SEARCH_ENGINE_ID,searchType="image",num=num_images).execute()

    if "items" not in results:
        print("No results Found..")
    if not os.path.exists("project1"):
        os.makedirs("project1")
    for i, item in enumerate(results.get("items", [])):
        link = item["link"]
        try:
            response = requests.get(link, timeout=5)
            img = Image.open(BytesIO(response.content)).convert("RGB")
            img.save(f"project1/{query}_{i+1}.jpg", "JPEG")
            print(f"project1: {query}_{i+1}.jpg")
        except Exception:
            print(f"Skipped {link} (not a valid image)")

imagetype=input("Enter The Name of the Image you want to search...")
nimage=int(input("Enter No.of Images to be generated.."))
download_image(imagetype, nimage)