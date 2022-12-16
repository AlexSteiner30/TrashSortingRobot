# Reference: https://fabacademy.org/2022/labs/kamakura/students/atsufumi-suzuki/Final%20Project/5.final-project-image-recognition.html

# Import Libraries
import time
import tensorflow as tf
import numpy as np
import cv2

model_path = "../TrainingModel/TensorFlow/saved_model.pb"

model = tf.keras.models.load_model(model_path)

# Functions
def preprocess_image(image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  image = cv2.resize(image, (224, 224))

  image = image / 255.0
  image = image - 0.5
  image = image * 2.0

  image = image + np.random.normal(0, 0.1, size=image.shape)

  return image

def detect(frame):
    predictions = model.predict(frame)

    print(predictions)

    return 1


def main():
    vid = cv2.VideoCapture(0)
    time.sleep(2)

    while True:
        ret, frame = vid.read()

        detection = detect(frame)

        cv2.imshow("Trash Sorting Robot", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()