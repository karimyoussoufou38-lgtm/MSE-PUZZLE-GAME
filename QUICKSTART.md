# 🚀 Guide de Démarrage Rapide MSE / MSE Quick Start Guide

## 🇫🇷 Français

### Installation Express (5 minutes)

```bash
# 1. Cloner ou télécharger le projet
git clone https://github.com/enrongroup/mse-encryption.git
cd mse-encryption

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Initialiser la configuration (première utilisation)
python tools.py
```

### Premier Chiffrement

Créez un fichier `test.py`:

```python
from MSE import mse_cipher, mse_decipher

# Votre message secret
message = "Le trésor est caché sous le vieux chêne"

# Chiffrement
encrypted = mse_cipher(message)
print(f"Message chiffré: {encrypted}")

# Déchiffrement
decrypted = mse_decipher(encrypted)
print(f"Message déchiffré: {decrypted}")
```

Exécutez:
```bash
python test.py
```

### Exemples d'Utilisation

#### 1. Énigme Simple
```python
from MSE import mse_cipher

# Créer une énigme
clue = "La clé est dans le livre rouge"
encrypted_clue = mse_cipher(clue, auto_copy=False)

print("Énigme pour vos joueurs:")
print(encrypted_clue)
```

#### 2. Escape Room Multi-étapes
```python
from MSE import mse_cipher

clues = [
    "Premier indice: Cherchez dans le salon",
    "Deuxième indice: Regardez derrière le tableau",
    "Troisième indice: Le code est 7394"
]

encrypted_clues = [mse_cipher(clue, auto_copy=False) for clue in clues]

for i, enc_clue in enumerate(encrypted_clues, 1):
    print(f"Énigme {i}:")
    print(enc_clue)
    print()
```

#### 3. Avec Statistiques
```python
from MSE import mse_cipher, get_encryption_stats

message = "Message secret"
encrypted = mse_cipher(message, auto_copy=False)

stats = get_encryption_stats(message, encrypted)
print(f"Longueur originale: {stats['original_length']}")
print(f"Longueur chiffrée: {stats['encrypted_length']}")
print(f"Taux d'expansion: {stats['expansion_ratio']:.2f}x")
```

### Configuration Personnalisée

Modifiez `configs/setting.json`:

```json
{
    "cipher": "ascii_letters",
    "cipher_punctuation": "True",
    "cipher_accent": "True",
    "cipher_digits": "True",
    "charac_len": [5, 6],
    "key_number": [1000, 2000]
}
```

Puis régénérez les clés:
```python
from tools import mixer, rebuild
mixer()    # Mélange les caractères
rebuild()  # Nettoie les doublons
```

### Démo Interactive

```bash
python main.py
```

Décommentez `demo()` dans `main.py` pour voir des exemples automatiques.

---

## 🇬🇧 English

### Express Installation (5 minutes)

```bash
# 1. Clone or download the project
git clone https://github.com/enrongroup/mse-encryption.git
cd mse-encryption

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize configuration (first time use)
python tools.py
```

### First Encryption

Create a file `test.py`:

```python
from MSE import mse_cipher, mse_decipher

# Your secret message
message = "The treasure is hidden under the old oak"

# Encryption
encrypted = mse_cipher(message)
print(f"Encrypted message: {encrypted}")

# Decryption
decrypted = mse_decipher(encrypted)
print(f"Decrypted message: {decrypted}")
```

Run:
```bash
python test.py
```

### Usage Examples

#### 1. Simple Puzzle
```python
from MSE import mse_cipher

# Create a puzzle
clue = "The key is in the red book"
encrypted_clue = mse_cipher(clue, auto_copy=False)

print("Puzzle for your players:")
print(encrypted_clue)
```

#### 2. Multi-Stage Escape Room
```python
from MSE import mse_cipher

clues = [
    "First clue: Search in the living room",
    "Second clue: Look behind the painting",
    "Third clue: The code is 7394"
]

encrypted_clues = [mse_cipher(clue, auto_copy=False) for clue in clues]

for i, enc_clue in enumerate(encrypted_clues, 1):
    print(f"Puzzle {i}:")
    print(enc_clue)
    print()
```

#### 3. With Statistics
```python
from MSE import mse_cipher, get_encryption_stats

message = "Secret message"
encrypted = mse_cipher(message, auto_copy=False)

stats = get_encryption_stats(message, encrypted)
print(f"Original length: {stats['original_length']}")
print(f"Encrypted length: {stats['encrypted_length']}")
print(f"Expansion rate: {stats['expansion_ratio']:.2f}x")
```

### Custom Configuration

Edit `configs/setting.json`:

```json
{
    "cipher": "ascii_letters",
    "cipher_punctuation": "True",
    "cipher_accent": "True",
    "cipher_digits": "True",
    "charac_len": [5, 6],
    "key_number": [1000, 2000]
}
```

Then regenerate keys:
```python
from tools import mixer, rebuild
mixer()    # Shuffle characters
rebuild()  # Clean duplicates
```

### Interactive Demo

```bash
python main.py
```

Uncomment `demo()` in `main.py` to see automatic examples.

---

## 📊 Difficulté des Énigmes / Puzzle Difficulty

### Facile / Easy
- Messages courts (< 20 caractères)
- Pas de ponctuation
- Indices fournis

### Moyen / Medium  
- Messages moyens (20-100 caractères)
- Avec ponctuation
- Analyse de fréquence nécessaire

### Difficile / Hard
- Messages longs (> 100 caractères)
- Textes complexes
- Plusieurs couches d'énigmes

---

## 🆘 Dépannage / Troubleshooting

### Problème: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Problème: "FileNotFoundError: keylib.txt"
```bash
python tools.py
```

### Problème: Le déchiffrement ne fonctionne pas
- Assurez-vous d'utiliser le même fichier `keylib.txt`
- Vérifiez que `setting.json` n'a pas été modifié
- Régénérez les clés avec `tools.py`

---

## 🎓 Ressources

- **Documentation complète**: `README.md`
- **Tests**: `python tests/test_mse.py`
- **Exemples**: dossier `examples/`
- **Support**: contact@enrongroup.fr

---

**🎮 Bon jeu! / Have fun!**
