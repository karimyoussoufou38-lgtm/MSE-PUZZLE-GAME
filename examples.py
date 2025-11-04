#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE Example Program
Demonstrates various uses of the encryption system
"""

from MSE import mse_cipher, mse_decipher, get_encryption_stats, verify_encryption
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def example_1_basic_usage():
    """Example 1: Basic encryption and decryption"""
    print(Fore.CYAN + "="*70)
    print("EXAMPLE 1: Basic Encryption & Decryption")
    print("="*70 + Style.RESET_ALL)
    
    message = "Hello, this is a secret message!"
    print(f"\n{Fore.GREEN}Original message:{Style.RESET_ALL}")
    print(f"  {message}")
    
    # Encrypt
    encrypted = mse_cipher(message, auto_copy=False)
    print(f"\n{Fore.RED}Encrypted message:{Style.RESET_ALL}")
    print(f"  {encrypted[:100]}..." if len(encrypted) > 100 else f"  {encrypted}")
    
    # Decrypt
    decrypted = mse_decipher(encrypted, auto_copy=False)
    print(f"\n{Fore.GREEN}Decrypted message:{Style.RESET_ALL}")
    print(f"  {decrypted}")
    
    # Verify
    print(f"\n{Fore.YELLOW}Verification:{Style.RESET_ALL}")
    print(f"  Match: {message == decrypted} ✓" if message == decrypted else "  Match: False ✗")


def example_2_escape_room():
    """Example 2: Escape room puzzle creation"""
    print(f"\n\n{Fore.CYAN}{'='*70}")
    print("EXAMPLE 2: Escape Room Puzzle")
    print(f"{'='*70}{Style.RESET_ALL}")
    
    clues = [
        "First clue: Search the bookshelf on the left wall",
        "Second clue: Look behind the painting of the ocean",
        "Third clue: Check inside the blue vase on the mantle",
        "Final code: The safe combination is 8-2-4-7"
    ]
    
    print(f"\n{Fore.GREEN}Creating encrypted clues for escape room:{Style.RESET_ALL}\n")
    
    encrypted_clues = []
    for i, clue in enumerate(clues, 1):
        encrypted = mse_cipher(clue, auto_copy=False)
        encrypted_clues.append(encrypted)
        print(f"{Fore.YELLOW}Clue {i}:{Style.RESET_ALL}")
        print(f"  Original: {clue}")
        print(f"  Encrypted: {encrypted[:80]}...")
        print()


def example_3_statistics():
    """Example 3: Encryption statistics analysis"""
    print(f"\n\n{Fore.CYAN}{'='*70}")
    print("EXAMPLE 3: Encryption Statistics")
    print(f"{'='*70}{Style.RESET_ALL}")
    
    messages = [
        "Hi",
        "Hello World",
        "The quick brown fox jumps over the lazy dog",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 3
    ]
    
    print(f"\n{Fore.GREEN}Analyzing expansion ratios:{Style.RESET_ALL}\n")
    
    for msg in messages:
        encrypted = mse_cipher(msg, auto_copy=False)
        stats = get_encryption_stats(msg, encrypted)
        
        print(f"{Fore.YELLOW}Message:{Style.RESET_ALL} {msg[:40]}...")
        print(f"  Original length:  {stats['original_length']:>5} chars")
        print(f"  Encrypted length: {stats['encrypted_length']:>5} chars")
        print(f"  Expansion ratio:  {stats['expansion_ratio']:>5.2f}x")
        print(f"  Unique chars (original):  {stats['original_unique_chars']:>3}")
        print(f"  Unique chars (encrypted): {stats['encrypted_unique_chars']:>3}")
        print()


def example_4_multilingual():
    """Example 4: Multilingual encryption"""
    print(f"\n\n{Fore.CYAN}{'='*70}")
    print("EXAMPLE 4: Multilingual Support")
    print(f"{'='*70}{Style.RESET_ALL}")
    
    messages = {
        "English": "The treasure is hidden in the garden",
        "French": "Le trésor est caché dans le jardin",
        "Spanish": "El tesoro está escondido en el jardín",
        "German": "Der Schatz ist im Garten versteckt"
    }
    
    print(f"\n{Fore.GREEN}Testing different languages:{Style.RESET_ALL}\n")
    
    for lang, msg in messages.items():
        encrypted = mse_cipher(msg, auto_copy=False)
        decrypted = mse_decipher(encrypted, auto_copy=False)
        match = "✓" if msg == decrypted else "✗"
        
        print(f"{Fore.YELLOW}{lang}:{Style.RESET_ALL}")
        print(f"  Original:  {msg}")
        print(f"  Encrypted: {encrypted[:60]}...")
        print(f"  Decrypted: {decrypted}")
        print(f"  Status:    {match}")
        print()


def example_5_puzzle_difficulty():
    """Example 5: Adjustable puzzle difficulty"""
    print(f"\n\n{Fore.CYAN}{'='*70}")
    print("EXAMPLE 5: Puzzle Difficulty Levels")
    print(f"{'='*70}{Style.RESET_ALL}")
    
    base_message = "Find the hidden key"
    
    difficulties = [
        ("Easy (short)", base_message),
        ("Medium (longer)", base_message + " in the old mansion by the lake"),
        ("Hard (very long)", base_message + " in the old mansion by the lake where the treasure hunter once lived in 1847")
    ]
    
    print(f"\n{Fore.GREEN}Same message with increasing difficulty:{Style.RESET_ALL}\n")
    
    for difficulty, msg in difficulties:
        encrypted = mse_cipher(msg, auto_copy=False)
        
        print(f"{Fore.YELLOW}{difficulty}:{Style.RESET_ALL}")
        print(f"  Length: {len(msg)} → {len(encrypted)} chars")
        print(f"  Preview: {encrypted[:70]}...")
        print()


def example_6_verification():
    """Example 6: System verification"""
    print(f"\n\n{Fore.CYAN}{'='*70}")
    print("EXAMPLE 6: Encryption System Verification")
    print(f"{'='*70}{Style.RESET_ALL}")
    
    test_messages = [
        "Test 1",
        "Test with numbers 123",
        "Test with symbols !@#$%",
        "Test with accents: àâéèêëîïôùûüç",
        "Long test message " * 20
    ]
    
    print(f"\n{Fore.GREEN}Running verification tests:{Style.RESET_ALL}\n")
    
    passed = 0
    failed = 0
    
    for i, msg in enumerate(test_messages, 1):
        result = verify_encryption(msg)
        status = f"{Fore.GREEN}PASS ✓{Style.RESET_ALL}" if result else f"{Fore.RED}FAIL ✗{Style.RESET_ALL}"
        
        if result:
            passed += 1
        else:
            failed += 1
        
        print(f"  Test {i}: {status} - {msg[:40]}...")
    
    print(f"\n{Fore.YELLOW}Results:{Style.RESET_ALL}")
    print(f"  Passed: {passed}/{len(test_messages)}")
    print(f"  Failed: {failed}/{len(test_messages)}")
    print(f"  Success rate: {(passed/len(test_messages)*100):.1f}%")


def main():
    """Run all examples"""
    print(f"\n{Fore.MAGENTA}{'='*70}")
    print(f"{'='*70}")
    print("   MSE (Multiple Substitution Encryption) - Examples")
    print(f"{'='*70}")
    print(f"{'='*70}{Style.RESET_ALL}\n")
    
    examples = [
        ("Basic Usage", example_1_basic_usage),
        ("Escape Room", example_2_escape_room),
        ("Statistics", example_3_statistics),
        ("Multilingual", example_4_multilingual),
        ("Difficulty Levels", example_5_puzzle_difficulty),
        ("Verification", example_6_verification)
    ]
    
    print("Available examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    print(f"  {len(examples)+1}. Run all examples")
    print(f"  0. Exit")
    
    try:
        choice = input(f"\n{Fore.GREEN}Select an example (0-{len(examples)+1}): {Style.RESET_ALL}")
        choice = int(choice)
        
        if choice == 0:
            print("Goodbye!")
            return
        elif choice == len(examples) + 1:
            for _, func in examples:
                func()
        elif 1 <= choice <= len(examples):
            examples[choice-1][1]()
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Interrupted by user{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
