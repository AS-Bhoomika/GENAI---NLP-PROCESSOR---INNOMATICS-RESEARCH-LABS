# Task 5: POS Tagging using DistilBERT

##  Objective
The goal of this task is to fine-tune a Transformer model (DistilBERT) to perform Part-of-Speech (POS) Tagging using token classification techniques.

---

##  Dataset
- Dataset Used: CoNLL-2003  
- Loaded using Hugging Face `datasets` library  
- Contains tokens annotated with POS tags  

---

##  Technologies Used
- Python  
- Hugging Face Transformers  
- Datasets Library  
- PyTorch  
- Google Colab  

---

##  Workflow
1. Load dataset using Hugging Face  
2. Tokenize text using BERT tokenizer  
3. Align labels with tokens (handle subwords)  
4. Load pre-trained DistilBERT model  
5. Train model using Trainer API  
6. Evaluate using seqeval metrics  
7. Perform inference on custom sentence  

---

##  Evaluation Metrics
- Precision  
- Recall  
- F1 Score  

---

##  Inference Example

### Input:
John works at Google in California

### Output:
[('John', 'NNP'), ('works', 'VBZ'), ('at', 'IN'), ('Google', 'NNP'), ('in', 'IN'), ('California', 'NNP')]

---

##  Comparison
- POS Tagging → Word-level tagging  
- Chunking → Phrase-level grouping  

---

##  Challenges Faced
- Token alignment with subwords  
- Handling padding and special tokens (-100)  
- Library version compatibility issues  

---

##  Observations
- Transformer models capture context effectively  
- Model performance improves with more training  
- Even small training gives reasonable results  

---

##  Conclusion
Successfully fine-tuned DistilBERT for POS tagging and understood token classification workflow in NLP.
