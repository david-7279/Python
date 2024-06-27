# O que é madlibs? Madlibs é um jogo onde você insere palavras em branco em uma história e depois lê a história com as palavras que você escolheu.
# What is madlibs? Madlibs is a game where you insert blank words into a story and then read the story with the words you chose.

# youtuber = "David" # String variable
# print("Subscribe to " + youtuber) # Concatenation of string and variable
# print("Subscribe to {}".format(youtuber)) # Using format method
# print(f"Subscribe to {youtuber}") # Using f-string

adj = input("Adjective: ")
verb1 = input("First verb: ")
verb2 = input("Second verb: ")
famousPerson = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time \
I love to {verb1}. Stay hydrated and {verb2} like your are {famousPerson}!"

print(madlib)