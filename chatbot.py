
# chatbot1-3


import random



def check_for_greeting(sentence):
#ricardo______
    import random
    word=input("You greeting:")
    KEYWORDS = ("hello", "hi", "greetings", "yo", "what's up",)
    GREETINGS = ["hello ol' sport", "hey", "*hand shake*", "hey, did you receive my letter?"]

    if word.lower() in KEYWORDS:
        return(random.choice(GREETINGS))

check_for_greeting()

def mornings():
    def mornings():
    words=input("Whats your favorite cereal?:")
    bfast = (words)
    repo = ["Really?", "That is good...", "Yummy!", "I cant even eat cereal or else my systems will fail."]

    if words.lower() in bfast:
        return(random.choice(repo))

mornings()


def tfunct():
    word=input("You Goodbye:")
KEYWORDS = ("bye bye", "bye")
ByeWords = ["Have a good day!", "Powering down", "HaveANiceTime"]

if word.lower() in KEYWORDS:
    print(random.choice(Byewords))
    
tfunct()

input("\n\nPress enter to exit")
