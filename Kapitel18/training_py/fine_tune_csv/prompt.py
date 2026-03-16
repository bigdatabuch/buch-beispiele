from transformers import pipeline

# Pipeline laden
pipe = pipeline("text-generation", model="./qa-model", tokenizer="distilgpt2")

# Generieren
result = pipe("Q: Who originally developed Hadoop? A:", max_length=30)
print(result[0]['generated_text'])