# Vehicle Number Detect

This project detects vehicle number plates using Python, OpenCV, and Cloudinary for storage and EasyOCR for optical character recognition.

## Prerequisites

- Python 3.7 (Anaconda recommended)
- Cloudinary account
- Google Colab

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/vehicle-number-detect.git
    cd vehicle-number-detect
    ```

2. **Install Required Modules**:
    ```bash
    pip install cloudinary opencv-python easyocr matplotlib
    ```

3. **Set Up Cloudinary**:
    - Sign up for a Cloudinary account if you don't have one.
    - Set your Cloudinary credentials as environment variables:

    On Windows:
    ```cmd
    set CLOUDINARY_CLOUD_NAME=your_cloud_name
    set CLOUDINARY_API_KEY=your_api_key
    set CLOUDINARY_API_SECRET=your_api_secret
    ```

    On Linux/Mac:
    ```bash
    export CLOUDINARY_CLOUD_NAME="your_cloud_name"
    export CLOUDINARY_API_KEY="your_api_key"
    export CLOUDINARY_API_SECRET="your_api_secret"
    ```

4. **Set Up Virtual Environment**:
    - Create and activate a virtual environment with Python 3.7:
    ```bash
    conda create -n number-detect python=3.7
    conda activate number-detect
    ```

5. **Run the Main Script**:
    - Capture and upload the vehicle number plate image:
    ```bash
    python main.py
    ```

6. **Process the Image on Google Colab**:
    - Open `RunOnColab.ipynb` in Google Colab.
    - Connect to the Colab runtime.
    - Run all cells to see the decoded text from the uploaded image.

## How It Works

1. **Capture Image**:
    - The `main.py` script captures an image from the webcam, detects the vehicle number plate, and uploads it to Cloudinary.

2. **Process Image**:
    - The `check.py` script (or cells in `RunOnColab.ipynb`) fetches the uploaded image from Cloudinary and processes it using EasyOCR to extract the text.

## Contact

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).
