#  Chatbot using Hugging Face Transformers

This project is a simple console-based chatbot built using Hugging Face Transformers. The chatbot can understand user questions and generate meaningful responses using a pre-trained NLP model.

The main objective of this project is to build an interactive chatbot that accepts user input, processes it using a transformer model, and returns accurate answers while maintaining a continuous conversation flow.

This chatbot is developed using Python, Hugging Face Transformers, and PyTorch in a Jupyter Notebook / Google Colab environment. The model used in this project is `distilbert-base-cased-distilled-squad`, which is a question-answering transformer model.

The chatbot supports:
- Interactive conversation
- Multiple user queries
- Greeting handling (Hello, Hi, etc.)
- Exit commands (exit, quit)
- Accurate answers for general questions

The working flow of the chatbot is simple: the user enters a question, the model processes the input, generates a response, and displays the output. This loop continues until the user exits.

### Sample Interaction

You: Hello  
Chatbot: Hello! How can I help you today?  

You: What is Artificial Intelligence?  
Chatbot: the simulation of human intelligence in machines  

You: Who created Python?  
Chatbot: Guido van Rossum  

You: exit  
Chatbot: Goodbye!  

### How to Run

1. Install required libraries:
   pip install transformers torch  

2. Open and run the notebook:
   chatbot_transformers.ipynb  

3. Start chatting with the chatbot

This project demonstrates how transformer-based NLP models can be used to build simple and effective conversational AI systems.

Thanks to Innomatics Research Labs for providing this learning opportunity.

#NLP #AI #DataScience #MachineLearning
