# Preprocessing

OrionBot provides a powerful preprocessing functionality to convert raw input text into a normalized format that can be used for training and generating responses. This functionality is implemented in the `_preprocess` method of the `Chatbot` class, and uses the Natural Language Toolkit (NLTK) library.

## Preprocessing Steps

The `_preprocess` method of the `Chatbot` class implements the following preprocessing steps:

1.  Tokenization: The raw input text is tokenized into individual words using the `word_tokenize` function from NLTK.
    
2.  Case Normalization: All the tokens are converted to lowercase.
    
3.  Stopword Removal: Stopwords, which are common words that don't carry much meaning (e.g. "the", "a", "and"), are removed from the token list using a list of stopwords provided by NLTK.
    
4.  Lemmatization: The remaining words are lemmatized using the WordNetLemmatizer from NLTK. Lemmatization reduces each word to its base form (e.g. "running" to "run"), which helps to group similar words together.
    
5.  Vectorization: Finally, the preprocessed text is returned as a string of space-separated tokens, which can be used for training and generating responses.
    

## Usage

To use the preprocessing functionality in OrionBot, you can call the `_preprocess` method of a `Chatbot` instance with the raw input text as a parameter. Here's an example:

```python
from orionbot import Chatbot

# Create a Chatbot instance
bot = Chatbot('MyBot')

# Preprocess an input text
preprocessed_text = bot._preprocess("Hello, how are you doing today?")
print(preprocessed_text)
# Output: hello today
```

In this example, the input text "Hello, how are you doing today?" is preprocessed using the `_preprocess` method of the `bot` instance. The resulting preprocessed text is "hello today".

Note that the preprocessing functionality is used internally by OrionBot for both training and generating responses, so you don't need to call this method directly in most cases. However, if you need to preprocess input text for some other purpose, you can use this method to do so.

## Parameters

The `_preprocess` method of the `Chatbot` class takes one parameter:

-   `text` (str): The raw input text to preprocess.

## Returns

The `_preprocess` method of the `Chatbot` class returns a string of space-separated tokens that represent the preprocessed text.

## Table of Contents
 
 - [Overview](README.md)
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)