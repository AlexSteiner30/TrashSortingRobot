from detecto import core, utils
from torchvision import transforms
import matplotlib.pyplot as plt

from detecto.core import Dataset

dataset = Dataset('your_images_and_labels/')
dataset = Dataset('your_labels/', 'your_images/')

from detecto.utils import xml_to_csv

xml_to_csv('your_labels/', 'labels.csv')
dataset = Dataset('labels.csv', 'your_images/')

from detecto.core import DataLoader, Model

# Specify all unique labels you're trying to predict
your_labels = ['label1', 'label2', '...']
model = Model(your_labels)

model.fit(dataset, verbose=True)

model.save("model.pth")