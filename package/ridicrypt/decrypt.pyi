"""RIDI file decryption functionality.

This module provides functions for decrypting RIDI encrypted files and ZIP archives
using AES-128-CBC encryption with PKCS7 padding.
"""

def to_bytes(key: bytes, path: str) -> bytes:
    """Decrypt a RIDI encrypted file and return the raw decrypted data.

    This function decrypts a single encrypted file using AES-128-CBC decryption.
    The first 16 bytes of the file are used as the initialization vector (IV),
    and the remaining bytes are the encrypted data.

    Args:
        key: A 16-byte encryption key for AES-128 decryption.
        path: The file path to the encrypted file to decrypt.

    Returns:
        The decrypted file content as raw bytes.

    Raises:
        RuntimeError: If the key length is not 16 bytes, the file is too small
            (less than 16 bytes), decryption fails, or file I/O errors occur.

    Example:
        >>> key = b'sixteen_byte_key'
        >>> decrypted_data = to_bytes(key, '/path/to/encrypted.dat')
        >>> print(len(decrypted_data))
        1024
    """

def to_str(key: bytes, path: str) -> str:
    """Decrypt a RIDI encrypted file and return the result as a UTF-8 string.

    This function is a convenience wrapper around decrypt() that automatically
    converts the decrypted bytes to a UTF-8 string. It's useful when the
    encrypted file contains text data.

    Args:
        key: A 16-byte encryption key for AES-128 decryption.
        path: The file path to the encrypted file to decrypt.

    Returns:
        The decrypted file content as a UTF-8 string.

    Raises:
        RuntimeError: If the key length is not 16 bytes, the file is too small,
            decryption fails, the decrypted data is not valid UTF-8, or file
            I/O errors occur.

    Example:
        >>> key = b'sixteen_byte_key'
        >>> text = to_str(key, '/path/to/encrypted_text.dat')
        >>> print(text)
        "Hello, World!"
    """

def zip_legacy(key: bytes, path: str, target: str) -> None:
    """Decrypt a RIDI encrypted file and save the result to a target file.

    This is a legacy function that decrypts an entire encrypted file and writes
    the decrypted content to a target file. It's primarily maintained for
    backward compatibility.

    Args:
        key: A 16-byte encryption key for AES-128 decryption.
        path: The file path to the encrypted file to decrypt.
        target: The output file path where decrypted data will be written.

    Raises:
        RuntimeError: If the key length is not 16 bytes, the file is too small,
            decryption fails, or file I/O errors occur during reading or writing.

    Example:
        >>> key = b'sixteen_byte_key'
        >>> zip_legacy(key, '/path/to/encrypted.dat', '/path/to/output.txt')
    """

def zip(key: bytes, path: str, target: str) -> None:
    """Decrypt individual files within a ZIP archive and create a new ZIP.

    This function processes a ZIP archive by attempting to decrypt each file
    within it using the provided key. Files that cannot be decrypted (e.g.,
    non-encrypted files) are copied as-is to the output ZIP. The function
    preserves the original ZIP structure including directories and compression
    methods.

    Args:
        key: A 16-byte encryption key for AES-128 decryption.
        path: The file path to the input ZIP archive.
        target: The file path where the processed ZIP archive will be created.

    Raises:
        RuntimeError: If file I/O errors occur, the ZIP archive is corrupted,
            or other processing errors happen during ZIP manipulation.

    Example:
        >>> key = b'sixteen_byte_key'
        >>> zip(key, '/path/to/encrypted.zip', '/path/to/decrypted.zip')

    Note:
        This function attempts to decrypt each file in the ZIP. If decryption
        fails for a particular file (e.g., it's not encrypted), the original
        file content is preserved in the output ZIP.
    """
