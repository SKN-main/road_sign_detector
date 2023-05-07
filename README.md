# Road Sign Detector

This is a project aimed at detecting and classifying road signs using YOLOv8. The project is written in Python and uses PyTorch and OpenCV libraries. 

The current version of the project uses YOLO for detecting road signs. The model has been trained on a dataset of various road signs using transfer learning techniques. The trained model can detect and classify the following road signs: compulsory turn left (c4), compulsory turn right (c2), stop (b20) and roundabout (c12). 

## Installation

To install the necessary packages, run the following command

```
pip install -r requirements.txt
```

After installing the required libraries, you can download the project code from the GitHub repository:

```
git clone https://github.com/SKN-main/road_sign_detector.git
```

## Usage

To use the road sign detector, you need to run the `detect.py` script, which takes an image or a video file as input and outputs the detected road signs with their labels.

```
python detect.py --i <path_to_image_file>
```

or 

```
python detect.py --v <path_to_video_file>
```


## Contributing

If you find any bugs or have any suggestions for improving the project, please feel free to create an issue or submit a pull request on the GitHub repository.
