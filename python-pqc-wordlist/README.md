# PQC Wordlist

Official Python implementation of the PQC Foundation English Wordlist Standard.

The PQC Wordlist Standard defines a deterministic 4096-word English wordlist designed for use in the PQC ecosystem, including mnemonic generation, seed derivation, wallets, and future post-quantum infrastructure.

---

## Features

* 4096 English words
* 12-bit word indices
* Zero-based indexing (0-4095)
* Alphabetically sorted
* Duplicate-free validation
* SHA3-512 integrity hash
* Designed for 33-word PQC mnemonics
* ML-DSA-65 ecosystem compatible
* Argon2id ecosystem compatible

---

## Standard Specification

| Parameter           | Value      |
| ------------------- | ---------- |
| Word Count          | 4096       |
| Bits Per Word       | 12         |
| Indexing            | Zero-based |
| Index Range         | 0-4095     |
| Mnemonic Entropy    | 384 bits   |
| Mnemonic Checksum   | 12 bits    |
| Total Mnemonic Bits | 396 bits   |
| Mnemonic Length     | 33 words   |
| Primary Hash        | SHA3-512   |
| Signature Standard  | ML-DSA-65  |
| KDF Standard        | Argon2id   |

---

## Installation

```bash
pip install pqc-wordlist
```

---

## Quick Start

```python
from pqc_wordlist import words

print(len(words()))
```

Output:

```text
4096
```

---

## Usage

### Load the complete wordlist

```python
from pqc_wordlist import words

all_words = words()

print(len(all_words))
```

---

### Get a word by index

```python
from pqc_wordlist import word_at

print(word_at(0))
print(word_at(4095))
```

---

### Get the index of a word

```python
from pqc_wordlist import index_of

print(index_of("example"))
```

---

### Check whether a word exists

```python
from pqc_wordlist import contains

print(contains("example"))
```

Returns:

```python
True
```

or

```python
False
```

---

### Validate the embedded wordlist

```python
from pqc_wordlist import validate_wordlist

print(validate_wordlist())
```

Output:

```python
True
```

Validation checks:

* Exactly 4096 words
* No duplicate entries
* Alphabetically sorted
* Lowercase only
* Alphabetic characters only

---

### Calculate SHA3-512

```python
from pqc_wordlist import sha3_512

print(sha3_512())
```

Returns:

```text
128-character SHA3-512 hex string
```

---

### Get metadata

```python
from pqc_wordlist import metadata

print(metadata())
```

Example:

```python
{
    "name": "PQC English Wordlist Standard",
    "version": "1.0.0",
    "words": 4096,
    "bits_per_word": 12,
    "primary_hash": "SHA3-512",
    "signature_standard": "ML-DSA-65",
    "kdf_standard": "Argon2id"
}
```

---

## API Reference

### words()

Returns the complete wordlist.

```python
words()
```

Type:

```python
tuple[str, ...]
```

---

### word_at(index)

Returns the word at the specified index.

```python
word_at(index)
```

Type:

```python
str
```

Valid range:

```text
0-4095
```

---

### index_of(word)

Returns the index of a word.

```python
index_of(word)
```

Type:

```python
int
```

---

### contains(word)

Checks whether a word exists.

```python
contains(word)
```

Type:

```python
bool
```

---

### validate_wordlist()

Validates the embedded PQC wordlist.

```python
validate_wordlist()
```

Type:

```python
bool
```

---

### sha3_512()

Calculates the canonical SHA3-512 hash of the wordlist.

```python
sha3_512()
```

Type:

```python
str
```

---

### metadata()

Returns metadata describing the PQC Wordlist Standard.

```python
metadata()
```

Type:

```python
dict
```

---

## Example

```python
from pqc_wordlist import (
    words,
    word_at,
    index_of,
    contains,
    validate_wordlist,
    sha3_512,
)

print(len(words()))
print(word_at(0))
print(index_of(word_at(0)))
print(contains(word_at(0)))
print(validate_wordlist())
print(sha3_512())
```

---

## Roadmap

Future PQC Foundation standards built on top of this package:

* PQC Mnemonic Standard
* PQC Seed Standard
* PQC Address Standard
* PQC Wallet Standard

---

## License

MIT License

Copyright (c) 2026 PQC Foundation

---

## Project Structure

PQC Foundation Repository

https://github.com/rijol95-web3/pqc-foundation

Wordlist Standard

https://github.com/rijol95-web3/pqc-foundation/tree/main/pqc-wordlist

Python SDK

https://github.com/rijol95-web3/pqc-foundation/tree/main/python-pqc-wordlist