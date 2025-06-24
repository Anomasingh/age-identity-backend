from deepface import DeepFace

def compare_faces(id_face, selfie_face):
    try:
        result = DeepFace.verify(img1_path=id_face, img2_path=selfie_face, enforce_detection=False)
        if result["verified"]:
            return (1 - result["distance"]) * 100
    except Exception as e:
        print(f"Error in face comparison: {e}")
    return 0