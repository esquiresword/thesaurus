import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return ("Sorry, I don't know this word :(")
        else:
            return "I didn't understand your entry."
    else:
        return "I don't know this word :("

word = input("Enter word that you don't know:")

output = (translate(word))

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)