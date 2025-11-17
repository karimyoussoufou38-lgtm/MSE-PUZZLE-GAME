#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MSE CLI - Command Line Interface for MSE
Version: 29.0.0
"""

import sys
import argparse
import json
from pathlib import Path
from typing import Optional
import logging
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Import MSE modules
from mse_core import MSE, MSEConfig
from mse_tools import MSETools, PerformanceOptimizer


class MSECLI:
    """Command-line interface for MSE operations."""
    
    def __init__(self):
        self.tools = MSETools()
        self.setup_logging()
    
    def setup_logging(self, level=logging.INFO):
        """Configure logging with colored output."""
        class ColoredFormatter(logging.Formatter):
            COLORS = {
                'DEBUG': Fore.CYAN,
                'INFO': Fore.GREEN,
                'WARNING': Fore.YELLOW,
                'ERROR': Fore.RED,
                'CRITICAL': Fore.RED + Style.BRIGHT,
            }
            
            def format(self, record):
                log_color = self.COLORS.get(record.levelname, '')
                record.levelname = f"{log_color}{record.levelname}{Style.RESET_ALL}"
                return super().format(record)
        
        handler = logging.StreamHandler()
        handler.setFormatter(ColoredFormatter('%(levelname)s: %(message)s'))
        
        logger = logging.getLogger()
        logger.setLevel(level)
        logger.handlers = [handler]
    
    def encrypt_text(self, text: str, config_path: Optional[str] = None, 
                    output_file: Optional[str] = None, show_stats: bool = False) -> None:
        """Encrypt text with optional output to file."""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}MSE ENCRYPTION")
        print(f"{Fore.CYAN}{'=' * 50}\n")
        
        # Load configuration
        if config_path:
            config = MSEConfig.from_json(config_path)
            mse = MSE(config=config)
        else:
            mse = MSE()
        
        # Encrypt the text
        print(f"{Fore.YELLOW}Original text ({len(text)} chars):{Style.RESET_ALL}")
        print(f"{text[:100]}{'...' if len(text) > 100 else ''}\n")
        
        encrypted = mse.encrypt(text)
        
        print(f"{Fore.GREEN}Encrypted text ({len(encrypted)} chars):{Style.RESET_ALL}")
        print(f"{encrypted[:100]}{'...' if len(encrypted) > 100 else ''}\n")
        
        # Save to file if requested
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted)
            print(f"{Fore.GREEN}✓ Encrypted text saved to: {output_file}{Style.RESET_ALL}")
        
        # Show statistics if requested
        if show_stats:
            expansion_ratio = len(encrypted) / len(text)
            print(f"\n{Fore.CYAN}Encryption Statistics:{Style.RESET_ALL}")
            print(f"  • Original length: {len(text)} characters")
            print(f"  • Encrypted length: {len(encrypted)} characters")
            print(f"  • Expansion ratio: {expansion_ratio:.2f}x")
            print(f"  • Key library size: {len(mse.key_manager.keys)} keys")
            print(f"  • System hash: {mse.get_hash()[:16]}...")
    
    def decrypt_text(self, text: str, config_path: Optional[str] = None,
                    output_file: Optional[str] = None) -> None:
        """Decrypt text with optional output to file."""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}MSE DECRYPTION")
        print(f"{Fore.CYAN}{'=' * 50}\n")
        
        # Load configuration
        if config_path:
            config = MSEConfig.from_json(config_path)
            mse = MSE(config=config)
        else:
            mse = MSE()
        
        # Decrypt the text
        print(f"{Fore.YELLOW}Encrypted text ({len(text)} chars):{Style.RESET_ALL}")
        print(f"{text[:100]}{'...' if len(text) > 100 else ''}\n")
        
        decrypted = mse.decrypt(text)
        
        print(f"{Fore.GREEN}Decrypted text ({len(decrypted)} chars):{Style.RESET_ALL}")
        print(f"{decrypted[:100]}{'...' if len(decrypted) > 100 else ''}\n")
        
        # Save to file if requested
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decrypted)
            print(f"{Fore.GREEN}✓ Decrypted text saved to: {output_file}{Style.RESET_ALL}")
    
    def encrypt_file(self, input_file: str, output_file: Optional[str] = None,
                    config_path: Optional[str] = None) -> None:
        """Encrypt a file."""
        if not Path(input_file).exists():
            print(f"{Fore.RED}✗ Input file not found: {input_file}{Style.RESET_ALL}")
            return
        
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        if output_file is None:
            output_file = f"{input_file}.mse"
        
        self.encrypt_text(text, config_path, output_file, show_stats=True)
    
    def decrypt_file(self, input_file: str, output_file: Optional[str] = None,
                    config_path: Optional[str] = None) -> None:
        """Decrypt a file."""
        if not Path(input_file).exists():
            print(f"{Fore.RED}✗ Input file not found: {input_file}{Style.RESET_ALL}")
            return
        
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        if output_file is None:
            output_file = input_file.replace('.mse', '.decrypted')
        
        self.decrypt_text(text, config_path, output_file)
    
    def generate_config(self, output_file: str = "configs/setting.json") -> None:
        """Generate a new random configuration."""
        print(f"\n{Fore.CYAN}Generating random configuration...{Style.RESET_ALL}")
        config = self.tools.generate_random_config(output_file)
        
        print(f"{Fore.GREEN}✓ Configuration saved to: {output_file}{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}Generated configuration:{Style.RESET_ALL}")
        print(json.dumps(config, indent=2))
    
    def generate_database(self, output_file: str, length: int = 3000) -> None:
        """Generate a new character database."""
        print(f"\n{Fore.CYAN}Generating character database...{Style.RESET_ALL}")
        self.tools.generate_character_database(output_file, length)
        print(f"{Fore.GREEN}✓ Database saved to: configs/{output_file} ({length} characters){Style.RESET_ALL}")
    
    def analyze_strength(self, config_path: Optional[str] = None) -> None:
        """Analyze encryption strength."""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}ENCRYPTION STRENGTH ANALYSIS")
        print(f"{Fore.CYAN}{'=' * 50}\n")
        
        analysis = self.tools.analyze_encryption_strength(config_path)
        
        # Display strength score with color coding
        score = analysis['strength_score']
        if score >= 80:
            score_color = Fore.GREEN
            rating = "EXCELLENT"
        elif score >= 60:
            score_color = Fore.YELLOW
            rating = "GOOD"
        elif score >= 40:
            score_color = Fore.YELLOW
            rating = "MODERATE"
        else:
            score_color = Fore.RED
            rating = "WEAK"
        
        print(f"{Fore.YELLOW}Configuration:{Style.RESET_ALL} {analysis['config_file']}")
        print(f"{Fore.YELLOW}Analysis Time:{Style.RESET_ALL} {analysis['timestamp']}\n")
        
        print(f"{Fore.CYAN}Strength Score:{Style.RESET_ALL} {score_color}{score:.1f}/100 ({rating}){Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}Metrics:{Style.RESET_ALL}")
        for key, value in analysis['metrics'].items():
            if isinstance(value, float):
                print(f"  • {key.replace('_', ' ').title()}: {value:.2f}")
            else:
                print(f"  • {key.replace('_', ' ').title()}: {value}")
        
        if analysis['recommendations']:
            print(f"\n{Fore.YELLOW}Recommendations:{Style.RESET_ALL}")
            for rec in analysis['recommendations']:
                print(f"  ⚠ {rec}")
    
    def benchmark(self, text: Optional[str] = None, iterations: int = 100,
                 config_path: Optional[str] = None) -> None:
        """Run performance benchmark."""
        print(f"\n{Fore.CYAN}{'=' * 50}")
        print(f"{Fore.CYAN}PERFORMANCE BENCHMARK")
        print(f"{Fore.CYAN}{'=' * 50}\n")
        
        # Load configuration and create MSE instance
        if config_path:
            config = MSEConfig.from_json(config_path)
            mse = MSE(config=config)
        else:
            mse = MSE()
        
        # Run benchmark
        optimizer = PerformanceOptimizer()
        results = optimizer.benchmark_encryption(mse, text, iterations)
        
        print(f"{Fore.YELLOW}Benchmark Parameters:{Style.RESET_ALL}")
        print(f"  • Iterations: {results['iterations']}")
        print(f"  • Text length: {results['text_length']} characters\n")
        
        print(f"{Fore.CYAN}Encryption Performance:{Style.RESET_ALL}")
        print(f"  • Total time: {results['encryption_total_time']:.3f} seconds")
        print(f"  • Average time: {results['encryption_avg_time']*1000:.2f} ms")
        print(f"  • Throughput: {results['encryption_throughput']:.0f} chars/second\n")
        
        print(f"{Fore.CYAN}Decryption Performance:{Style.RESET_ALL}")
        print(f"  • Total time: {results['decryption_total_time']:.3f} seconds")
        print(f"  • Average time: {results['decryption_avg_time']*1000:.2f} ms")
        print(f"  • Throughput: {results['decryption_throughput']:.0f} chars/second")
    
    def demo(self) -> None:
        """Run interactive demonstration."""
        print(f"\n{Fore.MAGENTA}{'=' * 50}")
        print(f"{Fore.MAGENTA}MSE INTERACTIVE DEMO")
        print(f"{Fore.MAGENTA}{'=' * 50}\n")
        
        # Sample texts
        samples = [
            "The quick brown fox jumps over the lazy dog.",
            "Security through obscurity is not enough!",
            "Multiple Substitution Encryption v29.0",
            "Hello, World! This is MSE encryption.",
            "Testing special characters: @#$%^&*()!"
        ]
        
        import random
        text = random.choice(samples)
        
        print(f"{Fore.YELLOW}Sample text:{Style.RESET_ALL} {text}\n")
        
        # Create MSE instance
        mse = MSE()
        
        # Encrypt
        print(f"{Fore.CYAN}Encrypting...{Style.RESET_ALL}")
        encrypted = mse.encrypt(text)
        print(f"{Fore.GREEN}Encrypted:{Style.RESET_ALL} {encrypted}\n")
        
        # Decrypt
        print(f"{Fore.CYAN}Decrypting...{Style.RESET_ALL}")
        decrypted = mse.decrypt(encrypted)
        print(f"{Fore.GREEN}Decrypted:{Style.RESET_ALL} {decrypted}\n")
        
        # Verify
        if text == decrypted:
            print(f"{Fore.GREEN}✓ Encryption/Decryption successful!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Encryption/Decryption failed!{Style.RESET_ALL}")
        
        # Show stats
        print(f"\n{Fore.YELLOW}Statistics:{Style.RESET_ALL}")
        print(f"  • Original length: {len(text)} characters")
        print(f"  • Encrypted length: {len(encrypted)} characters")
        print(f"  • Expansion ratio: {len(encrypted)/len(text):.2f}x")


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="MSE - Multiple Substitution Encryption System v29.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  mse_cli encrypt -t "Hello World" -o encrypted.txt
  mse_cli decrypt -f encrypted.txt
  mse_cli generate-config -o my_config.json
  mse_cli analyze -c my_config.json
  mse_cli benchmark -n 1000
  mse_cli demo
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt text or file')
    encrypt_group = encrypt_parser.add_mutually_exclusive_group(required=True)
    encrypt_group.add_argument('-t', '--text', help='Text to encrypt')
    encrypt_group.add_argument('-f', '--file', help='File to encrypt')
    encrypt_parser.add_argument('-o', '--output', help='Output file')
    encrypt_parser.add_argument('-c', '--config', help='Configuration file')
    encrypt_parser.add_argument('-s', '--stats', action='store_true', help='Show statistics')
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt text or file')
    decrypt_group = decrypt_parser.add_mutually_exclusive_group(required=True)
    decrypt_group.add_argument('-t', '--text', help='Text to decrypt')
    decrypt_group.add_argument('-f', '--file', help='File to decrypt')
    decrypt_parser.add_argument('-o', '--output', help='Output file')
    decrypt_parser.add_argument('-c', '--config', help='Configuration file')
    
    # Generate config command
    genconfig_parser = subparsers.add_parser('generate-config', help='Generate random configuration')
    genconfig_parser.add_argument('-o', '--output', default='configs/setting.json', help='Output file')
    
    # Generate database command
    gendb_parser = subparsers.add_parser('generate-db', help='Generate character database')
    gendb_parser.add_argument('-o', '--output', required=True, help='Output file')
    gendb_parser.add_argument('-l', '--length', type=int, default=3000, help='Database length')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze encryption strength')
    analyze_parser.add_argument('-c', '--config', help='Configuration file to analyze')
    
    # Benchmark command
    bench_parser = subparsers.add_parser('benchmark', help='Run performance benchmark')
    bench_parser.add_argument('-t', '--text', help='Custom text to benchmark')
    bench_parser.add_argument('-n', '--iterations', type=int, default=100, help='Number of iterations')
    bench_parser.add_argument('-c', '--config', help='Configuration file')
    
    # Demo command
    demo_parser = subparsers.add_parser('demo', help='Run interactive demo')
    
    # Reset command
    reset_parser = subparsers.add_parser('reset', help='Reset MSE system')
    reset_parser.add_argument('--full', action='store_true', help='Perform full system reset')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    cli = MSECLI()
    
    try:
        if args.command == 'encrypt':
            if args.text:
                cli.encrypt_text(args.text, args.config, args.output, args.stats)
            else:
                cli.encrypt_file(args.file, args.output, args.config)
        
        elif args.command == 'decrypt':
            if args.text:
                cli.decrypt_text(args.text, args.config, args.output)
            else:
                cli.decrypt_file(args.file, args.output, args.config)
        
        elif args.command == 'generate-config':
            cli.generate_config(args.output)
        
        elif args.command == 'generate-db':
            cli.generate_database(args.output, args.length)
        
        elif args.command == 'analyze':
            cli.analyze_strength(args.config)
        
        elif args.command == 'benchmark':
            cli.benchmark(args.text, args.iterations, args.config)
        
        elif args.command == 'demo':
            cli.demo()
        
        elif args.command == 'reset':
            cli.tools.reset_system(args.full)
            print(f"{Fore.GREEN}✓ System reset completed{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
