from transformers import DistilBertTokenizer, DistilBertModel
import torch
import numpy as np

_tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
_model = DistilBertModel.from_pretrained('distilbert-base-uncased') 
_model.eval()

_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
_model.to(_device)

def get_title_embedding(text: str) -> np.ndarray:
    inputs = _tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=64)
    inputs = {key: val.to(_device) for key, val in inputs.items()}
    
    with torch.no_grad():
        outputs = _model(**inputs)
    
    # Use the mean of the last hidden state as the embedding
    cls_embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy().flatten()

    return cls_embeddings