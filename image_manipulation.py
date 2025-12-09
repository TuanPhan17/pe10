from PIL import Image, ImageFilter     # Import Pillow classes for image handling and filters

def main():
    input_path = "/Users/tphizzel/Downloads/Los_Angeles_Lakers_logo.svg.png"   # File path to the input image

    img = Image.open(input_path)        # Load the image into memory

    img_resized = img.resize((300, 300))    # Resize the image to 300x300 pixels

    w, h = img_resized.size             # Get width and height of the resized image
    crop_size = 200                     # Define crop size
    left   = (w - crop_size) // 2       # Calculate left boundary (center crop)
    upper  = (h - crop_size) // 2       # Calculate upper boundary
    right  = left + crop_size           # Right boundary of crop box
    lower  = upper + crop_size          # Lower boundary of crop box
    cropped = img_resized.crop((left, upper, right, lower))   # Crop a centered 200x200 section

    rotated = cropped.rotate(45, expand=True)    # Rotate the cropped image 45 degrees and expand canvas

    gray = rotated.convert("L")         # Convert the rotated image to grayscale

    gray.save("output_task1.png")       # Save Task 1 result (grayscale, rotated, cropped, resized)
    print("Saved: output_task1.png")    # Print confirmation

    blurred = gray.filter(ImageFilter.BLUR)   # Apply a blur filter to the grayscale image

    blurred.save("output_task2.png")    # Save Task 2 result (blurred image)
    print("Saved: output_task2.png")    # Print confirmation


if __name__ == "__main__":              # Run main() only if the script is executed directly
    main()

