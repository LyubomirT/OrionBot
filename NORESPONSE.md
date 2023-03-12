
# Setting the "No Response" message

The `set_no_response_message()` method allows you to customize the default message that the `Chatbot` object returns when it is unable to find a suitable response. By default, the message is "I'm sorry, I did not understand what you just said. What should I have said?"

## Syntax
```python
chatbot.set_no_response_message(message)
```

## Parameters

-   `message` (str): the custom message to be set as the new "No Response" message.

## Example

```python
from orionbot import Chatbot

chatbot = Chatbot("My Chatbot")
chatbot.set_no_response_message("I'm not sure what you mean. Can you please rephrase your question?")

# Now, if the chatbot cannot find a suitable response, it will return the custom message instead of the default one
print(chatbot.get_response("What is the weather like today?"))
# Output: "I'm not sure what you mean. Can you please rephrase your question?"
```

Note that you can set any message you like as the "No Response" message. This can be useful if you want to provide a more personalized experience to your users or if you want to guide them to ask more specific questions.

## Table of Contents
 
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)