import spacy
from bertopic import BERTopic

nlp = spacy.load("en_core_web_sm")
topic_model = BERTopic(verbose=True)

def enrich_chunks(chunks: list[str]) -> list[dict]:
    """Add NER and topics to text chunks"""
    topics, _ = topic_model.fit_transform(chunks)
    
    enriched = []
    for chunk, topic in zip(chunks, topics):
        doc = nlp(chunk)
        ents = [(ent.text, ent.label_) for ent in doc.ents]  # Fixed ent.label_
        enriched.append({
            'text': chunk,
            'entities': ents,
            'topic': int(topic)  # Convert to Python int
        })
    
    return enriched