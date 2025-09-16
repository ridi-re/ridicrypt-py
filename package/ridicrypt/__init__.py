"""RidiCrypt: A Python library for decrypting RIDI encrypted files.

This package provides functionality to decrypt RIDI encrypted files, access global
encryption keys from the system keyring, and parse encrypted settings files.

Modules:
    decrypt: Core decryption functions for files and ZIP archives.
    global_key: Functions to retrieve global encryption keys from system keyring.
    settings: Classes and functions for handling encrypted settings data.
"""

from .ridicrypt import datastores, decrypt, utils

__all__ = ["datastores", "decrypt", "utils"]
