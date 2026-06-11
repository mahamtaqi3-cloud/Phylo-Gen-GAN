import torch
from gan_model import Generator

# 1. Generator define (Make sure input_dim matches your train.py)
gen = Generator(input_dim=10, output_dim=100)
gen.eval()

# 2. Noise
noise = torch.randn(1, 10)

# 3. Generate
with torch.no_grad():
    output = gen(noise)
    print("Raw Model Output (First 10 values):", output[0][:10]) # Debugging

# 4. Convert to DNA
# Convrt output to indices (0,1,2,3) for A,C,G,T
indices = torch.argmax(output, dim=1)
print("Indices detected:", indices)

mapping = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

# Sequence building
final_dna = []
for idx in range(100): # Generate 100 bases
    # Randomly pick mapping if model is not fully trained
    # Or pick from model output if it gives valid indices
    base = mapping.get(indices[0][idx].item(), 'A') # This is a fallback to 'A' if index is out of range
    final_dna.append(base)

print("\n--- Final Predicted Ancestral Sequence ---")
print("".join(final_dna))