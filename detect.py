import getopt, sys
from RoadSignsDetector import RoadSignsDetector
import cv2


def show_video(source):
    print("source:", source)
    cap = cv2.VideoCapture(source)
    detector = RoadSignsDetector()

    if not cap.isOpened():
        print("Cannot open the video/camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        img = detector.predict(frame)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def show_image(path):
    detector = RoadSignsDetector()
    image = cv2.imread(path)
    pred = detector.predict(image)
    cv2.imshow('Prediction', pred)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    argumentList = sys.argv[1:]
    
    options = "v:i:"
    
    long_options = ["Video", "Img"]
    
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-v", "--Video"):
                show_video(currentValue)
            elif currentArgument in ("-i", "--Image"):
                show_image(currentValue)

                
    except getopt.error as err:
        print (str(err))