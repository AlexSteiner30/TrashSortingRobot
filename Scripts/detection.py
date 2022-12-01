import os
import cv2

from detecto.core import Model
from detecto import utils, visualize

# Loading model
model = Model.load("model.pth", ['plasticBottle', 'plasticCap', 'plasticBag', 'paperBag'])

# Clear console
os.system('clear')

# Analize image & render it
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)

startPos = (0, 0)
endPos = (0, 0)

color = (0, 0, 0)

org = (0, 0)

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = vid.read()

    cv2.imwrite('frame.png', frame)

    image = utils.read_image('frame.png') 
    labels, boxes, scores = model.predict(image) 

    #Frame Rendering
    count = 0
    for x in labels:
        org = (0, count + 5)
        frame = cv2.putText(frame, labels[count] + " " + str(scores[count] * 100).replace('tensor(', '').replace(')', '') + "%", org, font, 0.5, color, 1, cv2.LINE_AA)
        count += 1;

        
    cv2.imshow('Trash Sorting Robot', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()