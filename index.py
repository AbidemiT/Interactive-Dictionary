import json
import difflib
from difflib import get_close_matches

fileName = "data.json" # The Json file where the datas are stored.

data = json.load(open(fileName))

print("Welcome to Abit Universal Dictionary")
word = input("Search for an English Word: ").lower()

def search(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        for i in get_close_matches(w, data.keys(), cutoff=0.8):
            print("Answer yes or no")
            status = input("Do you mean " + i + " ? ").lower()
            if status == "yes":
                return data[i]
            else:
                return "Oops crosscheck entered word again"
    else:
        return w + " not found, kindly crosscheck word again..."

output = search(word)
if type(output) == list:
    for i in output:
        print(i)
