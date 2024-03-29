# Reference: https://fabacademy.org/2022/labs/kamakura/students/atsufumi-suzuki/Final%20Project/5.final-project-image-recognition.html

# Import Libraries
import time
import tensorflow as tf
import numpy as np
import cv2

import robot

percentage = 50

model_path = "../TrainingModel/model_unquant.tflite"

interpreter = tf.lite.Interpreter(model_path=model_path) # Load the model
interpreter.allocate_tensors() # Memory allocation

# Get the properties of the input and output layers of the training model
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Obtaining the tensor data configuration of the input layer
target_height = input_details[0]["shape"][1]
target_width = input_details[0]["shape"][2]

# Load the classes
f = open("../TrainingModel/labels.txt", "r")
lines = f.readlines()
f.close()
classes = {}

for line in lines:
    pair = line.strip().split(maxsplit=1)
    classes[int(pair[0])] = pair[1].strip()

def detect(frame):
    resized = cv2.resize(frame, (target_width, target_height))

    input_data = np.expand_dims(resized, axis=0)
    input_data = (np.float32(input_data) - 127.5) / 127.5
    interpreter.set_tensor(input_details[0]["index"], input_data)
    interpreter.invoke()

    detection = interpreter.get_tensor(output_details[0]["index"])

    return detection

def draw_detection(frame, detection):
    count = 1
    for i, s in enumerate(detection[0]):
        tag = classes[i] + str(int(s*100)) + "%"

        if s*100 >= percentage :
            print(tag)

    return frame

def Sort(name):
    if name == "Bottle_Caps" or name == "Crushed_Bottles":
        print("Plastic detected!")
        robot.move("Plastic")

    elif name == "Mandarin_Peels" or name == "Banana_Peels":
        print("Organic detected!")
        robot.move("Organic")

    elif name == "A4_Paper" or name == "Paper_Tissues":
        print("Paper detected!")
        robot.move("Organic")

    else:
        print("Other object detected!")

def main():
    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, target_width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, target_height)

    time.sleep(2)

    while True:
        ret, frame = vid.read()

        detection = detect(frame)

        drawn = draw_detection(frame, detection)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
