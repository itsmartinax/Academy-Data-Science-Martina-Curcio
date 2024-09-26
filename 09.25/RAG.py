from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Carica il tokenizer, il retriever e il modello di generazione
tokenizer=RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever=RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True, trust_remote_code=True)
model=RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

# Testo di input
input_text="Spiega il paradigma di programmazione orientata agli oggetti"

# Tokenizzazione dell'input
input_ids=tokenizer(input_text, return_tensors="pt").input_ids

# Recupero delle informazioni rilevanti
retriever_outputs=retriever(input_ids, return_tensors="pt")

#Generazione della risposta
generated_ids=model.generate(input_ids, context_input_ids=retriever_outputs['context_input_ids'])

# Decodifica della risposta
output_text=tokenizer.batch_decode(generated_ids,skip_special_tokens=True)[0]

print(output_text)