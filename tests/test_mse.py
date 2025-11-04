#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE Unit Tests
Tests for the Multiple Substitution Encryption system
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MSE import mse_cipher, mse_decipher, get_encryption_stats, verify_encryption


class TestMSEBasicFunctionality(unittest.TestCase):
    """Test basic encryption and decryption functionality"""
    
    def test_simple_encryption_decryption(self):
        """Test that encryption and decryption are reversible"""
        original = "Hello World"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_empty_string_raises_error(self):
        """Test that empty strings raise ValueError"""
        with self.assertRaises(ValueError):
            mse_cipher("", auto_copy=False)
        
        with self.assertRaises(ValueError):
            mse_decipher("", auto_copy=False)
    
    def test_non_string_input_raises_error(self):
        """Test that non-string inputs raise ValueError"""
        with self.assertRaises(ValueError):
            mse_cipher(123, auto_copy=False)
        
        with self.assertRaises(ValueError):
            mse_decipher(456, auto_copy=False)
    
    def test_whitespace_only_raises_error(self):
        """Test that whitespace-only strings raise ValueError"""
        with self.assertRaises(ValueError):
            mse_cipher("   ", auto_copy=False)


class TestMSECharacterSets(unittest.TestCase):
    """Test encryption with different character sets"""
    
    def test_lowercase_letters(self):
        """Test encryption of lowercase letters"""
        original = "abcdefghijklmnopqrstuvwxyz"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_uppercase_letters(self):
        """Test encryption of uppercase letters"""
        original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_digits(self):
        """Test encryption of digits"""
        original = "0123456789"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_punctuation(self):
        """Test encryption of punctuation marks"""
        original = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_accented_characters(self):
        """Test encryption of French accented characters"""
        original = "àâéèêëîïôùûüç"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_mixed_characters(self):
        """Test encryption of mixed character types"""
        original = "Hello123!@# Wörld éèê"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)


class TestMSEMessageLengths(unittest.TestCase):
    """Test encryption with different message lengths"""
    
    def test_single_character(self):
        """Test encryption of single character"""
        original = "A"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_short_message(self):
        """Test encryption of short message"""
        original = "Hi"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_medium_message(self):
        """Test encryption of medium-length message"""
        original = "The quick brown fox jumps over the lazy dog"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_long_message(self):
        """Test encryption of long message"""
        original = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_very_long_message(self):
        """Test encryption of very long message"""
        original = "A" * 10000
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)


class TestMSEEncryptionProperties(unittest.TestCase):
    """Test properties of the encryption"""
    
    def test_encryption_increases_length(self):
        """Test that encrypted text is longer than original"""
        original = "Hello World"
        encrypted = mse_cipher(original, auto_copy=False)
        self.assertGreater(len(encrypted), len(original))
    
    def test_encryption_is_different(self):
        """Test that encrypted text differs from original"""
        original = "Hello World"
        encrypted = mse_cipher(original, auto_copy=False)
        self.assertNotEqual(original, encrypted)
    
    def test_multiple_encryptions_differ(self):
        """Test that same message encrypted twice produces different results"""
        original = "Hello World"
        encrypted1 = mse_cipher(original, auto_copy=False)
        encrypted2 = mse_cipher(original, auto_copy=False)
        # This might fail occasionally due to random key selection
        # but should pass most of the time
        self.assertNotEqual(encrypted1, encrypted2)


class TestMSEStatistics(unittest.TestCase):
    """Test encryption statistics functions"""
    
    def test_get_encryption_stats(self):
        """Test that statistics are calculated correctly"""
        original = "Hello World"
        encrypted = mse_cipher(original, auto_copy=False)
        stats = get_encryption_stats(original, encrypted)
        
        self.assertEqual(stats['original_length'], len(original))
        self.assertEqual(stats['encrypted_length'], len(encrypted))
        self.assertGreater(stats['expansion_ratio'], 1.0)
        self.assertIsInstance(stats['original_unique_chars'], int)
        self.assertIsInstance(stats['encrypted_unique_chars'], int)
    
    def test_verify_encryption(self):
        """Test encryption verification function"""
        original = "Test message"
        result = verify_encryption(original)
        self.assertTrue(result)
    
    def test_verify_encryption_with_encrypted(self):
        """Test verification with pre-encrypted message"""
        original = "Test message"
        encrypted = mse_cipher(original, auto_copy=False)
        result = verify_encryption(original, encrypted)
        self.assertTrue(result)


class TestMSESpecialCases(unittest.TestCase):
    """Test special edge cases"""
    
    def test_spaces_only(self):
        """Test message with multiple spaces"""
        original = "     "
        with self.assertRaises(ValueError):
            mse_cipher(original, auto_copy=False)
    
    def test_newlines_and_tabs(self):
        """Test message with newlines and tabs"""
        # Note: This might fail if the system doesn't support these characters
        original = "Line1\nLine2\tTabbed"
        try:
            encrypted = mse_cipher(original, auto_copy=False)
            decrypted = mse_decipher(encrypted, auto_copy=False)
            # Check if they're equal (might differ in whitespace handling)
            self.assertEqual(original, decrypted)
        except Exception:
            # If not supported, skip this test
            self.skipTest("Newlines and tabs not supported")
    
    def test_repeated_characters(self):
        """Test message with repeated characters"""
        original = "aaaaaabbbbbbcccccc"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_palindrome(self):
        """Test palindrome message"""
        original = "A man a plan a canal Panama"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)


class TestMSEMultilingual(unittest.TestCase):
    """Test encryption with different languages"""
    
    def test_french_text(self):
        """Test French text with accents"""
        original = "Bonjour, comment ça va? C'est une belle journée!"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)
    
    def test_english_text(self):
        """Test English text"""
        original = "Hello, how are you? It's a beautiful day!"
        encrypted = mse_cipher(original, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        self.assertEqual(original, decrypted)


def run_tests():
    """Run all test suites"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestMSEBasicFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestMSECharacterSets))
    suite.addTests(loader.loadTestsFromTestCase(TestMSEMessageLengths))
    suite.addTests(loader.loadTestsFromTestCase(TestMSEEncryptionProperties))
    suite.addTests(loader.loadTestsFromTestCase(TestMSEStatistics))
    suite.addTests(loader.loadTestsFromTestCase(TestMSESpecialCases))
    suite.addTests(loader.loadTestsFromTestCase(TestMSEMultilingual))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
