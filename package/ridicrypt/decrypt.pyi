"""RIDI file decryption functionality.

This module provides functions for decrypting RIDI encrypted files and ZIP archives
using AES-128-CBC encryption with PKCS7 padding.
"""

def to_str(key: str, path: str) -> str:
    """Decrypt a RIDI encrypted file and return the result as a UTF-8 string.

    This function decrypts a single encrypted file using AES-128-CBC decryption
    and converts the result to a UTF-8 string. The first 16 bytes of the file
    are used as the initialization vector (IV), and the remaining bytes are
    the encrypted data.

    Args:
        key: A 16-character encryption key string for AES-128 decryption.
        path: The file path to the encrypted file to decrypt.

    Returns:
        The decrypted file content as a UTF-8 string.

    Raises:
        RuntimeError: If the key length is not 16 characters, the file is too small
            (less than 16 bytes), decryption fails, the decrypted data is not valid
            UTF-8, or file I/O errors occur.

    Example:
        >>> key = "sixteen_char_key"
        >>> text = to_str(key, '/path/to/encrypted_text.dat')
        >>> print(text)
        "Hello, World!"
    """

def binary(key: str, path: str, target: str) -> None:
    """Decrypt a RIDI encrypted file and save the result to a target file.

    This function decrypts an entire encrypted file using AES-128-CBC decryption
    and writes the decrypted content to a target file. The first 16 bytes of
    the source file are used as the initialization vector (IV).

    Args:
        key: A 16-character encryption key string for AES-128 decryption.
        path: The file path to the encrypted file to decrypt.
        target: The output file path where decrypted data will be written.

    Raises:
        RuntimeError: If the key length is not 16 characters, the file is too small
            (less than 16 bytes), decryption fails, or file I/O errors occur during
            reading or writing.

    Example:
        >>> key = "sixteen_char_key"
        >>> binary(key, '/path/to/encrypted.dat', '/path/to/output.txt')
    """

def zip(key: str, path: str, target: str) -> None:
    """Decrypt individual files within a ZIP archive and create a new ZIP.

    This function processes a ZIP archive by attempting to decrypt each file
    within it using the provided key. Files that cannot be decrypted (e.g.,
    non-encrypted files) are copied as-is to the output ZIP. The function
    preserves the original ZIP structure including directories and compression
    methods.

    Args:
        key: A 16-character encryption key string for AES-128 decryption.
        path: The file path to the input ZIP archive.
        target: The file path where the processed ZIP archive will be created.

    Raises:
        RuntimeError: If file I/O errors occur, the ZIP archive is corrupted,
            or other processing errors happen during ZIP manipulation.

    Example:
        >>> key = "sixteen_char_key"
        >>> zip(key, '/path/to/encrypted.zip', '/path/to/decrypted.zip')

    Note:
        This function attempts to decrypt each file in the ZIP. If decryption
        fails for a particular file (e.g., it's not encrypted), the original
        file content is preserved in the output ZIP.
    """
