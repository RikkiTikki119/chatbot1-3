
def check_for_greeting(sentence):
#ricardo______
    import random
    word=input("You greeting:")
    KEYWORDS = ("hello", "hi", "greetings", "yo", "what's up",)
    GREETINGS = ["hello ol' sport", "hey", "*hand shake*", "hey, did you receive my letter?"]

    if word.lower() in KEYWORDS:
        return(random.choice(GREETINGS))

# chatbot1-3



def mornings():
    import random
    words=input("Whats your favorite cereal?:")
    bfast = (words)
    respo = ["Really?", "That is good...", "Yummy!", "I cant even eat cereal or else my systems will fail."]

    if words.lower() in bfast:
        return(random.choice(respo))


mornings()

