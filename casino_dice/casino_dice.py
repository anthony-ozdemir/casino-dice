import hashlib


class CasinoDice:
    def __init__(self, dice_rolls: list[int | str]):
        self.dice_rolls = []
        for roll in dice_rolls:
            if isinstance(roll, str):
                try:
                    roll = int(roll)
                except ValueError:
                    raise ValueError("Invalid dice roll. Input should be a number between 1 and 6.")

            if roll < 1 or roll > 6:
                raise ValueError("Invalid dice roll. Allowed values are between 1 and 6.")
            self.dice_rolls.append(roll)

        self.bin_dice_rolls = []
        # Convert to string binary representation
        for dice_roll in self.dice_rolls:
            bin_dice_roll = self.__dice_roll_to_binary(dice_roll)
            self.bin_dice_rolls.append(bin_dice_roll)

        # Combine the binary representations into a single bitstring.
        bitstring = ''.join(self.bin_dice_rolls)
        padding_needed = 8 - len(bitstring) % 8
        if padding_needed != 8:
            bitstring = bitstring + '0' * padding_needed

        byte_strings = []
        for i in range(0, len(bitstring), 8):
            byte_str = bitstring[i:i + 8]
            byte_strings.append(byte_str)

        # Convert each byte substring to its corresponding integer value using a for loop
        byte_values = []
        for byte_str in byte_strings:
            byte_value = int(byte_str, 2)
            byte_values.append(byte_value)

        # Pack the list of byte values into a binary data format.
        self.raw_binary_data = bytes(byte_values)

    def get_raw_binary(self):
        return self.raw_binary_data

    # Converts a single dice roll result to its binary representation.
    # dice_roll: an integer from 1 to 6, representing the dice roll result.
    # Returns: a 3-bit binary string representation of the dice roll.
    def __dice_roll_to_binary(self, dice_roll) -> str:
        # The `bin()` function converts an integer to its binary
        # representation as a string, e.g., bin(5) -> '0b101'.
        binary_repr = bin(dice_roll)

        # We need only the last 3 characters of the binary_repr string
        # and pad with zeros if necessary, as the first two characters are '0b'.
        return binary_repr[2:].zfill(3)

    def get_sha256_hash(self) -> bytes:
        if len(self.raw_binary_data) > 32:
            raise ValueError("The raw binary data exceeds the 256-bit limit for SHA256 hashing.")

        sha256_hash = hashlib.sha256(self.raw_binary_data)  # Using self.raw_binary_data from the previous step
        return sha256_hash.digest()

    def get_sha512_hash(self) -> bytes:
        if len(self.raw_binary_data) > 64:
            raise ValueError("The raw binary data exceeds the 512-bit limit for SHA512 hashing.")

        sha512_hash = hashlib.sha512(self.raw_binary_data)  # Using self.raw_binary_data from the previous step
        return sha512_hash.digest()
