from webbrowser import get
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(0,len(prepositions)):
        preposition = get_preposition()
    assert preposition in prepositions


pytest.main(["-v", "--tb=line", "-rN", __file__])
