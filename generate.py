from runwayml import RunwayML, TaskFailedError
import os
import requests

client = RunwayML(api_key="key_9c24eb5496fee3192aa76c8a1253eef4618a7833c588c4e0cd2ea8e04f6762535b4b7db81a686f1957145cbddda8e9b560db5da6c90cc2d30c9f50a6855e25c0")

# Base URL of your GitHub images
github_base_url = "https://raw.githubusercontent.com/Monsi-code/Replacing-Background-AI/main/referenceimages"

# List your actual image filenames
image_filenames = [
    "composite_Car11.png",
]

# Build the reference_images list with safe tags
reference_images = [
    {'uri': f"{github_base_url}/{filename}", 'tag': f"car{i+1}"}
    for i, filename in enumerate(image_filenames)
]

try:
    task = client.text_to_image.create(
        model='gen4_image',
        ratio='1920:1080',
        prompt_text=(
            "Adjusting the light and the shadow of the car to makes it look realistic, like it is actually in the background, keeping all the details of the car like scratches, including the point of view"
        ),
        reference_images=reference_images,
    ).wait_for_task_output()

    print("Task complete!")
    print("Image URL:", task.output[0])

    # Create final folder if it doesn't exist
    os.makedirs("final", exist_ok=True)

# URL of the generated image
    image_url = task.output[0]

# Download the image
    response = requests.get(image_url)
    response.raise_for_status()

# Save the image to a local file inside "final"
    output_path = os.path.join("final", "generated_car.png")
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"Image saved locally at {output_path}")


except TaskFailedError as e:
    print("The image failed to generate.")
    print(e.task_details)
