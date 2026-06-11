from Bio import SeqIO
import numpy as np

def fasta_to_numeric(fasta_file):
    # Mapping DNA to integers
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Convert sequence string to list of numbers
        seq_numeric = [mapping.get(base, 0) for base in record.seq.upper()]
        sequences.append(seq_numeric)
    
    return np.array(sequences)

# Read the file
file_path = "final_merged.fasta" # Apni file ka naam yahan likhein
data = fasta_to_numeric(file_path)

print("Data shape (Sequences, Length):", data.shape)
print("Pehli 5 positions (Numerical):", data[0][:5])