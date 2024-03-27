import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('train_log/single_model/stats.json', 'r') as file:
    data = json.load(file)

# Extract relevant fields
losses = [entry['loss'] for entry in data]
loss0 = [entry['syn/loss0'] for entry in data]
loss1 = [entry['syn/loss1'] for entry in data]
loss2 = [entry['syn/loss2'] for entry in data]
loss3 = [entry['syn/loss3'] for entry in data]
loss4 = [entry['syn/loss4'] for entry in data]
learning_rate = [entry['optimize/learning_rate'] for entry in data]
sum = [l0 + l1 + l2 + l3 + l4 for l0, l1, l2, l3, l4 in zip(loss0, loss1, loss2, loss3, loss4)]
epoch_nums = [entry['epoch_num'] for entry in data]
global_steps = [entry['global_step'] for entry in data]

# Plot the losses over epochs
plt.figure(figsize=(10, 6))
plt.plot(epoch_nums, losses, marker='o', linestyle='-')
plt.title('Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epoch_nums, learning_rate, marker='o', linestyle='-')
plt.title('Learning rate Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Learning rate')
plt.grid(True)
plt.show()