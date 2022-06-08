from webbrowser import get
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_prepositional_phrase():
    phrase_singular = get_prepositional_phrase(1)
    phrase_plural = get_prepositional_phrase(2)
    
    split_phrase = phrase_singular.split()
    preposition = split_phrase[0]
    determiner = split_phrase[1]
    noun = split_phrase[2] 
    return (f"{preposition}, {determiner}, {noun} ")
    # return (f"hello , {phrase_singular}")


print(test_get_prepositional_phrase())
