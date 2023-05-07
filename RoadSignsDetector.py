import torch
import cv2
import numpy as np


class RoadSignsDetector():
    CLASS_NAMES = ['c4', 'c2', 'b20', 'c12', 'a7']

    def __init__(self) -> None:
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/20e_street_20e_printed.pt')
        self.predicted_signs = []

    def predict(self, frame):
        original_size = frame.shape[:2][::-1]
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (640, 640))

        result = self.model(img)

        rendered_img = result.render()[0]
        rendered_img = cv2.resize(rendered_img, original_size)
        rendered_img = cv2.cvtColor(rendered_img, cv2.COLOR_RGB2BGR)

        self.predicted_signs = []
        for pred in result.xyxyn[0]:
            class_name = self.CLASS_NAMES[int(pred[5])]
            self.predicted_signs.append((*pred[:4].numpy(), class_name))

        return rendered_img
    
    def get_predicted_signs(self):
        """
        The function returns a list of detected road signs as: (x_cetner, y_center, width, height, class_name).
        The coordintates are represented in the form of floats which are relative distances from left top corner.
        """
        return self.predicted_signs

if __name__ == '__main__':
    print("Hello world")

    cap = cv2.VideoCapture(0)
    detector = RoadSignsDetector()

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        img = detector.predict(frame)
        predicted_signs = detector.get_predicted_signs()

        print(predicted_signs)

        if len(predicted_signs):
            cv2.putText(img, f"Znak {predicted_signs[0][-1]}", (50, 75), 1, 5, (0, 0, 255), 2)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

