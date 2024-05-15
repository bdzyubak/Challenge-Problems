import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
import sys

import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

import itertools

# Example based on https://www.datacamp.com/tutorial/pytorch-tutorial-building-a-simple-neural-network-from-scratch


def main():
    X_train, X_test, y_train, y_test = prepare_data()

    batch_size = 64
    train_data = Data(X_train, y_train)
    train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)

    test_data = Data(X_test, y_test)
    test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=True)

    # Test loading

    # Set up model
    input_dim = 2
    hidden_dim = 10
    output_dim = 1
    model = NeuralNetwork(input_dim, hidden_dim, output_dim)
    print(model)

    if 'hiddenlayer' in sys.modules:
        batch = next(iter(train_dataloader))
        yhat = model(batch.text)  # Give dummy batch to forward().

    learning_rate = 0.1
    loss_fn = torch.nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    num_epochs = 100
    loss_values = []
    for epoch in range(num_epochs):
        for x, y in train_dataloader:
            optimizer.zero_grad()
            pred = model(x)
            loss = loss_fn(pred, y.unsqueeze(-1))
            loss_values.append(loss.item())
            loss.backward()
            optimizer.step()

    print("Training Complete")

    plot_loss(loss_values)

    y_pred = []
    points_total_image = 0
    points_predicted_correctly = 0
    with torch.no_grad():
        for x, y in test_dataloader:
            outputs = model(x)
            predicted = np.where(outputs < 0.5, 0, 1)
            predicted = list(itertools.chain(*predicted))
            y_pred.append(predicted)
            points_total_image += y.size(0)
            points_predicted_correctly += (predicted == y.numpy()).sum().item()

    print(f"The accuracy of the network in {len(y_test)} test images is: "
          f"{100 * points_predicted_correctly / points_total_image}")


def plot_loss(loss_values):
    step = np.linspace(0, 100, 10500)
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.plot(step, np.array(loss_values))
    plt.title("Step-wise Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show(block=False)


def prepare_data():
    # Create a dataset with 10,000 samples.
    X, y = make_circles(n_samples=10000,
                        noise=0.05,
                        random_state=26)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=26)

    # Visualize the data.
    fig, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(10, 5))
    train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.Spectral)
    train_ax.set_title("Training Data")
    train_ax.set_xlabel("Feature #0")
    train_ax.set_ylabel("Feature #1")
    test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
    test_ax.set_xlabel("Feature #0")
    test_ax.set_title("Testing data")
    plt.show(block=False)
    return X_train, X_test, y_train, y_test


class Data(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X.astype(np.float32))
        self.y = torch.from_numpy(y.astype(np.float32))
        self.len = self.X.shape[0]

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.len


class NeuralNetwork(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(NeuralNetwork, self).__init__()
        self.hidden_layer_1 = torch.nn.Linear(input_dim, hidden_dim)
        torch.nn.init.kaiming_uniform(self.hidden_layer_1.weight, nonlinearity='relu')
        self.hidden_layer_2 = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.nn.functional.relu(self.hidden_layer_1(x))
        x = torch.nn.functional.sigmoid(self.hidden_layer_2(x))
        return x



if __name__ == '__main__':
    main()
