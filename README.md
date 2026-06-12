# Phylo-Gen-GAN

Phylo-Gen-GAN is an innovative AI-driven framework designed to bridge the gap between deep learning and evolutionary biology. This project utilizes Generative Adversarial Networks (GANs) for Ancestral Sequence Reconstruction (ASR), providing a novel computational approach to predict ancestral DNA states.

## 🧬 Project Overview

Traditional ASR methods rely heavily on statistical models like Maximum Likelihood (ML) and specific evolutionary assumptions (e.g., GTR models). **Phylo-Gen-GAN** introduces a deep learning paradigm that learns evolutionary patterns directly from aligned sequences to reconstruct ancestral nodes.

## 🚀 Key Features

* **GAN-based Architecture:** Implements a generator and discriminator network tailored for DNA sequence pattern learning.
* **Interdisciplinary Approach:** Combines bioinformatics principles with modern AI optimization.
* **Benchmarking:** Validated against classical phylogenetic models in MEGA12 to ensure biological plausibility.

## 🛠 Technologies Used

* **Languages:** Python
* **Deep Learning:** PyTorch (GAN architectures)
* **Bioinformatics Tools:** MEGA12, FASTA, MAFFT (for sequence alignment)
* **Data Science:** NumPy, Pandas

## 📂 Repository Structure

* `gan_model.py`: Core architecture for the Generator and Discriminator.
* `train.py`: Training loop and model optimization logic.
* `generate.py`: Inference script to reconstruct ancestral sequences.
* `README.md`: Project documentation.

## 💡 How to Run

1. Clone the repository:
```bash
git clone https://github.com/mahamtaqi3-cloud/Phylo-Gen-GAN.git

```



```
2. Install dependencies:
   ```bash
   pip install torch numpy

```

3. Run the generator script:
```bash

```



python generate.py

```

## 🤝 Contribution
Contributions to improve the model's accuracy or to integrate new phylogenetic constraints are welcome. Please open an issue or submit a pull request.

