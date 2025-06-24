import pytesseract
import cv2
import re
import os

def extract_dob_and_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    dob_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    dob = dob_match.group(0) if dob_match else "01/01/2000"

    face_path = os.path.join("uploads", "face_from_aadhar.jpg")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        cv2.imwrite(face_path, face)
        break

    return dob, face_path