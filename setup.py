#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for MSE - Multiple Substitution Encryption System
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    with open(requirements_path, "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f 
                       if line.strip() and not line.startswith("#")]

setup(
    name="mse-encryption",
    version="29.0.0",
    author="MSE Team",
    author_email="support@mse-encryption.org",
    description="Advanced text encryption system with multiple substitution layers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mse-encryption",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/mse-encryption/issues",
        "Documentation": "https://mse-encryption.org/docs",
        "Source Code": "https://github.com/yourusername/mse-encryption",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "black>=23.7.0",
            "mypy>=1.4.1",
            "sphinx>=7.0.0",
        ],
        "performance": [
            "numpy>=1.24.0",
            "numba>=0.57.0",
        ],
        "security": [
            "cryptography>=41.0.0",
            "pycryptodome>=3.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mse=mse_cli:main",
            "mse-cli=mse_cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.json", "*.md", "configs/*"],
    },
    keywords=[
        "encryption",
        "cryptography",
        "substitution",
        "cipher",
        "text-processing",
        "security",
        "obfuscation",
        "mse",
        "puzzle",
        "game-engine",
    ],
    zip_safe=False,
)
