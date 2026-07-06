from PIL import Image, ImageOps
import numpy as np
import os


class ImageProcessor:

    def __init__(self, image_path):
        self.image_path = image_path
        self.image_name = os.path.basename(image_path)

    # Load Image
    def load_image(self):
        image = Image.open(self.image_path).convert("RGB")
        return image

    # Resize Image
    def resize_image(self, image, width, height):
        return image.resize((width, height))

    # Padding
    def add_padding(self, image, left, top, right, bottom, fill="black"):
        padding = (left, top, right, bottom)
        return ImageOps.expand(image, border=padding, fill=fill)

    # Normalize Image
    def normalize(self, image):
        return np.array(image, dtype=np.float32) / 255.0

    # Save Image
    def save_image(self, image, output_folder):

        os.makedirs(output_folder, exist_ok=True)

        save_path = os.path.join(output_folder, self.image_name)

        image.save(save_path)

        print(f"\nImage Saved Successfully")
        print(f"Location : {save_path}")

    # Extract Pixels
    def extract_pixels(self, image_array, output_file):

        height, width, channels = image_array.shape

        with open(output_file, "w") as file:

            file.write(f"Image Name : {self.image_name}\n")
            file.write(f"Height     : {height}\n")
            file.write(f"Width      : {width}\n")
            file.write(f"Channels   : {channels}\n\n")

            for i in range(height):
                for j in range(width):
                    pixel = image_array[i, j]
                    file.write(f"Pixel ({i}, {j}) = {pixel}\n")

        print("Pixel Extraction Completed")


# ---------------- MAIN ---------------- #

path = "src/Images/Original Image/sample.png"

processor = ImageProcessor(path)

# Load Image
img = processor.load_image()

# Resize
width = int(input("Enter Width : "))
height = int(input("Enter Height : "))

img = processor.resize_image(img, width, height)

# Padding
choice = input("Add Padding? (yes/no): ").strip().lower()

if choice == "yes":

    left = int(input("Left   : "))
    top = int(input("Top    : "))
    right = int(input("Right  : "))
    bottom = int(input("Bottom : "))

    img = processor.add_padding(img, left, top, right, bottom)

# Save Image
processor.save_image(
    img,
    "src/Images/Resized Data"
)

# Normalize
img_array = processor.normalize(img)

print("\nImage Shape :", img_array.shape)

# Extract Pixels
processor.extract_pixels(
    img_array,
    "src/store/PixelValue.txt"
)