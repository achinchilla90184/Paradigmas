import numpy as np
import cv2
import time


# Colors and Constants
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (176, 130, 39)
ORANGE = (0, 127, 255)

# Create Car Classifier
xmlCar = './testing/src/cars.xml'
CLF = cv2.CascadeClassifier(xmlCar)
FONT = cv2.FONT_HERSHEY_COMPLEX

# Configuration
offset = 6
fps = 60
min_width = 80
min_height = 80
linePos = 550

ground_truth1 = 62
ground_truth2 = 36


# get center position of the car
def center_position(x, y, w, h):
    center_x = x + (w // 2)
    center_y = y + (h // 2)
    return center_x, center_y


def objectCounter(path):
    CAP = cv2.VideoCapture(path)

    # Configuration for detection
    detect_vehicle = []
    vehicle_counts = 0

    while CAP.isOpened():
        duration = 1 / fps
        time.sleep(duration)

        # Read first frame
        ret, frame = CAP.read()
        if frame is None:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 5)

        # Pass frame to our car classifier
        vehicle = CLF.detectMultiScale(
            blur,
            scaleFactor=1.2,    # how much the image size is reduced at each image scale
            minNeighbors=2,     # how many neighbors each candidate rectangle should have to retain it
            minSize=(min_width, min_height)
        )

        # Count if the car pass this line
        cv2.line(frame, (25, linePos), (1200, linePos), BLUE, 2)

        # Extract bounding boxes for any car identified
        for (x, y, w, h) in vehicle:
            cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)

            center = center_position(x, y, w, h)
            detect_vehicle.append(center)
            cv2.circle(frame, center, 4, RED, -1)

            # if center of the car pass the counting line
            for x, y in detect_vehicle:
                if (y < linePos + offset) and (y > linePos - offset):
                    cv2.line(frame, (25, linePos), (1200, linePos), ORANGE, 3)
                    detect_vehicle.remove((x, y))
                    vehicle_counts += 1

        cv2.putText(
            frame, f"Car Detected: {vehicle_counts}", (50, 70), FONT, 2, RED, 3, cv2.LINE_AA)
        cv2.imshow('Vehicles Detection', frame)

        # Press 'ESC' Key to Quit
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    CAP.release()

    print(str(vehicle_counts))
    return vehicle_counts