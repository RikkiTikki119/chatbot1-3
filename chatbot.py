# chatbot1-3




def check_for_greeting(sentence):
#ricardo______
    import random
    word=input("You greeting:")
    KEYWORDS = ("hello", "hi", "greetings", "yo", "what's up",)
    GREETINGS = ["hello ol' sport", "hey", "*hand shake*", "hey, did you receive my letter?"]

    if word.lower() in KEYWORDS:
        return(random.choice(GREETINGS))

def mornings():
#brandon______
print('Hello this is your computer speaking...we are wondering what our master eats for nutrients?')
    import random
    word=input("Whats your favorite cereal?:")
    KEYWORDS = (word)
    GREETINGS = ["Really?", "That is good...", "Yummy!", "I cant even eat cereal or else my systems will fail."]

    if word.lower() in KEYWORDS:
        return(random.choice(GREETINGS))

mornings()
#___________
input("\n\nPress enter to exit")
