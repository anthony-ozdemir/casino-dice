# Casino Dice Library

Generating secure cryptographic keys requires a strong source of entropy. Hardware entropy generators are commonly used for this purpose. However, they may be untrustworthy due to design vulnerabilities or malicious tampering by bad actors. This library provides an alternative source of entropy using physical casino dice rolls to create byte representations for generating computational secrets, such as private SSH keys and CA certificates.

## Background

Hardware entropy generators are embedded in most computers, smartphones, and other devices. These generators rely on unpredictable physical processes such as electronic noise to generate random numbers. Despite built-in hardware generators being widely used, several factors can make them untrustworthy:

1. Design flaws: If the hardware design has weaknesses, it can lead to less random and predictable outputs.
2. Reverse engineering: An attacker could reverse engineer the hardware generator to find vulnerabilities or weaknesses in the source of entropy.
3. Supply chain risks: An attacker may tamper with the components of the device during manufacturing, transit, or storage, adding backdoors, or hidden functionalities to compromise the entropy generation.
4. Malware attacks: Malicious code might compromise the hardware generator's functionality, resulting in less secure entropy.

Casino dice are generally considered to be a trustworthy source of entropy due to the strict regulations and manufacturing standards they must adhere to. These dice are designed for fairness and highly accurate randomness. The manufacturing precision and the use of a translucent material make it difficult to tamper with casino dice without being detected.

Certified casino dice feature:

1. Precise manufacturing: High-precision processes ensure that each side of the dice has equal dimensions, reducing the chances of consistently landing on a specific side.
2. Identical weight distribution: Equal weight distribution across the dice, ensuring that each roll has an equal probability of landing on any number.
3. Sharp edges and corners: Distinctive sharp edges and corners to minimize interference during a roll, increasing the entropic quality.
4. Translucent material: Casino dice are made of a translucent material, making it challenging to introduce manipulative elements without being noticeable.

Using a physical casino dice roll as a source of entropy provides a high level of randomness and security, ensuring that the generated secrets are significantly more challenging to predict or compromise.

## Features

- Convert a list of casino dice rolls into a binary data format
- Calculate SHA-256 and SHA-512 hashes of the generated binary data

## Installation

Use the package manager pip to install the library.

```bash
pip install casino-dice
```

To install the library from source:

```bash
git clone https://github.com/anthony-ozdemir/casino-dice.git
cd casino_dice
pip install .
```

## Usage

```python
from casino_dice import CasinoDice

# Initialize the CasinoDice object with a list of dice rolls (integers 1-6)
dice = CasinoDice([1, 2, 3, 4, 5, 6])

# Get the raw binary data
raw_binary = dice.get_raw_binary()

# Compute the SHA-256 and SHA-512 hashes
sha256_hash = dice.get_sha256_hash()
sha512_hash = dice.get_sha512_hash()
```


### Generating a LUKS Master Key

LUKS usually relies on hardware entropy generators to create its master key. However, as an alternative due to the potential trustworthiness concerns, we can use the casino-dice library for generating a master key with 128 bits of entropy by rolling a dice at least 50 times. Capture the dice rolls as a list and pass it to the `CasinoDice` object.

```python
import os
from casino_dice import CasinoDice

# Capture 50 dice rolls
dice_rolls = [5, 1, 2, 4, 6, 3, 1, 2, 3, 5, 6, 2, 3, 4, 1, 6, 6, 1, 4, 3,
              4, 5, 6, 2, 1, 6, 3, 5, 4, 1, 1, 6, 5, 3, 2, 2, 5, 6, 3, 4,
              4, 2, 1, 6, 1, 3, 3, 4, 5, 2]

# Initialize the CasinoDice object with the 50 dice rolls
# for approximately 128bits of entropy
dice = CasinoDice(dice_rolls)

# Compute the SHA-512 hash to minimize entropy loss when creating
# a master-key with 512bits
sha512_hash = dice.get_sha512_hash()

# Save the hash as the master key to a file
with open('master_key.bin', 'wb') as f:
    f.write(sha512_hash)
```

### Generating Other Cryptographic Keys

Similarly, you can use the output of the Casino Dice Entropy library for generating other types of cryptographic keys like PGP keys, SSL certificates, etc., by using the resulting binary or hashed data as the input for the respective key generation tools.
