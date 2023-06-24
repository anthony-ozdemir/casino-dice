import unittest
import hashlib
import casino_dice

class TestCasinoDice(unittest.TestCase):
    def test_dice_roll_to_binary(self):
        dice = casino_dice.CasinoDice([1, 2, 3])
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(1), '001')
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(2), '010')
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(3), '011')
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(4), '100')
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(5), '101')
        self.assertEqual(dice._CasinoDice__dice_roll_to_binary(6), '110')

    def test_init(self):
        dice = casino_dice.CasinoDice([1, 2, 3, 4, 5, 6])
        self.assertEqual(dice.dice_rolls, [1, 2, 3, 4, 5, 6])
        self.assertEqual(dice.bin_dice_rolls, ['001', '010', '011', '100', '101', '110']) # 00101001 11001011 1000 0000
        self.assertEqual(dice.get_raw_binary(), b')\xcb\x80')

    def test_get_raw_binary(self):
        dice = casino_dice.CasinoDice([1, 2, 3, 4, 5, 6])  # 0010 1001 1100 1011 1000 0000
        self.assertEqual(dice.get_raw_binary(), b')\xcb\x80')

        dice = casino_dice.CasinoDice([6, 5, 4, 3, 2, 1])  # 1101 0110 0011 0100 0100 0000
        self.assertEqual(dice.get_raw_binary(), b'\xd64@')

    def test_sha256_hash(self):
        dice = casino_dice.CasinoDice([1, 2, 3, 4, 5, 6])
        sha256_hash = dice.get_sha256_hash()
        self.assertIsInstance(sha256_hash, bytes)

        # Check hash length
        self.assertEqual(len(sha256_hash), 32)

        # Check if the calculated hash matches the expected hash
        expected_sha256 = hashlib.sha256(dice.get_raw_binary()).digest()
        self.assertEqual(sha256_hash, expected_sha256)

        # Test for ValueError when the input bytes exceed 256-bit limit
        dice = casino_dice.CasinoDice([1] * 90)
        with self.assertRaises(ValueError):
            dice.get_sha256_hash()

    def test_sha512_hash(self):
        dice = casino_dice.CasinoDice([1, 2, 3, 4, 5, 6])
        sha512_hash = dice.get_sha512_hash()
        self.assertIsInstance(sha512_hash, bytes)

        # Check hash length
        self.assertEqual(len(sha512_hash), 64)

        # Check if the calculated hash matches the expected hash
        expected_sha512 = hashlib.sha512(dice.get_raw_binary()).digest()
        self.assertEqual(sha512_hash, expected_sha512)

        # Test for ValueError when the input bytes exceed 512-bit limit
        dice = casino_dice.CasinoDice([1] * 172)
        with self.assertRaises(ValueError):
            dice.get_sha512_hash()


if __name__ == '__main__':
    unittest.main()
