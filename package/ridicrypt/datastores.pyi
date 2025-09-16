"""RIDI encrypted settings file handling.

This module provides classes and functions for decrypting and parsing RIDI
application settings files. Settings are stored in an encrypted format using
a custom AES implementation that matches CryptoJS behavior.
"""

def decrypt(key: str, path: str) -> str:
    """Decrypt a RIDI settings file and return the JSON string.

    This function decrypts an encrypted RIDI settings file using a custom AES
    implementation that matches CryptoJS behavior. The function handles PKCS7
    padding, checksum verification, and returns the decrypted JSON content as a string.

    The decryption process:
    1. Reads the encrypted settings file from the specified path
    2. Validates the file signature and checksum
    3. Applies PKCS7 padding to the key if needed based on UTF-16 length
    4. Performs AES-ECB decryption using CryptoJS-compatible implementation
    5. Removes PKCS7 padding from the decrypted data
    6. Returns the resulting JSON string

    Args:
        key: The decryption key as a string. The key will be processed according
            to CryptoJS UTF-8 parsing and may be PKCS7-padded to a 16-byte boundary
            depending on its UTF-16 character length.
        path: The file path to the encrypted settings file to decrypt.

    Returns:
        A string containing the decrypted JSON data from the settings file.

    Raises:
        RuntimeError: If the settings file cannot be found or read, has an invalid
            signature, fails checksum verification, cannot be decrypted, or contains
            invalid PKCS7 padding.

    Example:
        >>> from ridicrypt import utils
        >>> settings_path = utils.get_settings_path()
        >>> json_data = decrypt("my_decryption_key", settings_path)
        >>> import json
        >>> parsed_data = json.loads(json_data)
        >>> print(f"Username: {parsed_data['data']['auto_login']['username']}")

    Note:
        You can use utils.get_settings_path() to get the default system location
        for the RIDI settings file, which varies by operating system.
    """

