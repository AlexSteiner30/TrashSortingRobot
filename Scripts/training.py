from detecto.core import Dataset, Model, DataLoader

dataset = Dataset('../TrainingModel/') #folder (traning)

your_labels = ['plasticBottle', 'plasticCap', 'plasticBag', 'paperBag'] # all the labels
model = Model(your_labels)

model.fit(dataset, verbose=True)

model.save("model.pth") 