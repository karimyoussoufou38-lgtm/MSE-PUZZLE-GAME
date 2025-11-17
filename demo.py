#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MSE Demo - Interactive demonstration of MSE encryption system
Version: 29.0.0
"""

import os
import sys
import time
from colorama import init, Fore, Style, Back

# Initialize colorama
init(autoreset=True)

# Import MSE modules
from mse_core import MSE, MSEConfig
from mse_tools import MSETools, PerformanceOptimizer


class MSEDemo:
    """Interactive MSE demonstration."""
    
    def __init__(self):
        self.mse = MSE()
        self.tools = MSETools()
        
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print MSE banner."""
        banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════╗
║                                                                       ║
║  {Fore.YELLOW}███╗   ███╗  ███████╗ ███████╗   {Fore.GREEN}██╗   ██╗██████╗  █████╗{Fore.CYAN}         ║
║  {Fore.YELLOW}████╗ ████║ ██╔════╝ ██╔════╝   {Fore.GREEN}██║   ██║╚════██╗██╔══██╗{Fore.CYAN}        ║
║  {Fore.YELLOW}██╔████╔██║ ███████╗ █████╗     {Fore.GREEN}██║   ██║ █████╔╝╚██████║{Fore.CYAN}        ║
║  {Fore.YELLOW}██║╚██╔╝██║ ╚════██║ ██╔══╝     {Fore.GREEN}╚██╗ ██╔╝██╔═══╝  ╚═══██║{Fore.CYAN}        ║
║  {Fore.YELLOW}██║ ╚═╝ ██║ ███████║ ███████╗   {Fore.GREEN} ╚████╔╝ ███████╗ █████╔╝{Fore.CYAN}        ║
║  {Fore.YELLOW}╚═╝     ╚═╝ ╚══════╝ ╚══════╝   {Fore.GREEN}  ╚═══╝  ╚══════╝ ╚════╝{Fore.CYAN}         ║
║                                                                       ║
║        {Fore.WHITE}Multiple Substitution Encryption System - Version 29.0{Fore.CYAN}        ║
║                  {Fore.WHITE}Advanced Text Encryption Framework{Fore.CYAN}                  ║
╚═══════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def animated_text(self, text, delay=0.02):
        """Print text with typing animation."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def demo_basic_encryption(self):
        """Demonstrate basic encryption/decryption."""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Fore.CYAN}═══ BASIC ENCRYPTION DEMO ═══{Style.RESET_ALL}\n")
        
        # Sample texts
        samples = [
            "The quick brown fox jumps over the lazy dog",
            "Hello, World! Welcome to MSE v29.0",
            "Security through multiple substitution layers",
            "🔐 Encryption with special characters! @#$%",
        ]
        
        for i, text in enumerate(samples, 1):
            print(f"\n{Fore.YELLOW}Example {i}:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Original:{Style.RESET_ALL} {text}")
            
            # Encrypt
            encrypted = self.mse.encrypt(text)
            print(f"{Fore.GREEN}Encrypted:{Style.RESET_ALL} {encrypted[:80]}{'...' if len(encrypted) > 80 else ''}")
            
            # Decrypt
            decrypted = self.mse.decrypt(encrypted)
            print(f"{Fore.CYAN}Decrypted:{Style.RESET_ALL} {decrypted}")
            
            # Verify
            if text == decrypted:
                print(f"{Fore.GREEN}✓ Success!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ Failed!{Style.RESET_ALL}")
            
            time.sleep(1)
    
    def demo_security_analysis(self):
        """Demonstrate security analysis."""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Fore.CYAN}═══ SECURITY ANALYSIS DEMO ═══{Style.RESET_ALL}\n")
        
        # Generate different configurations
        configs = [
            ("Weak Security", {
                "cipher": "ascii_lowercase",
                "cipher_punctuation": "False",
                "cipher_digits": "False",
                "cipher_accent": "False",
                "key_number": [100, 200],
                "charac_len": [2, 3],
            }),
            ("Medium Security", {
                "cipher": "ascii_letters",
                "cipher_punctuation": "True",
                "cipher_digits": "False",
                "cipher_accent": "False",
                "key_number": [1000, 1500],
                "charac_len": [4, 5],
            }),
            ("Strong Security", {
                "cipher": "ascii_letters",
                "cipher_punctuation": "True",
                "cipher_digits": "True",
                "cipher_accent": "True",
                "key_number": [3000, 4000],
                "charac_len": [6, 8],
            }),
        ]
        
        for name, config_data in configs:
            print(f"\n{Fore.YELLOW}Configuration: {name}{Style.RESET_ALL}")
            
            # Create temporary config
            temp_config = config_data.copy()
            temp_config.update({
                "len_special_charac": [3, 4],
                "len_charac_group_b": [8, 11],
                "mini_add_group_b_charac": 7,
                "max_add_group_b_charac": 9,
                "substitue_with": "configs/all.txt",
                "special_charac": "easintrluodchEASINTRLUODCH0123456789!#$%&'()*+,-./:;<=>?@[]"
            })
            
            # Analyze
            import json
            with open("temp_config.json", "w") as f:
                json.dump(temp_config, f)
            
            analysis = self.tools.analyze_encryption_strength("temp_config.json")
            
            # Display results
            score = analysis['strength_score']
            if score >= 80:
                color = Fore.GREEN
                rating = "EXCELLENT"
            elif score >= 60:
                color = Fore.YELLOW
                rating = "GOOD"
            elif score >= 40:
                color = Fore.YELLOW
                rating = "MODERATE"
            else:
                color = Fore.RED
                rating = "WEAK"
            
            print(f"  Strength Score: {color}{score:.1f}/100 ({rating}){Style.RESET_ALL}")
            print(f"  Character Space: {analysis['metrics']['character_space']} characters")
            print(f"  Key Space: {analysis['metrics']['key_space_bits']:.1f} bits")
            print(f"  Number of Keys: {analysis['metrics']['number_of_keys']:.0f}")
            
            time.sleep(1)
        
        # Cleanup
        if os.path.exists("temp_config.json"):
            os.remove("temp_config.json")
    
    def demo_performance(self):
        """Demonstrate performance benchmarking."""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Fore.CYAN}═══ PERFORMANCE BENCHMARK DEMO ═══{Style.RESET_ALL}\n")
        
        optimizer = PerformanceOptimizer()
        
        # Test different text sizes
        text_sizes = [
            ("Small (100 chars)", "A" * 100),
            ("Medium (1KB)", "The quick brown fox jumps over the lazy dog. " * 22),
            ("Large (10KB)", "Lorem ipsum dolor sit amet. " * 357),
        ]
        
        for name, text in text_sizes:
            print(f"\n{Fore.YELLOW}Testing: {name}{Style.RESET_ALL}")
            print(f"Text length: {len(text)} characters")
            
            # Run benchmark
            results = optimizer.benchmark_encryption(self.mse, text, iterations=50)
            
            print(f"\n{Fore.GREEN}Encryption Performance:{Style.RESET_ALL}")
            print(f"  • Average time: {results['encryption_avg_time']*1000:.2f} ms")
            print(f"  • Throughput: {results['encryption_throughput']:.0f} chars/second")
            
            print(f"\n{Fore.CYAN}Decryption Performance:{Style.RESET_ALL}")
            print(f"  • Average time: {results['decryption_avg_time']*1000:.2f} ms")
            print(f"  • Throughput: {results['decryption_throughput']:.0f} chars/second")
            
            time.sleep(1)
    
    def demo_interactive(self):
        """Interactive encryption/decryption demo."""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Fore.CYAN}═══ INTERACTIVE ENCRYPTION ═══{Style.RESET_ALL}\n")
        
        while True:
            print(f"\n{Fore.YELLOW}Options:{Style.RESET_ALL}")
            print("1. Encrypt custom text")
            print("2. Decrypt text")
            print("3. Generate random text and encrypt")
            print("4. Back to main menu")
            
            choice = input(f"\n{Fore.GREEN}Enter choice (1-4): {Style.RESET_ALL}")
            
            if choice == "1":
                text = input(f"\n{Fore.CYAN}Enter text to encrypt: {Style.RESET_ALL}")
                if text:
                    encrypted = self.mse.encrypt(text)
                    print(f"\n{Fore.GREEN}Encrypted result:{Style.RESET_ALL}")
                    print(encrypted)
                    print(f"\n{Fore.YELLOW}Statistics:{Style.RESET_ALL}")
                    print(f"  • Original length: {len(text)} chars")
                    print(f"  • Encrypted length: {len(encrypted)} chars")
                    print(f"  • Expansion ratio: {len(encrypted)/len(text):.2f}x")
            
            elif choice == "2":
                text = input(f"\n{Fore.CYAN}Enter text to decrypt: {Style.RESET_ALL}")
                if text:
                    try:
                        decrypted = self.mse.decrypt(text)
                        print(f"\n{Fore.GREEN}Decrypted result:{Style.RESET_ALL}")
                        print(decrypted)
                    except Exception as e:
                        print(f"\n{Fore.RED}Decryption failed: {e}{Style.RESET_ALL}")
            
            elif choice == "3":
                import random
                import string
                
                length = random.randint(50, 200)
                text = ''.join(random.choices(
                    string.ascii_letters + string.digits + string.punctuation + ' ',
                    k=length
                ))
                
                print(f"\n{Fore.YELLOW}Generated text:{Style.RESET_ALL}")
                print(text)
                
                encrypted = self.mse.encrypt(text)
                print(f"\n{Fore.GREEN}Encrypted:{Style.RESET_ALL}")
                print(encrypted[:100] + "..." if len(encrypted) > 100 else encrypted)
                
                decrypted = self.mse.decrypt(encrypted)
                if text == decrypted:
                    print(f"\n{Fore.GREEN}✓ Verification successful!{Style.RESET_ALL}")
                else:
                    print(f"\n{Fore.RED}✗ Verification failed!{Style.RESET_ALL}")
            
            elif choice == "4":
                break
            
            else:
                print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
    
    def run(self):
        """Run the main demo menu."""
        while True:
            self.clear_screen()
            self.print_banner()
            
            print(f"\n{Fore.CYAN}═══ MAIN MENU ═══{Style.RESET_ALL}\n")
            print("1. Basic Encryption Demo")
            print("2. Security Analysis Demo")
            print("3. Performance Benchmark Demo")
            print("4. Interactive Encryption")
            print("5. Configuration Generator")
            print("6. System Information")
            print("7. Exit")
            
            choice = input(f"\n{Fore.GREEN}Enter choice (1-7): {Style.RESET_ALL}")
            
            if choice == "1":
                self.demo_basic_encryption()
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == "2":
                self.demo_security_analysis()
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == "3":
                self.demo_performance()
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == "4":
                self.demo_interactive()
            
            elif choice == "5":
                self.clear_screen()
                self.print_banner()
                print(f"\n{Fore.CYAN}═══ CONFIGURATION GENERATOR ═══{Style.RESET_ALL}\n")
                
                config = self.tools.generate_random_config("demo_config.json")
                print(f"{Fore.GREEN}Generated configuration:{Style.RESET_ALL}")
                
                import json
                print(json.dumps(config, indent=2))
                
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == "6":
                self.clear_screen()
                self.print_banner()
                print(f"\n{Fore.CYAN}═══ SYSTEM INFORMATION ═══{Style.RESET_ALL}\n")
                
                print(f"{Fore.YELLOW}MSE System Information:{Style.RESET_ALL}")
                print(f"  • Version: 29.0.0")
                print(f"  • Python: {sys.version.split()[0]}")
                print(f"  • Platform: {sys.platform}")
                print(f"  • Key Library Size: {len(self.mse.key_manager.keys)} keys")
                print(f"  • Character Space: {len(self.mse.char_set.substitution_chars)} chars")
                print(f"  • System Hash: {self.mse.get_hash()[:32]}...")
                
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == "7":
                print(f"\n{Fore.GREEN}Thank you for using MSE v29.0!{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Goodbye!{Style.RESET_ALL}\n")
                break
            
            else:
                print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
                time.sleep(1)


def main():
    """Main entry point."""
    try:
        demo = MSEDemo()
        demo.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Demo interrupted by user.{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
