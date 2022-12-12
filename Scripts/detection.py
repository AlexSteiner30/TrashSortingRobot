# Reference: https://fabacademy.org/2022/labs/kamakura/students/atsufumi-suzuki/Final%20Project/5.final-project-image-recognition.html

# Import Libraries
import time
import tensorflow as tf
import numpy as np
import cv2

model_path = "model.tflite"

interpreter = tf.lite.Interpreter(model_path=model_path) # Load the model
interpreter.allocate_tensors() # Memory allocation

# Get the properties of the input and output layers of the training model
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Obtaining the tensor data configuration of the input layer
target_height = input_details[0]["shape"][1]
target_width = input_details[0]["shape"][2]

# Load the classes
f = open("labels.txt", "r")
lines = f.readlines()
f.close()
classes = {}

for line in lines:
    pair = line.strip().split(maxsplit=1)
    classes[int(pair[0])] = pair[1].strip()

def detect(frame):
    resized = cv2.resize(frame, (target_width, target_height))
    input_data = np.expand_dims(resized, axis=0)
    input_data = (np.float32(input_data) - 127.5) / 127.5 # Each RGB 0 ~ 255 pixel value should fall in the range of -1 to 1
    interpreter.set_tensor(input_details[0]["index"], input_data) # Set pointer to tensor data in index

    interpreter.invoke()
    detection = interpreter.get_tensor(output_details[0]["index"])

    return detection

def draw_detection(frame, detection):
    for i, s in enumerate(detection[0]):
        tag = f"{classes[i]}: {s*100:.2f}%"
        cv2.putText(frame, tag, (10, 20 + 20 * i),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    return frame

def main():
    vid = cv2.VideoCapture(0)
    time.sleep(2)

    while True:
        ret, frame = vid.read()

        detection = detect(frame)
        value = classes[detection.tolist()[0].index(max(detection.tolist()[0]))]

        drawn = draw_detection(frame, detection)
        cv2.imshow("frame", drawn)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()