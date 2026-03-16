import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)

# CSV Daten laden und vorbereiten
df = pd.read_csv("qa_dataset.csv")
df['text'] = "Q: " + df['question'] + " A: " + df['answer']
dataset = Dataset.from_pandas(df[['text']])

print(df)

# Tokenizer und Modell
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Tokenisieren
def tokenize(examples):
    return tokenizer(examples['text'], truncation=True, padding=True, max_length=64)
tokenized = dataset.map(tokenize, batched=True)

# Training
trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    args=TrainingArguments(
        output_dir="./output",
        num_train_epochs=50,  # Mehr Epochen bei wenig Daten
        per_device_train_batch_size=2,  # Klein bei wenig Daten
        save_strategy="no",
        logging_steps=10,
        no_cuda=True, # CPU Mode
    ),
    train_dataset=tokenized,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

trainer.train()
trainer.save_model("./qa-model")