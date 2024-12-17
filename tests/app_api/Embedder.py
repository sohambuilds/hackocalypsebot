import numpy as np
from transformers import BertTokenizer, TFBertModel

# 3. Embedder Class
class Embedder:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = TFBertModel.from_pretrained("bert-base-uncased")

    def get_embeddings(self, texts):
        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="tf", max_length=512)
        outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.numpy()  # Use the last hidden state
        return np.mean(embeddings, axis=1)  # Mean pooling of token embeddings

