#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MSE Tools - Utility functions for MSE system management
Version: 29.0.0
"""

import os
import json
import shutil
import secrets
import hashlib
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class MSETools:
    """Utility tools for MSE system management."""
    
    def __init__(self, config_dir: str = "configs", data_dir: str = "data"):
        self.config_dir = Path(config_dir)
        self.data_dir = Path(data_dir)
        self.ensure_directories()
    
    def ensure_directories(self) -> None:
        """Ensure required directories exist."""
        self.config_dir.mkdir(exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)
    
    def generate_character_database(self, 
                                   output_file: str,
                                   length: int = 3000,
                                   charset: Optional[str] = None) -> None:
        """Generate a character database file."""
        import string
        
        if charset is None:
            # Default character set with repetitions for better distribution
            charset = (
                string.ascii_letters * 5 +
                string.digits * 3 +
                string.punctuation * 2 +
                "ÀÂÄÇÈÉÊËÎÏÔÙÛÜàâäçèéêëîïôùûü" * 2
            )
        
        # Generate random sequence
        chars = [secrets.choice(charset) for _ in range(length)]
        
        # Shuffle for better distribution
        import random
        random.shuffle(chars)
        
        # Write to file
        output_path = self.config_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(chars))
        
        logger.info(f"Generated character database: {output_path} ({length} characters)")
    
    def generate_random_config(self, output_file: str = "setting.json") -> Dict[str, Any]:
        """Generate a randomized configuration."""
        config = {
            "cipher": secrets.choice(["ascii_letters", "ascii_lowercase", "ascii_uppercase"]),
            "cipher_punctuation": secrets.choice(["True", "False"]),
            "cipher_digits": secrets.choice(["True", "False"]),
            "cipher_accent": secrets.choice(["True", "False"]),
            "charac_len": [
                secrets.randbelow(3) + 4,  # 4-6
                secrets.randbelow(3) + 7   # 7-9
            ],
            "len_special_charac": [
                secrets.randbelow(2) + 3,  # 3-4
                secrets.randbelow(2) + 5   # 5-6
            ],
            "key_number": [
                secrets.randbelow(500) + 1000,   # 1000-1500
                secrets.randbelow(1000) + 2000   # 2000-3000
            ],
            "len_charac_group_b": [
                secrets.randbelow(3) + 6,   # 6-8
                secrets.randbelow(5) + 10   # 10-14
            ],
            "mini_add_group_b_charac": secrets.randbelow(3) + 5,  # 5-7
            "max_add_group_b_charac": secrets.randbelow(3) + 8,   # 8-10
            "substitue_with": "configs/all.txt",
            "special_charac": "easintrluodchEASINTRLUODCH0123456789!#$%&'()*+,-./:;<=>?@[]"
        }
        
        # Ensure max > min values
        if config["charac_len"][1] <= config["charac_len"][0]:
            config["charac_len"][1] = config["charac_len"][0] + 1
        
        if config["len_special_charac"][1] <= config["len_special_charac"][0]:
            config["len_special_charac"][1] = config["len_special_charac"][0] + 1
        
        if config["key_number"][1] <= config["key_number"][0]:
            config["key_number"][1] = config["key_number"][0] + 100
        
        if config["len_charac_group_b"][1] <= config["len_charac_group_b"][0]:
            config["len_charac_group_b"][1] = config["len_charac_group_b"][0] + 2
        
        if config["max_add_group_b_charac"] <= config["mini_add_group_b_charac"]:
            config["max_add_group_b_charac"] = config["mini_add_group_b_charac"] + 1
        
        # Save configuration
        output_path = self.config_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        
        logger.info(f"Generated random configuration: {output_path}")
        return config
    
    def shuffle_database(self, database_file: str) -> None:
        """Shuffle characters in a database file."""
        db_path = self.config_dir / database_file
        
        if not db_path.exists():
            raise FileNotFoundError(f"Database file not found: {db_path}")
        
        with open(db_path, 'r', encoding='utf-8') as f:
            chars = list(f.read())
        
        import random
        random.shuffle(chars)
        
        with open(db_path, 'w', encoding='utf-8') as f:
            f.write(''.join(chars))
        
        logger.info(f"Shuffled database: {db_path}")
    
    def clean_database(self, database_file: str, remove_duplicates: bool = True) -> None:
        """Clean and optimize a database file."""
        db_path = self.config_dir / database_file
        
        if not db_path.exists():
            raise FileNotFoundError(f"Database file not found: {db_path}")
        
        with open(db_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove whitespace
        content = content.replace('\n', '').replace('\r', '').replace('\t', '')
        
        # Remove duplicates if requested
        if remove_duplicates:
            content = ''.join(dict.fromkeys(content))
        
        with open(db_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Cleaned database: {db_path}")
    
    def backup_configuration(self, backup_name: Optional[str] = None) -> str:
        """Create a backup of current configuration."""
        if backup_name is None:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        backup_dir = self.data_dir / "backups" / backup_name
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy configuration files
        for file in self.config_dir.glob("*"):
            if file.is_file():
                shutil.copy2(file, backup_dir)
        
        # Copy key library if exists
        keylib_path = Path("keylib.txt")
        if keylib_path.exists():
            shutil.copy2(keylib_path, backup_dir)
        
        logger.info(f"Created backup: {backup_dir}")
        return str(backup_dir)
    
    def restore_configuration(self, backup_name: str) -> None:
        """Restore configuration from backup."""
        backup_dir = self.data_dir / "backups" / backup_name
        
        if not backup_dir.exists():
            raise FileNotFoundError(f"Backup not found: {backup_dir}")
        
        # Restore configuration files
        for file in backup_dir.glob("*"):
            if file.is_file():
                if file.name == "keylib.txt":
                    shutil.copy2(file, "keylib.txt")
                else:
                    shutil.copy2(file, self.config_dir / file.name)
        
        logger.info(f"Restored configuration from: {backup_dir}")
    
    def calculate_system_hash(self) -> str:
        """Calculate hash of entire MSE system for integrity check."""
        hash_data = b""
        
        # Hash configuration files
        for file in sorted(self.config_dir.glob("*.json")):
            with open(file, 'rb') as f:
                hash_data += f.read()
        
        # Hash character databases
        for file in sorted(self.config_dir.glob("*.txt")):
            with open(file, 'rb') as f:
                hash_data += f.read()
        
        # Hash key library if exists
        keylib_path = Path("keylib.txt")
        if keylib_path.exists():
            with open(keylib_path, 'rb') as f:
                hash_data += f.read()
        
        return hashlib.sha3_512(hash_data).hexdigest()
    
    def analyze_encryption_strength(self, config_path: str = None) -> Dict[str, Any]:
        """Analyze the strength of current encryption configuration."""
        import math
        
        if config_path is None:
            config_path = self.config_dir / "setting.json"
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "config_file": str(config_path),
            "metrics": {}
        }
        
        # Calculate character space
        char_space = 0
        if config.get("cipher") == "ascii_letters":
            char_space += 52
        elif config.get("cipher") == "ascii_lowercase":
            char_space += 26
        elif config.get("cipher") == "ascii_uppercase":
            char_space += 26
        
        if config.get("cipher_punctuation") == "True":
            char_space += 32
        
        if config.get("cipher_digits") == "True":
            char_space += 10
        
        if config.get("cipher_accent") == "True":
            char_space += 26
        
        analysis["metrics"]["character_space"] = char_space
        
        # Calculate key complexity
        avg_key_length = sum(config["charac_len"]) / 2
        num_keys = sum(config["key_number"]) / 2
        
        analysis["metrics"]["average_key_length"] = avg_key_length
        analysis["metrics"]["number_of_keys"] = num_keys
        analysis["metrics"]["key_space_bits"] = math.log2(char_space ** avg_key_length) if char_space > 0 else 0
        
        # Calculate obfuscation level
        obfuscation_additions = sum([
            config["mini_add_group_b_charac"],
            config["max_add_group_b_charac"]
        ]) / 2
        
        analysis["metrics"]["obfuscation_level"] = obfuscation_additions
        
        # Overall strength score (0-100)
        strength_score = min(100, (
            (analysis["metrics"]["key_space_bits"] / 256) * 40 +
            (num_keys / 5000) * 30 +
            (obfuscation_additions / 20) * 30
        ))
        
        analysis["strength_score"] = round(strength_score, 2)
        
        # Recommendations
        recommendations = []
        if char_space < 60:
            recommendations.append("Enable more character types for increased complexity")
        if num_keys < 2000:
            recommendations.append("Increase number of keys for better security")
        if avg_key_length < 5:
            recommendations.append("Increase key length for stronger encryption")
        
        analysis["recommendations"] = recommendations
        
        return analysis
    
    def reset_system(self, full_reset: bool = False) -> None:
        """Reset the MSE system."""
        # Remove temporary files
        temp_files = ["keylib.txt", "user.txt", "user.data"]
        for file in temp_files:
            file_path = Path(file)
            if file_path.exists():
                file_path.unlink()
                logger.info(f"Removed: {file}")
        
        # Remove cache directories
        cache_dirs = ["__pycache__", "configs/__pycache__"]
        for cache_dir in cache_dirs:
            cache_path = Path(cache_dir)
            if cache_path.exists():
                shutil.rmtree(cache_path)
                logger.info(f"Removed cache: {cache_dir}")
        
        if full_reset:
            # Remove all generated files
            if self.data_dir.exists():
                shutil.rmtree(self.data_dir)
                logger.info(f"Removed data directory: {self.data_dir}")
            
            # Reset configurations to default
            self.generate_character_database("all.txt", 3000)
            self.generate_random_config()
            logger.info("Full system reset completed")
        else:
            logger.info("Basic system reset completed")


class PerformanceOptimizer:
    """Performance optimization utilities for MSE."""
    
    @staticmethod
    def benchmark_encryption(mse_instance, test_text: str = None, iterations: int = 100) -> Dict[str, float]:
        """Benchmark encryption/decryption performance."""
        import time
        
        if test_text is None:
            test_text = "The quick brown fox jumps over the lazy dog. " * 10
        
        results = {
            "iterations": iterations,
            "text_length": len(test_text)
        }
        
        # Benchmark encryption
        start = time.perf_counter()
        for _ in range(iterations):
            encrypted = mse_instance.encrypt(test_text)
        end = time.perf_counter()
        
        results["encryption_total_time"] = end - start
        results["encryption_avg_time"] = (end - start) / iterations
        results["encryption_throughput"] = (len(test_text) * iterations) / (end - start)
        
        # Benchmark decryption
        encrypted = mse_instance.encrypt(test_text)
        start = time.perf_counter()
        for _ in range(iterations):
            decrypted = mse_instance.decrypt(encrypted)
        end = time.perf_counter()
        
        results["decryption_total_time"] = end - start
        results["decryption_avg_time"] = (end - start) / iterations
        results["decryption_throughput"] = (len(encrypted) * iterations) / (end - start)
        
        return results
    
    @staticmethod
    def optimize_key_library(key_manager, target_size: int = 2000) -> None:
        """Optimize key library size for performance."""
        current_size = len(key_manager.keys)
        
        if current_size > target_size:
            # Reduce to target size
            key_manager.keys = key_manager.keys[:target_size]
            logger.info(f"Reduced key library from {current_size} to {target_size}")
        elif current_size < target_size:
            # Generate additional keys
            additional = target_size - current_size
            for _ in range(additional):
                key_manager.keys.append(key_manager.generate_key())
            logger.info(f"Expanded key library from {current_size} to {target_size}")


if __name__ == "__main__":
    # Example usage
    tools = MSETools()
    
    # Generate a new character database
    tools.generate_character_database("test_db.txt", length=1000)
    
    # Generate random configuration
    config = tools.generate_random_config("test_config.json")
    print("Generated config:", json.dumps(config, indent=2))
    
    # Analyze encryption strength
    analysis = tools.analyze_encryption_strength("test_config.json")
    print("\nEncryption Analysis:")
    print(f"Strength Score: {analysis['strength_score']}/100")
    print(f"Recommendations: {analysis['recommendations']}")
