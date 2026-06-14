from __future__ import annotations

from functools import lru_cache
from importlib.resources import files
import hashlib

from .errors import WordIndexError, WordNotFoundError, WordlistValidationError

WORDLIST_FILENAME = "pqc_wordlist.txt"

WORD_COUNT = 4096
BITS_PER_WORD = 12
MIN_INDEX = 0
MAX_INDEX = 4095

MNEMONIC_ENTROPY_BITS = 384
MNEMONIC_CHECKSUM_BITS = 12
MNEMONIC_TOTAL_BITS = 396
MNEMONIC_WORDS = 33

SIGNATURE_STANDARD = "ML-DSA-65"
KDF_STANDARD = "Argon2id"
PRIMARY_HASH = "SHA3-512"


@lru_cache(maxsize=1)
def words() -> tuple[str, ...]:
    text = (
        files("pqc_wordlist")
        .joinpath(WORDLIST_FILENAME)
        .read_text(encoding="utf-8")
    )

    return tuple(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )


@lru_cache(maxsize=1)
def _index_map() -> dict[str, int]:
    return {word: index for index, word in enumerate(words())}


def word_at(index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("index must be int")

    if index < MIN_INDEX or index > MAX_INDEX:
        raise WordIndexError(f"index must be between {MIN_INDEX} and {MAX_INDEX}")

    return words()[index]


def index_of(word: str) -> int:
    if not isinstance(word, str):
        raise TypeError("word must be str")

    normalized = word.strip().lower()

    try:
        return _index_map()[normalized]
    except KeyError:
        raise WordNotFoundError(f"word not found in PQC wordlist: {word}") from None


def contains(word: str) -> bool:
    if not isinstance(word, str):
        return False

    return word.strip().lower() in _index_map()


def _canonical_bytes() -> bytes:
    return ("\n".join(words()) + "\n").encode("utf-8")


def sha3_512() -> str:
    return hashlib.sha3_512(_canonical_bytes()).hexdigest()


def validate_wordlist() -> bool:
    ws = words()

    if len(ws) != WORD_COUNT:
        raise WordlistValidationError(
            f"word count is {len(ws)}, expected {WORD_COUNT}"
        )

    if len(set(ws)) != WORD_COUNT:
        raise WordlistValidationError("duplicate words found")

    if list(ws) != sorted(ws):
        raise WordlistValidationError("wordlist is not alphabetically sorted")

    for index, word in enumerate(ws):
        if word != word.lower():
            raise WordlistValidationError(
                f"word at index {index} is not lowercase: {word}"
            )

        if not word.isalpha():
            raise WordlistValidationError(
                f"word at index {index} is not alphabetic: {word}"
            )

    return True


def metadata() -> dict[str, object]:
    return {
        "name": "PQC English Wordlist Standard",
        "version": "1.0.0",
        "words": WORD_COUNT,
        "bits_per_word": BITS_PER_WORD,
        "indexing": "zero-based",
        "index_range": [MIN_INDEX, MAX_INDEX],
        "mnemonic_entropy_bits": MNEMONIC_ENTROPY_BITS,
        "mnemonic_checksum_bits": MNEMONIC_CHECKSUM_BITS,
        "mnemonic_total_bits": MNEMONIC_TOTAL_BITS,
        "mnemonic_words": MNEMONIC_WORDS,
        "signature_standard": SIGNATURE_STANDARD,
        "kdf_standard": KDF_STANDARD,
        "primary_hash": PRIMARY_HASH,
        "sha3_512": sha3_512(),
    }