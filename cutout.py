import os
import requests
from PIL import Image
from io import BytesIO

API_KEY = "oQJBQf3JcU3zjtjEVCoXazC9"  # Your Remove.bg API key

input_folder = "input"          # Folder containing your car images
output_folder = "cutout_cars"  # Folder to save transparent cutout PNGs
os.makedirs(output_folder, exist_ok=True)

def remove_background(input_path, output_path):
    with open(input_path, "rb") as f:
        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            files={"image_file": f},
            data={"size": "auto"},
            headers={"X-Api-Key": API_KEY},
        )
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(output_path)
        print(f"Saved clean cutout: {output_path}")
    else:
        print(f"Failed for {input_path}: {response.status_code} {response.text}")

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
        remove_background(input_path, output_path)
