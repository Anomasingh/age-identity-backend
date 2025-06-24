from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.ocr import extract_dob_and_face
from utils.face_match import compare_faces
from utils.age_utils import calculate_age

app = Flask(name)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/verify', methods=['POST'])
def verify():
aadhar_file = request.files.get('aadhar')
selfie_file = request.files.get('selfie')

if not aadhar_file or not selfie_file:
    return jsonify({'error': 'Missing files'}), 400

aadhar_path = os.path.join(UPLOAD_FOLDER, 'aadhar.jpg')
selfie_path = os.path.join(UPLOAD_FOLDER, 'selfie.jpg')

aadhar_file.save(aadhar_path)
selfie_file.save(selfie_path)

dob, face_path = extract_dob_and_face(aadhar_path)
age = calculate_age(dob)
confidence = compare_faces(face_path, selfie_path)

return jsonify({
    "age": age,
    "dob": dob,
    "matchConfidence": round(confidence, 2),
    "status": "verified" if age >= 18 and confidence >= 70 else "not_verified"
})
if name == "main":
print("✅ Flask backend starting on http://localhost:5000")
app.run(debug=True)