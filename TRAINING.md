# Training the Chatbot

The `Chatbot` class in OrionBot has a built-in training mechanism that allows you to add new training data to the chatbot and improve its accuracy over time. In this document, we'll go over the various ways you can train your chatbot.

## Adding Training Data

To add training data to the chatbot, you can use the `train` method. This method takes in two parameters: `input_text` and `response_text`. `input_text` is the text that the user inputs, and `response_text` is the response that the chatbot should give in return. Here's an example:

```python
bot = Chatbot("my_bot")
bot.train("Hello", "Hi there!")
```
This will add the training data "Hello" and "Hi there!" to the chatbot. The `train` method automatically preprocesses the text by tokenizing it, lemmatizing it, and removing stop words. The preprocessed text is then added to the chatbot's training data.

## Training from File

If you have a large amount of training data that you'd like to add to the chatbot, you can use the `train_from_file` method. This method takes in a file path to a JSON file containing training data in the following format:

```json
{
    "input_text_1": ["response_text_1", "response_text_2", ...],
    "input_text_2": ["response_text_1", "response_text_2", ...],
    ...
}
```

Here's an example of how to use `train_from_file`:
```python
bot = Chatbot("my_bot")
bot.train_from_file("training_data.json")
```

This will add all of the training data in the `training_data.json` file to the chatbot.

## Disabling Training

By default, the chatbot's training mode is enabled, which means that if it doesn't know how to respond to a user's input, it will ask the user for a response and add that to its training data. However, if you'd like to disable training mode, you can use the `disable_training` method:

```python
bot = Chatbot("my_bot")
bot.disable_training()
```

Now, if the chatbot doesn't know how to respond to a user's input, it will simply return a default "I'm sorry, I did not understand what you just said" message.

## Enabling Training

If you've disabled training mode and would like to re-enable it, you can use the `enable_training` method:

```python
bot = Chatbot("my_bot")
bot.enable_training()
```

Now, if the chatbot doesn't know how to respond to a user's input, it will ask the user for a response and add that to its training data.

## Customizing the "No Response" Message

By default, if the chatbot doesn't know how to respond to a user's input and training mode is enabled, it will prompt the user for a response. If the user doesn't provide a response, the chatbot will return a default "Okay, I'll keep that in mind" message. However, you can customize this message by using the `set_no_response_message` method:

```python
bot = Chatbot("my_bot")
bot.set_no_response_message("I'm sorry, I still don't understand. Could you please try rephrasing your question?")
```

Now, if the chatbot doesn't know how to respond to a user's input, it will send the message you specified.

## Table of Contents
 
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)