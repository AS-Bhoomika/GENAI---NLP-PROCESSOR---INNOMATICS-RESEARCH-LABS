# GENAI---NLP-PROCESSOR---INNOMATICS-RESEARCH-LABS

This project presents an advanced Natural Language Processing (NLP) preprocessing engine designed to clean and transform raw, unstructured text into meaningful and structured data. It simulates real-world text cleaning pipelines used in modern AI and GenAI applications.

---

## Features

* Removal of URLs, emojis, and unwanted symbols
* Text normalization (lowercasing, punctuation removal)
* Removal of numbers and extra spaces
* Handling repeated characters (e.g., "soooo" → "soo")
* Tokenization for structured output
* Clean and reusable preprocessing pipeline

---

## Technologies Used

* Python
* Regular Expressions (`re`)
* String Processing

---

## Project Structure

```
GENAI---NLP-PROCESSOR---INNOMATICS-RESEARCH-LABS
│
├── task-1.ipynb
├── README.md
```

---

## Sample Input & Output

**Input:**

```
I absolutely looooved this product 😍😍 100%!!! Visit https://abc.com
```

**Output:**

```
['absolutely', 'looved', 'this', 'product', 'visit']
```

---

##  Use Cases

This preprocessing engine can be used in:

* Machine Learning models
* NLP applications
* Sentiment analysis
* Text classification
* Chatbots and GenAI systems

---

## Internship

This project was developed as part of an internship at
**Innomatics Research Labs**

---

##  Author
Bhoomika A S
---
