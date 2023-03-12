
# Training from Existing Dataset

`train_from_file(file_path)` and `train_from_default_file()` methods in `Chatbot` class are designed to help you train your chatbot using an existing dataset. You can pass the path of the file containing the dataset or use the default file path `training_data_qbot.json` that comes with the package.

## Parameters

-   `file_path`: A string that specifies the path of the file containing the training data. (Optional)
-   No parameters needed for `train_from_default_file()` method.

## Usage

```python
from orionbot import Chatbot

# Create a Chatbot object
bot = Chatbot("My Bot")

# Train the chatbot from a file
bot.train_from_file("path/to/training_data.json")

# Train the chatbot from the default file
bot.train_from_default_file()
```

## Details

-   `train_from_file(file_path)` method reads the training data from a JSON file, specified by `file_path` parameter, and trains the chatbot with it. The file should be a dictionary with input texts as keys and response texts as values. The method loops over each input-output pair and calls `train()` method to train the chatbot with each pair.
-   `train_from_default_file()` method reads the training data from the default file path `training_data_qbot.json` and trains the chatbot with it. This method is a shorthand for `train_from_file()` method where `file_path` parameter is set to the default file path.

## Example

Let's say you have a JSON file named `training_data.json` that contains the following training data:

```python
{
  "hello": ["Hi there!", "Hello!", "Hey!"],
  "how are you": ["I'm doing great!", "I'm fine, thank you!", "I'm doing well."],
  "what is your name": ["My name is MyBot.", "I'm MyBot.", "You can call me MyBot."]
}
```

You can train your chatbot using this dataset by calling the `train_from_file()` method like this:

```python
from orionbot import Chatbot

# Create a Chatbot object
bot = Chatbot("My Bot")

# Train the chatbot from the file
bot.train_from_file("training_data.json")
```

This will train the chatbot with the input-output pairs in the `training_data.json` file. You can also use the default file path by calling the `train_from_default_file()` method like this:

```python
from orionbot import Chatbot

# Create a Chatbot object
bot = Chatbot("My Bot")

# Train the chatbot from the default file
bot.train_from_default_file()
```
This will train the chatbot with the input-output pairs in the default `training_data_qbot.json` file.

## Table of Contents
 
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)