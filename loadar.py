# model_manager.py
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import Optional
from threading import Lock

class ModelManager:
    """
    A singleton class to manage the SentenceTransformer model instance.
    This ensures only one instance of the model is loaded in memory across all modules.
    """
    _instance: Optional['ModelManager'] = None
    _lock: Lock = Lock()
    _model: Optional[SentenceTransformer] = None

    def __new__(cls):
        # Double-checked locking pattern for thread safety
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ModelManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize the model only once
        if self._model is None:
            with self._lock:
                if self._model is None:
                    self._model = SentenceTransformer('thenlper/gte-base')

    def get_model(self) -> SentenceTransformer:
        """Returns the singleton model instance."""
        return self._model

    def generate_embedding(self, text: str) -> np.ndarray:
        """Generate embeddings for a single text."""
        return self._model.encode(text, normalize_embeddings=True)