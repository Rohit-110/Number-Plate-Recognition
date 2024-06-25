import matplotlib.pyplot as plt
import cv2
import easyocr
import os

# Configure Cloudinary with environment variables (same as in main.py)
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to process Cloudinary image URL with EasyOCR
def process_cloudinary_image(url):
    # Use the URL directly with EasyOCR (no need to download locally)
    img = cv2.imread(url)  # This is just a placeholder; OpenCV won't directly read URLs
    # Perform your image processing operations here
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Use EasyOCR to read text from image
    output = reader.readtext(img)
    return output

def main():
    # Example: Use a Cloudinary URL for an image named "scanned_img_0"
    cloudinary_url = cloudinary.utils.cloudinary_url("scanned_img_0.jpg", fetch_format="auto", quality="auto")[0]
    print("Cloudinary URL:", cloudinary_url)

    # Process the Cloudinary image URL with EasyOCR
    output = process_cloudinary_image(cloudinary_url)
    print("OCR Output:", output)

if __name__ == "__main__":
    main()
