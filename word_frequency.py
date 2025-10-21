#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if len(sentence) > 0 and sentence[0].isupper() and sentence[-1] in ".?!":
            return sentence
        print("Invalid sentence. It must start with a capital letter and end with a period, question mark, or exclamation mark.")

def calculate_frequencies(sentence):
    words = sentence[:-1].lower().split()
    unique_words = []
    frequencies = []
    for word in words:
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)
    return unique_words, frequencies

def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

if __name__ == "__main__":
    main()

    return True
