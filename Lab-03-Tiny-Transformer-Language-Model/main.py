# Lab 03 - Tiny Transformer Language Model

import torch
import torch.nn as nn

sample_text = "Once upon a time"

chars = sorted(list(set(sample_text)))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

print("Vocabulary Size:", len(chars))
print("Characters:", chars)

class TinyTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim=32):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        return self.fc(x)

model = TinyTransformer(len(chars))

input_ids = torch.tensor([[stoi[c] for c in sample_text[:5]]])

output = model(input_ids)

print("Model Output Shape:", output.shape)
print("Tiny Transformer Model Created Successfully!")
