"""EXO7 - Testing Dictionary Functions."""
__author__ = "730576293"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_dict() -> None:
    """Tests empty dict input."""
    test_dict = dict()
    assert invert(test_dict) == {}
    

def test_1_entry() -> None:
    """Tests inversion with entry dict with just 1 key/value pair."""
    test_dict: dict = {"beans": "green"}
    assert invert(test_dict) == {"green": "beans"}


def test_number_entries() -> None:
    """Tests inversion with entry dict with some str number values."""
    test_dict: dict = {"beans": "30", "tomatoes": "10", "potatoes": "none"}
    assert invert(test_dict) == {"30": "beans", "10": "tomatoes", "none": "potatoes"}


def test_return_order() -> None:
    """Tests a return of the first highest favorite color when tied."""
    test_dict: dict = {"Marc": "yellow", "Kevin": "red", "Ezri": "blue", "Kris": "blue", "Jake": "red"}
    assert favorite_color(test_dict) == "red"


def test_empty_dict1() -> None:
    """Tests empty dict input, should return empty list."""
    test_dict = dict()
    assert favorite_color(test_dict) == ""


def test_capitalization() -> None:
    """Tests the effects of captalization of a value; should be counted differently."""
    test_dict: dict = {"Marc": "yellow", "Kevin": "Red", "Ezri": "blue", "Kris": "blue", "Jake": "red"}
    assert favorite_color(test_dict) == "blue"


def test_empty_list() -> None:
    """Tests empty dict input, should return empty dict."""
    test_list = list()
    assert count(test_list) == {}


def test_updating_properly() -> None:
    """Tests that new entries start at 1 and update properly."""
    test_list: list[str] = ["apple", "banana", "banana", "carrot", "carrot", "carrot"]
    assert count(test_list) == {"apple": 1, "banana": 2, "carrot": 3}


def test_number_entries2() -> None:
    """Tests count with entry list with some str number values."""
    test_list: list[str] = ["4", "3", "7", "3", "3", "7"]
    assert count(test_list) == {"4": 1, "3": 3, "7": 2}