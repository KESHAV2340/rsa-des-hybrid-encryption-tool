# rsa-des-hybrid-encryption-tool
Hybrid Encryption Tool implementing RSA-2048 and DES with randomized OAEP padding. Demonstrates PGP-style encryption blocks for secure message transmission.
# RSA DES Hybrid Encryption Tool

This project demonstrates a hybrid cryptography system using RSA and DES.

Features
- RSA 2048-bit encryption
- DES symmetric encryption
- OAEP randomized RSA encryption
- PGP-style encrypted message block

Workflow
1. Message encrypted using DES
2. DES key encrypted using RSA
3. Receiver decrypts key using RSA
4. Message decrypted using DES

Technologies
Python
PyCryptodome
