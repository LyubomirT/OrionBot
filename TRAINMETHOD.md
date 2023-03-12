
# OrionBot - Train Method

The `train` method of the `Chatbot` class is used to train the chatbot on new input and response pairs. Here's how you can use it:
```python
my_bot = Chatbot(name="MyBot")
my_bot.train("Hello", "Hi there!")
```

## Parameters

The `train` method takes two parameters:

-   `input_text`: The input text to train the chatbot on. This can be any string.
-   `response_text`: The response text to associate with the input text. This can also be any string.

## Example

Here's an example of how to use the `train` method to train the chatbot on multiple input and response pairs:

```python
my_bot = Chatbot(name="MyBot")

my_bot.train("Hello", "Hi there!")
my_bot.train("How are you?", "I'm doing well, thanks for asking.")
my_bot.train("What's your name?", "My name is MyBot.")
```

In the example above, we create a new `Chatbot` instance called `my_bot` and then train it on three different input and response pairs.

## Notes

-   The `train` method adds the input and response pair to the training data, which is stored in a JSON file.
-   The JSON file is automatically loaded when the `Chatbot` instance is created, so any previously trained input and response pairs will be available for the chatbot to use.
-   The `train` method also updates the `TfidfVectorizer` object used by the chatbot to vectorize the input text. This ensures that any new words in the training data are accounted for when generating response vectors.
-   If you want to train the chatbot on a large dataset, you can use the `train_from_file` method to read input and response pairs from a JSON file.


## Table of Contents
 
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)