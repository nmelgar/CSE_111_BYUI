from webbrowser import get
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_prepositional_phrase():
    # phrase_singular = get_prepositional_phrase(1)
    # phrase_plural = get_prepositional_phrase(2)

    # split_phrase = phrase_singular.split()
    # preposition_1 = split_phrase[0]
    # determiner = split_phrase[1]
    # noun = split_phrase[2]
    # return (f"hello {preposition}, {determiner}, {noun} ")
    # return (f"hello , {phrase_singular}")

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(0, len(prepositions)):
        preposition = get_preposition()
    assert preposition in prepositions

    determiners = ["a", "one", "some", "many", "the"]
    for _ in range(0, len(determiners)):
        determiner = get_determiner(1)
    assert determiner in determiners

    nouns = ["bird", "boy", "car", "cat", "child",
             "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
             "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(0, len(nouns)):
        noun = get_noun(1)
    assert noun in nouns


# print(test_get_prepositional_phrase())
pytest.main(["-v", "--tb=line", "-rN", __file__])
