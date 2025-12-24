import numpy as np
import hashlib

def generate_embedding(text: str, dim: int = 384):
    """
    Prototype embedding generator.
    Deterministic and reproducible for demo.
    """
    h = hashlib.sha256(text.encode()).digest()
    np.random.seed(int.from_bytes(h[:4], "little"))
    return np.random.rand(dim).tolist()