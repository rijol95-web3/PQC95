import pytest

from pqc_wordlist import (
    WORD_COUNT,
    BITS_PER_WORD,
    MIN_INDEX,
    MAX_INDEX,
    MNEMONIC_WORDS,
    words,
    word_at,
    index_of,
    contains,
    validate_wordlist,
    sha3_512,
    metadata,
    WordIndexError,
    WordNotFoundError,
)


def test_constants():
    assert WORD_COUNT == 4096
    assert BITS_PER_WORD == 12
    assert MIN_INDEX == 0
    assert MAX_INDEX == 4095
    assert MNEMONIC_WORDS == 33


def test_words_count():
    assert len(words()) == 4096


def test_validate_wordlist():
    assert validate_wordlist() is True


def test_word_at():
    assert word_at(0) == words()[0]
    assert word_at(4095) == words()[4095]


def test_index_of():
    assert index_of(words()[0]) == 0
    assert index_of(words()[4095]) == 4095


def test_contains():
    assert contains(words()[0]) is True
    assert contains("notawordinpqcwordlist") is False


def test_invalid_index():
    with pytest.raises(WordIndexError):
        word_at(-1)

    with pytest.raises(WordIndexError):
        word_at(4096)


def test_missing_word():
    with pytest.raises(WordNotFoundError):
        index_of("notawordinpqcwordlist")


def test_sha3_512():
    h = sha3_512()
    assert isinstance(h, str)
    assert len(h) == 128


def test_metadata():
    m = metadata()

    assert m["words"] == 4096
    assert m["bits_per_word"] == 12
    assert m["mnemonic_words"] == 33
    assert m["signature_standard"] == "ML-DSA-65"
    assert m["kdf_standard"] == "Argon2id"
    assert m["primary_hash"] == "SHA3-512"
    assert len(m["sha3_512"]) == 128