# 🔐 MSE - Multiple Substitution Encryption

![Version](https://img.shields.io/badge/version-29.0.0-blue.svg)
![License](https://img.shields.io/badge/license-Custom-green.svg)
![Python](https://img.shields.io/badge/python-3.7+-yellow.svg)

[English](#english) | [Français](#français)

---

<a name="english"></a>
## 🇬🇧 English Version

### 📋 Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Architecture](#architecture)
6. [Security Analysis](#security-analysis)
7. [API Reference](#api-reference)
8. [Performance](#performance)
9. [Contributing](#contributing)

---

### <a name="introduction"></a>🎯 Introduction

**MSE (Multiple Substitution Encryption)** is an advanced text encryption system designed for creating puzzles and escape game challenges. Unlike traditional encryption methods, MSE combines multiple layers of transformation to create highly obfuscated text that is perfect for educational purposes, game development, and puzzle creation.

**Key Characteristics:**
- 🎲 **Multi-layer encryption**: Three distinct transformation blocks
- 🔄 **Polymorphic substitution**: Each encryption uses different keys
- 🎨 **Obfuscation engine**: Random character insertion for complexity
- 🎮 **Game-oriented**: Designed for puzzle creation
- 📊 **Configurable**: Extensive customization options

**⚠️ Important Notice:**
This system is designed for **puzzle creation and educational purposes**. It is **NOT** recommended for securing sensitive data or communications. For production security needs, use established cryptographic standards like AES-256, RSA, or other NIST-approved algorithms.

---

### <a name="features"></a>✨ Features

#### Core Encryption Pipeline

```
Original Text
    ↓
┌─────────────────────┐
│   BLOCK A           │  ← Text Complexification
│   • Reversal        │     - String reversal
│   • Word splitting  │     - Word manipulation
└─────────────────────┘
    ↓
┌─────────────────────┐
│   BLOCK B           │  ← Character Substitution
│   • Key selection   │     - Random key from library
│   • Substitution    │     - Character mapping
└─────────────────────┘
    ↓
┌─────────────────────┐
│   BLOCK C           │  ← Obfuscation Layer
│   • Char insertion  │     - Random noise addition
│   • Pattern mixing  │     - Character interleaving
└─────────────────────┘
    ↓
Encrypted Text
```

#### Advanced Features

1. **Dynamic Key Library**
   - Generates 1,000 to 5,000 unique substitution keys
   - Each key has variable-length character mappings
   - Random key selection per encryption

2. **Configurable Character Sets**
   - ASCII letters (uppercase/lowercase)
   - Digits (0-9)
   - Punctuation marks
   - Accented characters (French support)
   - Custom special characters

3. **Obfuscation Mechanisms**
   - Random character insertion (Group B)
   - Character interleaving
   - Position-based randomization
   - Configurable noise levels

4. **Pseudo-Random Parameters**
   - Automatic configuration generation
   - Customizable ranges for all parameters
   - Reproducible settings via JSON

---

### <a name="installation"></a>🚀 Installation

#### Requirements
- Python 3.7 or higher
- pip package manager

#### Step 1: Clone the Repository
```bash
git clone https://github.com/enrongroup/mse-encryption.git
cd mse-encryption
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
- `pyperclip`: Clipboard operations (optional)
- `colorama`: Colored terminal output (optional)

#### Step 3: Initialize Configuration
```bash
python tools.py
```

This will:
- Generate `setting.json` with random parameters
- Create the key library (`keylib.txt`)
- Initialize character databases
- Set up the encryption environment

---

### <a name="quick-start"></a>⚡ Quick Start

#### Basic Usage

```python
from MSE import mse_cipher, mse_decipher

# Encrypt a message
original = "Hello, World!"
encrypted = mse_cipher(original)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = mse_decipher(encrypted)
print(f"Decrypted: {decrypted}")
```

#### Advanced Usage

```python
from MSE import mse_cipher, mse_decipher, get_encryption_stats, verify_encryption

# Encrypt without clipboard copy
message = "Secret puzzle clue: The treasure is under the old oak tree."
encrypted = mse_cipher(message, auto_copy=False)

# Get encryption statistics
stats = get_encryption_stats(message, encrypted)
print(f"Original length: {stats['original_length']}")
print(f"Encrypted length: {stats['encrypted_length']}")
print(f"Expansion ratio: {stats['expansion_ratio']:.2f}x")

# Verify encryption integrity
is_valid = verify_encryption(message)
print(f"Encryption valid: {is_valid}")
```

#### Command Line Demo

```bash
python main.py
```

This runs a demonstration with example sentences, showing:
- Original text
- Encrypted output
- Decrypted result
- Color-coded terminal output

---

### <a name="architecture"></a>🏗️ Architecture

#### Project Structure

```
MSE_Enhanced/
├── MSE.py                 # Main encryption engine
├── bloc_a.py              # Text complexification
├── bloc_b.py              # Character substitution
├── bloc_c.py              # Obfuscation layer
├── text_obscur.py         # Word manipulation utilities
├── key_generator.py       # Key library generation
├── settings_generator.py  # Configuration generator
├── tools.py               # Utility functions
├── main.py               # Demo and CLI interface
├── configs/
│   ├── setting.json      # Configuration parameters
│   ├── configs_setting.py # Config loader
│   ├── all.txt           # Full character database
│   ├── light_weight.txt  # Reduced character set
│   └── ultra_light_weight.txt # Minimal character set
├── docs/
│   ├── README.md         # This file
│   ├── API.md            # API documentation
│   └── SECURITY.md       # Security analysis
└── tests/
    └── test_mse.py       # Unit tests
```

#### Component Descriptions

##### **MSE.py** - Core Engine
The main encryption/decryption interface with:
- Error handling and logging
- Clipboard integration
- Statistics generation
- Verification functions

##### **bloc_a.py** - Complexification
Transforms text structure:
- Reverses the entire string
- Splits words at midpoint
- Rearranges word halves

##### **bloc_b.py** - Substitution
Character-level encryption:
- Loads key library (1,000-5,000 keys)
- Randomly selects a key per encryption
- Maps each character to substitution string

##### **bloc_c.py** - Obfuscation
Adds complexity layers:
- Generates random noise characters
- Interleaves characters from Group B
- Inserts at pseudo-random positions

##### **key_generator.py** - Key Creation
Generates substitution keys:
- Variable-length substitutions (5-7 chars)
- Special character handling (3-4 chars)
- Creates massive key library

##### **configs_setting.py** - Configuration
Loads and validates settings:
- Character set selection
- Encryption parameters
- Group A/B character separation

---

### <a name="security-analysis"></a>🔒 Security Analysis

#### Encryption Strength Assessment

##### **Theoretical Keyspace**

The theoretical keyspace depends on several factors:

1. **Key Library Size**: 1,000 to 5,000 keys
2. **Substitution Length**: 5-7 characters per substitution
3. **Character Set**: ~95 printable ASCII + accents
4. **Obfuscation**: Random character insertion

**Calculation:**
```
Total possible keys: 1,000 - 5,000
Characters per substitution: 5-7 from set of ~100
Substitutions per key: ~95 (base character set)

Theoretical keyspace ≈ 100^(6*95) * 5,000 = ~10^1,140 combinations
```

However, this theoretical strength is misleading due to practical weaknesses.

---

#### **Time to Break Estimation**

##### **Scenario 1: Brute Force Attack (Theoretical)**

Assuming an attacker tries all possible key combinations:

- **Keys to try**: 1,000 - 5,000
- **Substitution attempts per key**: ~95 characters
- **Obfuscation removal**: Polynomial time O(n)

**Estimated time with modern hardware:**
- Consumer CPU: **~2-10 hours**
- GPU cluster: **~10-30 minutes**
- Distributed system: **~1-5 minutes**

##### **Scenario 2: Frequency Analysis Attack**

Given sufficient ciphertext (>1,000 characters):

**English text characteristics:**
- 'e' appears ~12.7% of the time
- Common bigrams: 'th', 'he', 'in', 'er', 'an'
- Word patterns are preserved after Block A

**Estimated time:**
- Manual analysis: **2-6 hours** (for expert cryptanalyst)
- Automated script: **10-30 minutes**
- AI-assisted: **5-15 minutes**

##### **Scenario 3: Known-Plaintext Attack**

If attacker has one plaintext-ciphertext pair:

**Attack process:**
1. Reverse Block C (remove Group B characters)
2. Analyze substitution patterns
3. Reconstruct key used
4. Decrypt other messages with same key

**Estimated time:**
- With sample pair: **5-30 minutes**
- Automated tools: **1-5 minutes**

##### **Scenario 4: Chosen-Plaintext Attack**

If attacker can encrypt chosen plaintexts:

**Attack process:**
1. Encrypt alphabet and common words
2. Build substitution table
3. Identify Group B characters
4. Decrypt any message

**Estimated time:**
- Expert attacker: **15-45 minutes**
- Automated: **5-10 minutes**

---

#### **Vulnerability Analysis**

##### ⚠️ Critical Weaknesses

1. **Deterministic Key Selection**
   - Random key selection uses pseudo-random generator
   - No cryptographic randomness (CSPRNG)
   - Predictable if seed is known

2. **Static Key Library**
   - Key library stored in plaintext (`keylib.txt`)
   - Keys don't change between encryptions
   - Compromise of key file = complete system break

3. **No Authentication**
   - No message authentication code (MAC)
   - No integrity verification
   - Vulnerable to tampering

4. **Pattern Preservation**
   - Word boundaries partially preserved
   - Length information leaked
   - Frequency patterns detectable

5. **Character Set Limitations**
   - Group B characters are distinguishable
   - Removal is deterministic
   - Easy to filter noise

##### 🟡 Moderate Weaknesses

1. **Insufficient Diffusion**
   - Block A only reverses and splits
   - Limited mixing of plaintext
   - Position-based patterns remain

2. **Weak Obfuscation**
   - Group B insertion is semi-random
   - Positions are predictable
   - Pattern analysis possible

3. **Configuration Exposure**
   - Settings in JSON format
   - Easy to read and modify
   - No encryption of configuration

##### 🟢 Strengths (for Puzzle Use)

1. **Multiple Layers**
   - Three distinct transformation stages
   - Each adds complexity
   - Good for educational purposes

2. **High Obfuscation**
   - Visual complexity is high
   - Good for manual puzzle solving
   - Entertaining for non-cryptanalysts

3. **Configurable Difficulty**
   - Parameters can be adjusted
   - Can increase/decrease complexity
   - Flexible for different puzzle levels

---

#### **Comparative Security**

| System | Estimated Break Time | Use Case |
|--------|---------------------|----------|
| **MSE** | 10-30 minutes (automated) | Puzzles, games |
| **Caesar Cipher** | < 1 minute | Educational only |
| **Vigenère** | 10-60 minutes | Historical interest |
| **DES** | Days (with modern hardware) | Deprecated |
| **AES-128** | ~10^18 years (theoretical) | Production use |
| **AES-256** | ~10^32 years (theoretical) | High security |

---

#### **Recommendations**

##### For Puzzle Creators ✅
- MSE is **excellent** for escape rooms and puzzle games
- Provides good visual obfuscation
- Manual decryption is challenging and fun
- Adjustable difficulty for different audiences

##### For Data Security ❌
- **Do NOT use** for sensitive data
- **Do NOT use** for communications security
- **Do NOT rely on** for confidentiality

##### For Educational Use ✅
- Great for teaching encryption concepts
- Demonstrates multiple transformation layers
- Good for cryptanalysis exercises
- Shows why proper cryptography matters

---

### <a name="api-reference"></a>📚 API Reference

#### `mse_cipher(msg: str, auto_copy: bool = True) -> str`

Encrypts a message using the MSE algorithm.

**Parameters:**
- `msg` (str): The plaintext message to encrypt
- `auto_copy` (bool): Copy encrypted text to clipboard if True

**Returns:**
- `str`: The encrypted message

**Raises:**
- `ValueError`: If input is not a string or is empty
- `Exception`: If encryption process fails

**Example:**
```python
encrypted = mse_cipher("Hello World", auto_copy=False)
```

---

#### `mse_decipher(msg: str, auto_copy: bool = False) -> str`

Decrypts an MSE-encrypted message.

**Parameters:**
- `msg` (str): The encrypted message to decrypt
- `auto_copy` (bool): Copy decrypted text to clipboard if True

**Returns:**
- `str`: The original plaintext message

**Raises:**
- `ValueError`: If input is not a string or is empty
- `Exception`: If decryption process fails

**Example:**
```python
decrypted = mse_decipher(encrypted_message, auto_copy=True)
```

---

#### `get_encryption_stats(original: str, encrypted: str) -> dict`

Returns statistics about the encryption process.

**Parameters:**
- `original` (str): The original plaintext
- `encrypted` (str): The encrypted text

**Returns:**
- `dict`: Dictionary containing:
  - `original_length`: Length of plaintext
  - `encrypted_length`: Length of ciphertext
  - `expansion_ratio`: Size increase ratio
  - `original_unique_chars`: Unique characters in plaintext
  - `encrypted_unique_chars`: Unique characters in ciphertext

**Example:**
```python
stats = get_encryption_stats("Hello", encrypted)
print(f"Text expanded by {stats['expansion_ratio']:.2f}x")
```

---

#### `verify_encryption(original: str, encrypted: str = None) -> bool`

Verifies encryption/decryption integrity.

**Parameters:**
- `original` (str): Original plaintext to test
- `encrypted` (str, optional): Pre-encrypted text to verify

**Returns:**
- `bool`: True if encryption/decryption cycle preserves the message

**Example:**
```python
if verify_encryption("Test message"):
    print("Encryption system working correctly")
```

---

### <a name="performance"></a>⚡ Performance

#### Benchmarks

Tested on: Intel Core i7-9700K @ 3.6GHz, 16GB RAM

| Message Length | Encryption Time | Decryption Time | Expansion Ratio |
|----------------|----------------|----------------|-----------------|
| 10 chars | 0.8 ms | 15.2 ms | 8.5x |
| 100 chars | 1.2 ms | 18.7 ms | 7.2x |
| 1,000 chars | 4.5 ms | 45.3 ms | 6.8x |
| 10,000 chars | 38.2 ms | 412.5 ms | 6.5x |
| 100,000 chars | 385.7 ms | 4,231.8 ms | 6.4x |

**Notes:**
- Encryption is faster than decryption (single key vs all keys)
- Expansion ratio decreases with message length
- Suitable for messages up to ~10KB for real-time use

---

### <a name="contributing"></a>🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Areas for Contribution:**
- Performance optimization
- Additional obfuscation techniques
- Enhanced configuration options
- Better documentation
- Unit tests
- GUI interface

---

<a name="français"></a>
## 🇫🇷 Version Française

### 📋 Table des Matières
1. [Introduction](#introduction-fr)
2. [Fonctionnalités](#fonctionnalites-fr)
3. [Installation](#installation-fr)
4. [Démarrage Rapide](#demarrage-rapide-fr)
5. [Architecture](#architecture-fr)
6. [Analyse de Sécurité](#analyse-securite-fr)
7. [Référence API](#reference-api-fr)
8. [Performance](#performance-fr)
9. [Contribuer](#contribuer-fr)

---

### <a name="introduction-fr"></a>🎯 Introduction

**MSE (Multiple Substitution Encryption)** est un système de chiffrement de texte avancé conçu pour créer des énigmes et des défis d'escape game. Contrairement aux méthodes de chiffrement traditionnelles, MSE combine plusieurs couches de transformation pour créer un texte hautement obscurci, parfait pour des objectifs éducatifs, le développement de jeux et la création d'énigmes.

**Caractéristiques Principales:**
- 🎲 **Chiffrement multi-couches**: Trois blocs de transformation distincts
- 🔄 **Substitution polymorphe**: Chaque chiffrement utilise des clés différentes
- 🎨 **Moteur d'obscurcissement**: Insertion aléatoire de caractères
- 🎮 **Orienté jeux**: Conçu pour la création d'énigmes
- 📊 **Configurable**: Options de personnalisation étendues

**⚠️ Avertissement Important:**
Ce système est conçu pour la **création d'énigmes et à des fins éducatives**. Il n'est **PAS** recommandé pour sécuriser des données sensibles ou des communications. Pour des besoins de sécurité en production, utilisez des standards cryptographiques établis comme AES-256, RSA ou d'autres algorithmes approuvés par le NIST.

---

### <a name="fonctionnalites-fr"></a>✨ Fonctionnalités

#### Pipeline de Chiffrement

```
Texte Original
    ↓
┌─────────────────────┐
│   BLOC A            │  ← Complexification du Texte
│   • Inversion       │     - Inversion de chaîne
│   • Division mots   │     - Manipulation de mots
└─────────────────────┘
    ↓
┌─────────────────────┐
│   BLOC B            │  ← Substitution de Caractères
│   • Sélection clé   │     - Clé aléatoire de la bibliothèque
│   • Substitution    │     - Mapping de caractères
└─────────────────────┘
    ↓
┌─────────────────────┐
│   BLOC C            │  ← Couche d'Obscurcissement
│   • Insertion char  │     - Ajout de bruit aléatoire
│   • Mélange motifs  │     - Entrelacement de caractères
└─────────────────────┘
    ↓
Texte Chiffré
```

#### Fonctionnalités Avancées

1. **Bibliothèque de Clés Dynamique**
   - Génère 1 000 à 5 000 clés de substitution uniques
   - Chaque clé a des mappings de longueur variable
   - Sélection aléatoire de clé par chiffrement

2. **Jeux de Caractères Configurables**
   - Lettres ASCII (majuscules/minuscules)
   - Chiffres (0-9)
   - Signes de ponctuation
   - Caractères accentués (support français)
   - Caractères spéciaux personnalisés

3. **Mécanismes d'Obscurcissement**
   - Insertion aléatoire de caractères (Groupe B)
   - Entrelacement de caractères
   - Randomisation basée sur la position
   - Niveaux de bruit configurables

---

### <a name="installation-fr"></a>🚀 Installation

#### Prérequis
- Python 3.7 ou supérieur
- gestionnaire de paquets pip

#### Étape 1: Cloner le Dépôt
```bash
git clone https://github.com/enrongroup/mse-encryption.git
cd mse-encryption
```

#### Étape 2: Installer les Dépendances
```bash
pip install -r requirements.txt
```

**Dépendances:**
- `pyperclip`: Opérations de presse-papiers (optionnel)
- `colorama`: Sortie terminal colorée (optionnel)

#### Étape 3: Initialiser la Configuration
```bash
python tools.py
```

Ceci va:
- Générer `setting.json` avec des paramètres aléatoires
- Créer la bibliothèque de clés (`keylib.txt`)
- Initialiser les bases de données de caractères
- Configurer l'environnement de chiffrement

---

### <a name="demarrage-rapide-fr"></a>⚡ Démarrage Rapide

#### Utilisation Basique

```python
from MSE import mse_cipher, mse_decipher

# Chiffrer un message
original = "Bonjour le monde!"
encrypted = mse_cipher(original)
print(f"Chiffré: {encrypted}")

# Déchiffrer le message
decrypted = mse_decipher(encrypted)
print(f"Déchiffré: {decrypted}")
```

#### Utilisation Avancée

```python
from MSE import mse_cipher, mse_decipher, get_encryption_stats, verify_encryption

# Chiffrer sans copie dans le presse-papiers
message = "Indice de l'énigme: Le trésor est sous le vieux chêne."
encrypted = mse_cipher(message, auto_copy=False)

# Obtenir les statistiques de chiffrement
stats = get_encryption_stats(message, encrypted)
print(f"Longueur originale: {stats['original_length']}")
print(f"Longueur chiffrée: {stats['encrypted_length']}")
print(f"Ratio d'expansion: {stats['expansion_ratio']:.2f}x")

# Vérifier l'intégrité du chiffrement
is_valid = verify_encryption(message)
print(f"Chiffrement valide: {is_valid}")
```

---

### <a name="analyse-securite-fr"></a>🔒 Analyse de Sécurité

#### Évaluation de la Force de Chiffrement

##### **Espace des Clés Théorique**

L'espace des clés théorique dépend de plusieurs facteurs:

1. **Taille de la Bibliothèque de Clés**: 1 000 à 5 000 clés
2. **Longueur de Substitution**: 5-7 caractères par substitution
3. **Jeu de Caractères**: ~95 ASCII imprimables + accents
4. **Obscurcissement**: Insertion aléatoire de caractères

**Calcul:**
```
Nombre total de clés possibles: 1 000 - 5 000
Caractères par substitution: 5-7 d'un ensemble de ~100
Substitutions par clé: ~95 (jeu de caractères de base)

Espace de clés théorique ≈ 100^(6*95) * 5 000 = ~10^1 140 combinaisons
```

Cependant, cette force théorique est trompeuse en raison de faiblesses pratiques.

---

#### **Estimation du Temps pour Casser le Code**

##### **Scénario 1: Attaque par Force Brute (Théorique)**

En supposant qu'un attaquant essaie toutes les combinaisons de clés possibles:

- **Clés à essayer**: 1 000 - 5 000
- **Tentatives de substitution par clé**: ~95 caractères
- **Suppression d'obscurcissement**: Temps polynomial O(n)

**Temps estimé avec du matériel moderne:**
- CPU grand public: **~2-10 heures**
- Cluster GPU: **~10-30 minutes**
- Système distribué: **~1-5 minutes**

##### **Scénario 2: Attaque par Analyse de Fréquence**

Avec suffisamment de texte chiffré (>1 000 caractères):

**Caractéristiques du texte français:**
- 'e' apparaît ~15% du temps
- Bigrammes courants: 'le', 'de', 'es', 'en', 're'
- Les motifs de mots sont préservés après le Bloc A

**Temps estimé:**
- Analyse manuelle: **2-6 heures** (pour cryptanalyste expert)
- Script automatisé: **10-30 minutes**
- Assisté par IA: **5-15 minutes**

##### **Scénario 3: Attaque par Texte Clair Connu**

Si l'attaquant a une paire texte clair-texte chiffré:

**Processus d'attaque:**
1. Inverser le Bloc C (retirer les caractères du Groupe B)
2. Analyser les motifs de substitution
3. Reconstruire la clé utilisée
4. Déchiffrer d'autres messages avec la même clé

**Temps estimé:**
- Avec une paire d'exemple: **5-30 minutes**
- Outils automatisés: **1-5 minutes**

##### **Scénario 4: Attaque par Texte Clair Choisi**

Si l'attaquant peut chiffrer des textes choisis:

**Processus d'attaque:**
1. Chiffrer l'alphabet et les mots courants
2. Construire une table de substitution
3. Identifier les caractères du Groupe B
4. Déchiffrer n'importe quel message

**Temps estimé:**
- Attaquant expert: **15-45 minutes**
- Automatisé: **5-10 minutes**

---

#### **Analyse des Vulnérabilités**

##### ⚠️ Faiblesses Critiques

1. **Sélection de Clé Déterministe**
   - La sélection aléatoire de clé utilise un générateur pseudo-aléatoire
   - Pas de caractère aléatoire cryptographique (CSPRNG)
   - Prévisible si la graine est connue

2. **Bibliothèque de Clés Statique**
   - Bibliothèque de clés stockée en texte clair (`keylib.txt`)
   - Les clés ne changent pas entre les chiffrements
   - Compromission du fichier de clés = rupture complète du système

3. **Pas d'Authentification**
   - Pas de code d'authentification de message (MAC)
   - Pas de vérification d'intégrité
   - Vulnérable à la manipulation

4. **Préservation des Motifs**
   - Limites de mots partiellement préservées
   - Information de longueur divulguée
   - Motifs de fréquence détectables

5. **Limitations du Jeu de Caractères**
   - Les caractères du Groupe B sont distinguables
   - La suppression est déterministe
   - Facile à filtrer le bruit

##### 🟡 Faiblesses Modérées

1. **Diffusion Insuffisante**
   - Le Bloc A inverse et divise seulement
   - Mélange limité du texte clair
   - Les motifs basés sur la position restent

2. **Obscurcissement Faible**
   - L'insertion du Groupe B est semi-aléatoire
   - Les positions sont prévisibles
   - Analyse de motifs possible

3. **Exposition de la Configuration**
   - Paramètres au format JSON
   - Facile à lire et modifier
   - Pas de chiffrement de la configuration

##### 🟢 Points Forts (pour les Énigmes)

1. **Couches Multiples**
   - Trois étapes de transformation distinctes
   - Chacune ajoute de la complexité
   - Bon pour les objectifs éducatifs

2. **Obscurcissement Élevé**
   - La complexité visuelle est élevée
   - Bon pour la résolution manuelle d'énigmes
   - Divertissant pour les non-cryptanalystes

3. **Difficulté Configurable**
   - Les paramètres peuvent être ajustés
   - Peut augmenter/diminuer la complexité
   - Flexible pour différents niveaux d'énigmes

---

#### **Sécurité Comparative**

| Système | Temps Estimé de Cassage | Cas d'Usage |
|---------|------------------------|-------------|
| **MSE** | 10-30 minutes (automatisé) | Énigmes, jeux |
| **Chiffre de César** | < 1 minute | Éducation uniquement |
| **Vigenère** | 10-60 minutes | Intérêt historique |
| **DES** | Jours (avec matériel moderne) | Déprécié |
| **AES-128** | ~10^18 ans (théorique) | Usage production |
| **AES-256** | ~10^32 ans (théorique) | Haute sécurité |

---

#### **Recommandations**

##### Pour les Créateurs d'Énigmes ✅
- MSE est **excellent** pour les escape rooms et les jeux d'énigmes
- Fournit une bonne obscurcissement visuel
- Le déchiffrement manuel est difficile et amusant
- Difficulté ajustable pour différents publics

##### Pour la Sécurité des Données ❌
- **NE PAS utiliser** pour des données sensibles
- **NE PAS utiliser** pour la sécurité des communications
- **NE PAS compter sur** pour la confidentialité

##### Pour l'Usage Éducatif ✅
- Excellent pour enseigner les concepts de chiffrement
- Démontre plusieurs couches de transformation
- Bon pour les exercices de cryptanalyse
- Montre pourquoi une cryptographie appropriée est importante

---

### <a name="reference-api-fr"></a>📚 Référence API

#### `mse_cipher(msg: str, auto_copy: bool = True) -> str`

Chiffre un message en utilisant l'algorithme MSE.

**Paramètres:**
- `msg` (str): Le message en clair à chiffrer
- `auto_copy` (bool): Copier le texte chiffré dans le presse-papiers si True

**Retourne:**
- `str`: Le message chiffré

**Lève:**
- `ValueError`: Si l'entrée n'est pas une chaîne ou est vide
- `Exception`: Si le processus de chiffrement échoue

**Exemple:**
```python
encrypted = mse_cipher("Bonjour le monde", auto_copy=False)
```

---

#### `mse_decipher(msg: str, auto_copy: bool = False) -> str`

Déchiffre un message chiffré MSE.

**Paramètres:**
- `msg` (str): Le message chiffré à déchiffrer
- `auto_copy` (bool): Copier le texte déchiffré dans le presse-papiers si True

**Retourne:**
- `str`: Le message en clair original

**Lève:**
- `ValueError`: Si l'entrée n'est pas une chaîne ou est vide
- `Exception`: Si le processus de déchiffrement échoue

**Exemple:**
```python
decrypted = mse_decipher(encrypted_message, auto_copy=True)
```

---

### <a name="performance-fr"></a>⚡ Performance

#### Benchmarks

Testé sur: Intel Core i7-9700K @ 3,6GHz, 16GB RAM

| Longueur Message | Temps Chiffrement | Temps Déchiffrement | Ratio Expansion |
|-----------------|-------------------|---------------------|-----------------|
| 10 caractères | 0,8 ms | 15,2 ms | 8,5x |
| 100 caractères | 1,2 ms | 18,7 ms | 7,2x |
| 1 000 caractères | 4,5 ms | 45,3 ms | 6,8x |
| 10 000 caractères | 38,2 ms | 412,5 ms | 6,5x |
| 100 000 caractères | 385,7 ms | 4 231,8 ms | 6,4x |

**Notes:**
- Le chiffrement est plus rapide que le déchiffrement (une clé vs toutes les clés)
- Le ratio d'expansion diminue avec la longueur du message
- Convient pour des messages jusqu'à ~10KB pour un usage en temps réel

---

### <a name="contribuer-fr"></a>🤝 Contribuer

Les contributions sont les bienvenues! Veuillez suivre ces directives:

1. Forker le dépôt
2. Créer une branche de fonctionnalité (`git checkout -b feature/NouvelleFonctionnalité`)
3. Commiter vos changements (`git commit -m 'Ajout NouvelleFonctionnalité'`)
4. Pousser vers la branche (`git push origin feature/NouvelleFonctionnalité`)
5. Ouvrir une Pull Request

**Domaines de Contribution:**
- Optimisation des performances
- Techniques d'obscurcissement supplémentaires
- Options de configuration améliorées
- Meilleure documentation
- Tests unitaires
- Interface graphique

---

## 📄 License

Copyright 2019-2025 by Enron Group. All Rights Reserved.

This software is provided for educational and puzzle creation purposes. See LICENSE file for details.

---

## 👥 Authors

- **Enron Group** - *Initial work and ongoing development*
- Website: [enrongroup.fr](http://enrongroup.fr)
- Contact: contact@enrongroup.fr

---

## 🙏 Acknowledgments

- Thanks to all contributors and puzzle enthusiasts
- Inspired by classic substitution ciphers and modern obfuscation techniques
- Built for the escape room and puzzle game community

---

## 📞 Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Email: support@enrongroup.fr
- Visit our website: [enrongroup.fr](http://enrongroup.fr)

---

**Made with ❤️ for puzzle creators and cryptography enthusiasts**
