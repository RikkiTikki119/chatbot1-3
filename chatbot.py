# chatbot1-3



def check_for_greeting(sentence):
    import random
    word=input("You greeting:")
    KEYWORDS = ("hello", "hi", "greetings", "yo", "what's up",)
    GREETINGS = ["hello ol' sport", "hey", "*hand shake*", "hey, did you receive my letter?"]

    if word.lower() in KEYWORDS:
        return(random.choice(GREETINGS))


def mornings():
    computerfavcereal= "Honey nut bolts"

    favcereal = input("What is your favorite cereal?: ")
    print(favcereal + '...is a very nice cereal choice. So...what is your name ol sport?')
        name=input()
    print('What?!?!?!?!:  ' + name + ' That is my name!!!, Want to know something funny?...my favorite cereal is:' ,computerfavcereal )

mornings()
input("\n\nPress enter to exit")

def tfunct():
