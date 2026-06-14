class PQCWordlistError(Exception):
    """Base exception for pqc-wordlist."""


class WordlistValidationError(PQCWordlistError):
    """Raised when the PQC wordlist is invalid."""


class WordNotFoundError(PQCWordlistError):
    """Raised when a word does not exist in the PQC wordlist."""


class WordIndexError(PQCWordlistError):
    """Raised when a word index is outside the valid range."""