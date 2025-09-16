"""RIDI utility helpers.

This module exposes small utility functions used by the RIDI decryption tools,
including retrieving the global encryption key from the system keyring and
locating the encrypted settings file path on the current OS.
"""

def get_global_key() -> str:
    """Retrieve the global RIDI encryption key from the system keyring.

    This function reads the global encryption key that RIDI applications store
    in the OS keyring. The stored value is base64-encoded; it is decoded and
    returned as a UTF-8 string.

    Keyring targets by platform:
    - Windows: service "com.ridi.books/global"
    - macOS:   service "com.ridi.books"

    Returns:
        The global encryption key as a string (typically 16 characters for
        AES-128 operations).

    Raises:
        RuntimeError: If the keyring entry is missing or inaccessible, if the
            stored data is not valid base64, or if the decoded bytes are not
            valid UTF-8.

    Example:
        >>> key = get_global_key()
        >>> len(key)
        16
    """

def get_ridi_data_path() -> str:
    """Get the OS-specific path to the RIDI application data directory.

    Resolves and returns the absolute path to the RIDI application data directory
    used by the application. The location depends on the operating system:

    - Windows: ``%APPDATA%\\Ridibooks``
    - macOS: ``$HOME/Library/Application Support/Ridibooks``

    Returns:
        The absolute file system path to the data directory as a string.

    Raises:
        RuntimeError: If required environment variables are not set or if the
            path cannot be constructed.

    Example:
        >>> path = get_ridi_data_path()
        >>> path.endswith("Ridibooks")
        True
    """

