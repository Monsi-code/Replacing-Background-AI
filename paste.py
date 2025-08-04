import os
from PIL import Image

# Paths
background_path = 'input/background.jpg'
cutout_folder = 'cutout_cars'
output_folder = 'output'

os.makedirs(output_folder, exist_ok=True)

# Load background image
background = Image.open(background_path).convert('RGBA')

# List all image files in cutout_cars folder
car_filenames = [f for f in os.listdir(cutout_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for car_filename in car_filenames:
    # Load car image with transparency
    car_path = os.path.join(cutout_folder, car_filename)
    car = Image.open(car_path).convert('RGBA')

    # Create a copy of background to paste onto (so original bg stays unchanged)
    composite = background.copy()

    # Calculate position to paste the car (e.g., center)
    bg_w, bg_h = composite.size
    car_w, car_h = car.size
    position = ((bg_w - car_w) // 2, (bg_h - car_h) // 2)

    # Paste the car image onto the background, using the alpha channel as mask
    composite.paste(car, position, mask=car)

    # Save the output image
    output_path = os.path.join(output_folder, f'composite_{car_filename}')
    composite.save(output_path)

    print(f'Saved {output_path}')
