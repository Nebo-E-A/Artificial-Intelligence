known_image = face_recognition.load_image_file("Image path here")
known_face_encoding = face_recognition.face_encodings(known_image)[0]
# Create a list of known face encodings and their corresponding names
known_face_encodings = [known_face_encoding]
known_face_names = ["Known Person"]

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame, number_of_times_to_upsample=5, model='hog')
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the current face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the known person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label it with the name
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        print(name)

    cv2.imshow('Exam Proctoring', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

