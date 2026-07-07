# Import required libraries
import cv2
import numpy as np
from IPython.display import display, clear_output
from PIL import Image

# Load the Haar cascades for object detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Connect to your computer's default camera
cap = cv2.VideoCapture(0)

try:
    last_frame = None  # To store the last captured frame

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        frame = cv2.flip(frame, 1)

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Iterate through detected faces
        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # Detect eyes within the face region
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                # Draw rectangles around eyes
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
                cv2.putText(roi_color, 'Eye', (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the resulting frame in Jupyter Notebook
        clear_output(wait=True)
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        display(img)

        # Store the last captured frame
        last_frame = frame.copy()

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    # Stop capturing on interrupt
    print("Video capture stopped")

# Release the capture
cap.release()

# Display the last captured frame
if last_frame is not None:
    img = Image.fromarray(cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB))
    display(img)

cv2.destroyAllWindows()
