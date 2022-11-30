from detecto.core import Dataset, Model, DataLoader

dataset = Dataset('your_images_and_labels/') #folder (traning)

your_labels = ['label1', 'label2', '...'] # all the labels
model = Model(your_labels)

model.fit(dataset, verbose=True)

model.save("model.pth") 