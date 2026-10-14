from CODE.Word_Frequency import word_frequency


def test_word_frequency():
    assert word_frequency("python is easy python is powerful") == {
        "python": 2,
        "is": 2,
        "easy": 1,
        "powerful": 1
    }


def test_uppercase_words():
    assert word_frequency("Hello hello") == {"hello": 2}


def test_empty_sentence():
    assert word_frequency("") == {}


def test_single_word():
    assert word_frequency("python") == {"python": 1}


def test_repeated_words():
    assert word_frequency("apple apple apple") == {"apple": 3}
