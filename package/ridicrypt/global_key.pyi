"""RIDI global encryption key retrieval.

This module provides functionality to retrieve the global encryption key
from the system keyring, which is used for decrypting RIDI files.
"""

def get() -> str:
    """Retrieve the global RIDI encryption key from the system keyring.

    This function accesses the system keyring to retrieve the global encryption
    key used by RIDI applications. The key is stored in the keyring with different
    targets depending on the operating system:
    - Windows: "com.ridi.books/global"
    - macOS: "com.ridi.books"

    The retrieved key is base64-decoded before being returned as a string.

    Returns:
        The global encryption key as a string.

    Raises:
        RuntimeError: If the keyring entry cannot be found, access is denied,
            the stored data is not valid base64, the decoded data is not valid
            UTF-8, or other keyring access errors occur.

    Example:
        >>> global_key = get()
        >>> print(f"Key length: {len(global_key)}")
        Key length: 16

    Note:
        This function requires that the RIDI application has previously stored
        a global key in the system keyring. The key is typically set up during
        the initial application setup or login process.
    """
