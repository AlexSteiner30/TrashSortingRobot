# Reference: https://fabacademy.org/2022/labs/kamakura/students/atsufumi-suzuki/Final%20Project/5.final-project-image-recognition.html

# Import Libraries
import time
import tensorflow as tf
import numpy as np
import cv2

percentage = 50

model_path = "../TrainingModel/model.tflite"

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

    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    detection = interpreter.get_tensor(output_details[0]["index"])

    return detection

def draw_detection(frame, detection):
    count = 1
    for i, s in enumerate(detection[0]):
        if(s*100 >= percentage):
            tag = f"{classes[i]}: {s*100:.2f}%"
            cv2.putText(frame, tag, (10, 20 * count), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            count += 1

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