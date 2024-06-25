import os
import cv2
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url


harcascade = "model/haarcascade_russian_plate_number.xml"


cloudinary.config( 
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


cap = cv2.VideoCapture(0)

cap.set(3,640) #width
cap.set(4,480) #height

min_area = 500
count = 0

while True:
    sucess , img =cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_grey ,1.1 ,4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img , (x,y) , (x+w,y+h),(0,255,0))
            cv2.putText(img , "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)

            img_roi = img[ y: y+h,x: x+w]
            cv2.imshow("ROI",img_roi)

    cv2.imshow("Result",img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the image locally
        img_path = "plates/scanned_img_" + str(count) + ".jpg"
        img_id   = "Vechicle Number_"+str(count)
        cv2.imwrite(img_path, img_roi)
        
        # Upload the local image file to Cloudinary
        upload_result = cloudinary.uploader.upload(img_path, public_id=img_id)
        print(upload_result["secure_url"])
        
        optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
        print(optimize_url)
        
        auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
        print(auto_crop_url)
        
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
        