import spacy

# Tải mô hình ngôn ngữ tiếng Việt
nlp = spacy.load('xx_ent_wiki_sm')

def analyze_question(question):
    doc = nlp(question)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities