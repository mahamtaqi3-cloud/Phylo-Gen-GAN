import torch
import torch.nn as nn
import torch.optim as optim
from gan_model import Generator, Discriminator
import numpy as np

# 1. Dummy Data Loading (Replace this with your actual data from convert_dna.py)
# For now, we create random tensors to represent 11 sequences of length 100
real_data = torch.randn(11, 100) 

# 2. Setup models
gen = Generator(input_dim=10, output_dim=100)
disc = Discriminator(input_dim=100)

# 3. Training setup
optimizer_g = optim.Adam(gen.parameters(), lr=0.001)
optimizer_d = optim.Adam(disc.parameters(), lr=0.001)
criterion = nn.BCELoss()

# 4. Simple Training Loop
for epoch in range(100):
    # Train Discriminator
    noise = torch.randn(11, 10)
    fake_data = gen(noise)
    
    # Simple labels: 1 for real, 0 for fake
    loss_d = criterion(disc(real_data), torch.ones(11, 1)) + \
             criterion(disc(fake_data.detach()), torch.zeros(11, 1))
    
    optimizer_d.zero_grad()
    loss_d.backward()
    optimizer_d.step()
    
    # Train Generator
    loss_g = criterion(disc(fake_data), torch.ones(11, 1))
    
    optimizer_g.zero_grad()
    loss_g.backward()
    optimizer_g.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss D: {loss_d.item():.4f}, Loss G: {loss_g.item():.4f}")

print("Training Complete!")

# Save the Generator model
torch.save(gen.state_dict(), 'generator_weights.pth')
print("Model saved successfully!")