# Training Mode

`Chatbot` instances created using the OrionBot library come with training mode enabled by default. Training mode is a feature that allows users to provide feedback to the chatbot whenever it responds with a default "no response message". In this mode, the chatbot will prompt the user to provide an appropriate response to their input if it failed to provide a relevant response. This response is then added to the training data, allowing the chatbot to learn and improve its responses over time.

## Enabling and Disabling Training Mode

To disable training mode, simply call the `disable_training` method on the `Chatbot` instance:

```python
bot = Chatbot('my_bot')
bot.disable_training()
```

To enable training mode, call the `enable_training` method on the `Chatbot` instance:

```python
bot = Chatbot('my_bot')
bot.enable_training()
```

## Examples

Here are some examples of how to enable and disable training mode:

```python
bot = Chatbot('my_bot')
bot.disable_training()  # disables training mode
bot.enable_training()  # enables training mode
```

It's important to note that training mode is enabled by default, so there's no need to call `enable_training` unless it was previously disabled.

## Table of Contents
 
 - [Overview](README.md)
 - [Training Guide](TRAINING.md)
 - [The Chatbot class](CHATBOTCLASS.md)
 - [Preprocessing Method](PREPROCESSING.md)
 - [Training Method](TRAINMETHOD.md)
 - [Train from an existing dataset](DATASETTRAINING.md)
 - [Training Mode](TRAININGMODE.md)
 - ["No Response Message"](NORESPONSE.md)