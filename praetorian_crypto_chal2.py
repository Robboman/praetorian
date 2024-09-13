import base64
from PIL import Image
from io import BytesIO

# Base64 string
base64_string = "<b64 string>"

# Decode Base64 string
image_data = base64.b64decode(base64_string)

# Open image using Pillow
image = Image.open(BytesIO(image_data))

# Save image to file
image.save("decoded_image.png")

# Extract and display basic image information
print(f"Image format: {image.format}")
print(f"Image size: {image.size}")
print(f"Image mode: {image.mode}")

# Extract EXIF data
exif_data = image.getexif()

# Print EXIF data
if exif_data:
    print("\nEXIF Metadata:")
    for tag_id, value in exif_data.items():
        tag_name = Image.ExifTags.TAGS.get(tag_id, tag_id)
        print(f"{tag_name}: {value}")
else:
    print("No EXIF data found.")
