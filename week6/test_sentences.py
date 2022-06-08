from webbrowser import get
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

quantity_1 = 1
quantity_2 = 2
tense = ["past", "present", "future"]


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1 test single nouns
    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        noun = get_noun(1)
    assert noun in single_nouns

    # 2 test plural nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        noun = get_noun(2)
    assert noun in plural_nouns


def test_get_verb():
    # 1 test past
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1, "past")
    assert verb in past_verbs

    # 2 single present
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")
    assert verb in single_present_verbs

    # 3 plural present
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(2, "present")
    assert verb in plural_present_verbs

    # 4 future
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, "future")
    assert verb in future_verbs


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(0, len(prepositions)):
        preposition = get_preposition()
    assert preposition in prepositions



def test_get_prepositional_phrase():
    """This function will call the get_preposition, get_determiner and 
    get_noun functions to check that they contain certain 
    word while creating the prepositional phrase."""
    
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



pytest.main(["-v", "--tb=line", "-rN", __file__])
