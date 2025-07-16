import random
import re
from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk import download

try:
    download('punkt')
    download('wordnet')
except:
    pass

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.sysnets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace('_', ' ')
            if synonym.lower() != word.lower():
                synonyms.add(synonym)
    return list(synonyms)

def recommend_title_variations(title: str, n=5):
    tokens = word_tokenize(title)
    recommendations = set()

    for _ in range(n*2):
        new_title = []
        for word in tokens:
            if re.match(r'\w{4,}', word) and random.random() < 0.4:
                syns = get_synonyms(word)
                new_word = random.choice(syns) if syns else word
                new_title.append(new_word)
            else:
                new_title.append(word)
        recommendations.add(' '.join(new_title))
        if len(recommendations) >= n:
            break
    return list(recommendations)[:n]
    