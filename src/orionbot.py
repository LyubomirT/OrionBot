import json
import os.path
from collections import defaultdict
import os

import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')
nltk.download("stopwords")

import platform
systemPlatform = platform.system()

if systemPlatform == "Windows":
    os.system("cls")
if systemPlatform == "Linux":
    os.system("clear")

class Chatbot:
    def __init__(self, name, lemmatizer=None, stopwords=None, data_file=None):
        self.name = name
        self.lemmatizer = lemmatizer or WordNetLemmatizer()
        self.stopwords = stopwords or set(nltk.corpus.stopwords.words('english'))
        self.data_file = data_file or 'training_data_qbot.json'
        self.training_data = defaultdict(list)
        self.vectorizer = TfidfVectorizer()
        self.similarity_threshold = 0.5
        self.training_enabled = True
        self.no_response_message = "I'm sorry, I did not understand what you just said. What should I have said?"

        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.training_data.update(json.load(f))
                if self.training_data:
                    self.vectorizer.fit_transform(list(self.training_data.keys()))
                else:
                    print("The chatbot was not yet trained!")

    def _preprocess(self, text):
        words = nltk.word_tokenize(text.lower())
        words = [self.lemmatizer.lemmatize(w) for w in words if w not in self.stopwords]
        return ' '.join(words)

    def train(self, input_text, response_text):
        if self.training_enabled:
            input_text = self._preprocess(input_text)
            self.training_data[input_text].append(response_text)

            with open(self.data_file, 'w') as f:
                json.dump(self.training_data, f)

            try:
                self.vectorizer.fit_transform(list(self.training_data.keys()))
            except ValueError as e:
                print("The chatbot was not yet trained!")

    def _get_response(self, input_text):
        if not self.vectorizer.vocabulary_:
            raise ValueError("The chatbot was not yet trained!")

        input_text = self._preprocess(input_text)
        input_vector = self.vectorizer.transform([input_text])
        similarities = cosine_similarity(input_vector, self.vectorizer.transform(list(self.training_data.keys())))[0]
        closest_match_idx = similarities.argmax()
        closest_match_score = similarities[closest_match_idx]

        if closest_match_score >= self.similarity_threshold:
            responses = self.training_data[list(self.training_data.keys())[closest_match_idx]]
            return responses[0]
        else:
            return self.no_response_message

    def get_response(self, input_text):
        response = None

        try:
            response = self._get_response(input_text)
        except ValueError as e:
            print("The chatbot was not yet trained!")
            response = self.no_response_message

        if response == self.no_response_message and self.training_enabled:
            new_response = input(f"{self.no_response_message} ")
            if new_response:
                self.train(input_text, new_response)
                response = f"Got it! I should have said '{new_response}'."
            else:
                response = "Okay, I'll keep that in mind."

        return response

    def enable_training(self):
        self.training_enabled = True

    def disable_training(self):
        self.training_enabled = False

    def set_no_response_message(self, message):
        self.no_response_message = message

    def train_from_file(self, file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        for input_text, response_list in existing_data.items():
            for response_text in response_list:
                self.train(input_text, response_text)

    def train_from_default_file(self):
        self.train_from_file(self.data_file)