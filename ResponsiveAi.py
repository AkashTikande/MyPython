
# To test someone's response towards same query ask repeatedly by a programme  #
# Additionally take response from google assistant feature directly #
# realtime responser like heyy google or heyy siri #
import random

class AI:
    def __init__(self):
        self.responses = ["Hello!", "How can I help you?", "What would you like to do?","Do you Still remember what you prommis for","How "]
           # Edit your response in self.response #                                                                                                                          "Do you Enjoying Your lone time"] # default algorithem.

    def respond(self, text):
        response = random.choice(self.responses)
        return response

ai = AI()

while True:
    text = input("You: ")
    response = ai.respond(text)
    print("AI: " + response)