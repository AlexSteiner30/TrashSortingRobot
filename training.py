from detecto import core, utils
from torchvision import transforms
import matplotlib.pyplot as plt
from detecto.core import Dataset, Model, DataLoader

dataset = Dataset('train/') #folder (traning)

your_labels = ['label1', 'label2', '...'] # all the labels
model = Model(your_labels)

model.fit(dataset, verbose=True)

model.save("model.pth") 