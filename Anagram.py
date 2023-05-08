import itertools
import nltk

nltk.download("words")
from nltk.corpus import words

correct_words = words.words()


def generate_anagrams(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Generate all possible permutations of the letters in the word
    permutations = itertools.permutations(word)

    # Convert each permutation to a string and check if it's an anagram
    anagrams = set()
    for permutation in permutations:
        permutation_str = "".join(permutation)
        if (
            permutation_str != word
            and is_anagram(permutation_str, word)
            and permutation_str in correct_words
        ):
            anagrams.add(permutation_str)

    return anagrams


def is_anagram(str1, str2):
    # Convert strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


# Example usage
anagrams = generate_anagrams("earth")
print(anagrams)


