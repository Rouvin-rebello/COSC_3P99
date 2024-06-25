import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split

# Define the transformation
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Load the full training dataset
dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# Split the dataset into 5 clients
num_clients = 5
client_datasets = random_split(dataset, [len(dataset) // num_clients] * num_clients)

# Create DataLoader for each client
client_loaders = [DataLoader(client_data, batch_size=32, shuffle=True) for client_data in client_datasets]

# Load the test dataset
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)


# Define the model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Train the model
def train(model, train_loader, epochs=1):
    model.train()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()


# Federated averaging
def federated_averaging(global_model, client_models):
    global_dict = global_model.state_dict()
    for k in global_dict.keys():
        global_dict[k] = torch.stack([client_models[i].state_dict()[k].float() for i in range(num_clients)], 0).mean(0)
    global_model.load_state_dict(global_dict)


# Test the model
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
    accuracy = 100 * correct / total
    return accuracy


# Initialize the global model
global_model = SimpleNN()

# Training loop
num_rounds = 10
for round in range(num_rounds):
    client_models = [SimpleNN() for _ in range(num_clients)]
    for client_model in client_models:
        client_model.load_state_dict(global_model.state_dict())

    # Train each client model locally
    for i, client_loader in enumerate(client_loaders):
        train(client_models[i], client_loader, epochs=1)

    # Aggregate the client models into the global model
    federated_averaging(global_model, client_models)

    # Test the global model after each round
    accuracy = test(global_model, test_loader)
    print(f"Round {round + 1} complete - Accuracy: {accuracy:.2f}%")

print("Federated training complete")
