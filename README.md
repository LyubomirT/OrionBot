# OrionBot: A Python bot training framework
OrionBot is a Python library that allows you to easily train and run chatbots, fully customizable.

## Installation
To install OrionBot, simply use pip:
```bash
pip install orionbot
```

## Usage

To use OrionBot, simply import the `Chatbot` class and create a new instance with a name:
```python
from orionbot import Chatbot
bot = Chatbot("My Bot")
```

### Training
You can train your bot by calling the `train` method with an input text and a response text:

```python
bot.train("Hi", "Hello there!")
```

You can also train your bot from a file:
```python
bot.train_from_file("training_data.json")
```

Or, you can train your bot from the default file:
```python
bot.train_from_default_file()
```

### Getting Responses
To get a response from your bot, simply call the `get_response` method with an input text:
```python
response = bot.get_response("Hi")
print(response)  # "Hello there!"
```

If your bot does not understand the input text, it will return a default response. You can set this response by calling the `set_no_response_message` method:

```python
bot.set_no_response_message("I'm sorry, I didn't understand that.")
```

### Training Toggle

You can enable or disable training by calling the `enable_training` or `disable_training` methods:

```python
bot.enable_training()
bot.disable_training()
```

## Examples

Here are some examples of how to use OrionBot:

### Example 1: Simple greeting bot
```python
from orionbot import Chatbot

bot = Chatbot("Greeting Bot")

bot.train("Hi", "Hello there!")
bot.train("Hello", "Hi there!")
bot.train("Hey", "Hiya!")

print(bot.get_response("Hi"))  # "Hello there!"
print(bot.get_response("Hey"))  # "Hiya!"
print(bot.get_response("What's up?"))  # "I'm sorry, I didn't understand that."
```
### Example 2: Movie recommendation bot
```python
from orionbot import Chatbot

bot = Chatbot("Movie Bot")

bot.train("What's a good movie to watch?", "I recommend watching The Shawshank Redemption.")
bot.train("What's your favorite movie?", "My favorite movie is The Godfather.")
bot.train("Have you seen Inception?", "Yes, Inception is a great movie!")

print(bot.get_response("What's a good movie to watch?"))  # "I recommend watching The Shawshank Redemption."
print(bot.get_response("What's your favorite movie?"))  # "My favorite movie is The Godfather."
print(bot.get_response("Have you seen The Matrix?"))  # "I'm sorry, I didn't understand that."
```

 You can find more information on our [GitHub repository](https://github.com/LyubomirT/OrionBot)
