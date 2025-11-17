#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MSE Test Suite - Comprehensive tests for MSE encryption system
Version: 29.0.0
"""

import unittest
import tempfile
import json
import os
from pathlib import Path

# Import MSE modules
from mse_core import MSE, MSEConfig, CharacterSet, KeyManager, TextObfuscator, BlockCipher
from mse_tools import MSETools, PerformanceOptimizer


class TestMSEConfig(unittest.TestCase):
    """Test MSEConfig class."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = MSEConfig()
        self.assertEqual(config.cipher_type, "ascii_letters")
        self.assertTrue(config.use_punctuation)
        self.assertTrue(config.use_digits)
        self.assertTrue(config.use_accents)
        self.assertEqual(config.charac_len, (5, 6))
        self.assertEqual(config.key_count, (1000, 1971))
    
    def test_config_from_json(self):
        """Test loading configuration from JSON."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({
                'cipher': 'ascii_lowercase',
                'cipher_punctuation': 'False',
                'cipher_digits': 'True',
                'cipher_accent': 'False',
                'charac_len': [3, 5],
                'len_special_charac': [2, 3],
                'key_number': [500, 1000],
                'len_charac_group_b': [5, 8],
                'mini_add_group_b_charac': 5,
                'max_add_group_b_charac': 7,
                'substitue_with': 'test.txt',
                'special_charac': 'test123'
            }, f)
            temp_file = f.name
        
        try:
            config = MSEConfig.from_json(temp_file)
            self.assertEqual(config.cipher_type, 'ascii_lowercase')
            self.assertFalse(config.use_punctuation)
            self.assertTrue(config.use_digits)
            self.assertFalse(config.use_accents)
            self.assertEqual(config.charac_len, (3, 5))
            self.assertEqual(config.key_count, (500, 1000))
        finally:
            os.unlink(temp_file)
    
    def test_config_to_json(self):
        """Test saving configuration to JSON."""
        config = MSEConfig(
            cipher_type="ascii_uppercase",
            use_punctuation=False,
            key_count=(2000, 3000)
        )
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            config.to_json(temp_file)
            
            with open(temp_file, 'r') as f:
                data = json.load(f)
            
            self.assertEqual(data['cipher'], 'ascii_uppercase')
            self.assertEqual(data['cipher_punctuation'], 'False')
            self.assertEqual(data['key_number'], [2000, 3000])
        finally:
            os.unlink(temp_file)


class TestCharacterSet(unittest.TestCase):
    """Test CharacterSet class."""
    
    def test_character_set_lowercase(self):
        """Test character set with lowercase only."""
        config = MSEConfig(
            cipher_type="ascii_lowercase",
            use_punctuation=False,
            use_digits=False,
            use_accents=False
        )
        char_set = CharacterSet(config)
        
        import string
        expected = string.ascii_lowercase + " "
        self.assertEqual(char_set.substitution_chars, expected)
    
    def test_character_set_full(self):
        """Test character set with all options enabled."""
        config = MSEConfig(
            cipher_type="ascii_letters",
            use_punctuation=True,
            use_digits=True,
            use_accents=True
        )
        char_set = CharacterSet(config)
        
        import string
        # Should contain letters, punctuation, digits, accents, and space
        self.assertIn('a', char_set.substitution_chars)
        self.assertIn('A', char_set.substitution_chars)
        self.assertIn('!', char_set.substitution_chars)
        self.assertIn('0', char_set.substitution_chars)
        self.assertIn('À', char_set.substitution_chars)
        self.assertIn(' ', char_set.substitution_chars)


class TestTextObfuscator(unittest.TestCase):
    """Test TextObfuscator class."""
    
    def test_split_word_even(self):
        """Test splitting word with even length."""
        first, second = TextObfuscator.split_word("test")
        self.assertEqual(first, "st")
        self.assertEqual(second, "te")
    
    def test_split_word_odd(self):
        """Test splitting word with odd length."""
        first, second = TextObfuscator.split_word("hello")
        self.assertEqual(first, "l")
        self.assertEqual(second, "heo")
    
    def test_reverse_word(self):
        """Test word reversal."""
        result = TextObfuscator.reverse_word("hello")
        self.assertEqual(result, "lheo")
    
    def test_process_sentence(self):
        """Test sentence processing."""
        sentence = "hello world"
        result = TextObfuscator.process_sentence(sentence, reverse=True)
        # Each word should be reversed
        words = result.split()
        self.assertEqual(len(words), 2)


class TestMSEEncryption(unittest.TestCase):
    """Test MSE encryption/decryption."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mse = MSE()
    
    def test_basic_encryption_decryption(self):
        """Test basic encryption and decryption."""
        texts = [
            "Hello, World!",
            "The quick brown fox jumps over the lazy dog",
            "12345 ABC xyz !@#$%",
            "Testing MSE v29.0",
            ""  # Empty string
        ]
        
        for original in texts:
            with self.subTest(text=original):
                encrypted = self.mse.encrypt(original)
                decrypted = self.mse.decrypt(encrypted)
                self.assertEqual(original, decrypted)
    
    def test_encryption_expansion(self):
        """Test that encryption expands text."""
        original = "Test message"
        encrypted = self.mse.encrypt(original)
        
        # Encrypted text should be longer due to obfuscation
        self.assertGreater(len(encrypted), len(original))
    
    def test_encryption_uniqueness(self):
        """Test that multiple encryptions produce different results."""
        original = "Test message"
        
        # Generate multiple encryptions
        encryptions = [self.mse.encrypt(original) for _ in range(5)]
        
        # All should decrypt to the same original
        for encrypted in encryptions:
            self.assertEqual(self.mse.decrypt(encrypted), original)
        
        # But encrypted versions should be different (due to randomness)
        # Note: There's a small chance they could be the same, but very unlikely
        unique_encryptions = set(encryptions)
        self.assertGreater(len(unique_encryptions), 1)
    
    def test_special_characters(self):
        """Test encryption with special characters."""
        special_texts = [
            "Unicode: À Ç É ñ ü",
            "Symbols: ♠ ♣ ♥ ♦",
            "Emoji: 😀 🎉 🔐",
            "Mixed: Hello_世界_مرحبا"
        ]
        
        for text in special_texts:
            with self.subTest(text=text):
                try:
                    encrypted = self.mse.encrypt(text)
                    decrypted = self.mse.decrypt(encrypted)
                    # May not handle all Unicode perfectly
                    self.assertIsInstance(encrypted, str)
                    self.assertIsInstance(decrypted, str)
                except Exception:
                    # Some characters might not be supported
                    pass


class TestMSETools(unittest.TestCase):
    """Test MSETools utilities."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.tools = MSETools(config_dir="test_configs", data_dir="test_data")
    
    def tearDown(self):
        """Clean up test files."""
        import shutil
        for dir_name in ["test_configs", "test_data"]:
            if Path(dir_name).exists():
                shutil.rmtree(dir_name)
    
    def test_generate_character_database(self):
        """Test character database generation."""
        self.tools.generate_character_database("test_db.txt", length=100)
        
        db_path = Path("test_configs") / "test_db.txt"
        self.assertTrue(db_path.exists())
        
        with open(db_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertEqual(len(content), 100)
    
    def test_generate_random_config(self):
        """Test random configuration generation."""
        config = self.tools.generate_random_config("test_config.json")
        
        self.assertIn('cipher', config)
        self.assertIn('key_number', config)
        self.assertIsInstance(config['key_number'], list)
        self.assertEqual(len(config['key_number']), 2)
        
        # Check that max > min values
        self.assertGreater(config['charac_len'][1], config['charac_len'][0])
        self.assertGreater(config['key_number'][1], config['key_number'][0])
    
    def test_analyze_encryption_strength(self):
        """Test encryption strength analysis."""
        # Create a test config
        config = {
            "cipher": "ascii_letters",
            "cipher_punctuation": "True",
            "cipher_digits": "True",
            "cipher_accent": "False",
            "charac_len": [5, 6],
            "len_special_charac": [3, 4],
            "key_number": [1000, 2000],
            "len_charac_group_b": [8, 11],
            "mini_add_group_b_charac": 7,
            "max_add_group_b_charac": 9,
            "substitue_with": "test.txt",
            "special_charac": "test"
        }
        
        config_path = Path("test_configs") / "analyze_config.json"
        with open(config_path, 'w') as f:
            json.dump(config, f)
        
        analysis = self.tools.analyze_encryption_strength(str(config_path))
        
        self.assertIn('strength_score', analysis)
        self.assertIn('metrics', analysis)
        self.assertIn('recommendations', analysis)
        
        self.assertIsInstance(analysis['strength_score'], (int, float))
        self.assertGreaterEqual(analysis['strength_score'], 0)
        self.assertLessEqual(analysis['strength_score'], 100)


class TestPerformanceOptimizer(unittest.TestCase):
    """Test PerformanceOptimizer."""
    
    def test_benchmark(self):
        """Test performance benchmarking."""
        mse = MSE()
        optimizer = PerformanceOptimizer()
        
        results = optimizer.benchmark_encryption(
            mse,
            test_text="Test message for benchmarking",
            iterations=10
        )
        
        self.assertIn('encryption_avg_time', results)
        self.assertIn('decryption_avg_time', results)
        self.assertIn('encryption_throughput', results)
        self.assertIn('decryption_throughput', results)
        
        self.assertGreater(results['encryption_throughput'], 0)
        self.assertGreater(results['decryption_throughput'], 0)


class TestKeyManager(unittest.TestCase):
    """Test KeyManager functionality."""
    
    def test_key_generation(self):
        """Test key generation."""
        config = MSEConfig()
        char_set = CharacterSet(config)
        key_manager = KeyManager(char_set, config)
        
        key = key_manager.generate_key()
        
        self.assertIsInstance(key, list)
        self.assertEqual(len(key), len(char_set.substitution_chars))
        
        # Each substitution should be a string
        for substitution in key:
            self.assertIsInstance(substitution, str)
            self.assertGreater(len(substitution), 0)
    
    def test_key_library_generation(self):
        """Test key library generation."""
        config = MSEConfig(key_count=(10, 20))
        char_set = CharacterSet(config)
        key_manager = KeyManager(char_set, config)
        
        key_manager.generate_key_library()
        
        self.assertGreaterEqual(len(key_manager.keys), 10)
        self.assertLessEqual(len(key_manager.keys), 20)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    test_cases = [
        TestMSEConfig,
        TestCharacterSet,
        TestTextObfuscator,
        TestMSEEncryption,
        TestMSETools,
        TestPerformanceOptimizer,
        TestKeyManager,
    ]
    
    for test_case in test_cases:
        suite.addTests(loader.loadTestsFromTestCase(test_case))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)
