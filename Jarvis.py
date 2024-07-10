import pyttsx3

def convert_text_to_speech(text, voice_id=0):
    engine = pyttsx3.init()
    engine.setProperty("voice", engine.getProperty("voices")[voice_id].id)
    engine.setProperty("rate", 150) # adjust the speech rate to make it sound more natural
    engine.say(text)
    engine.runAndWait()

# Continuously take input from the user until they type "exit"
while True:
    text = input("Enter the text you want to convert to speech (type 'exit' to quit): ")
    if text.lower() == "exit":
        break
    else:
        # Now, let's add more realistic feelings to the voice output
        def add_feelings(text, feeling):
            # You can add more feeling options as needed
            feeling_dict = {
                "happy": "I'm so happy to hear that!",
                "sad": "I'm sorry to hear that.",
                "excited": "Sounds Good!"
                           " Wish you many many happy returns of the day, Akash!"
                    
                           " i have little suprise for you, do you  open up my lid: suprice is waiting for you:",
                "Hopefull": "here i have a relaxing song for you:"
                           "You definately like it "
                           "liten"
                           "Love you Zindgi"



            }
            return text + " " + feeling_dict[feeling]

        feeling = input("Enter a feeling to add to the text: ")
        text = add_feelings(text, feeling)

        # Convert the text to speech with the added feeling
        convert_text_to_speech(text)