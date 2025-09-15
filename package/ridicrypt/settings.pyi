"""RIDI encrypted settings file handling.

This module provides classes and functions for decrypting and parsing RIDI
application settings files. Settings are stored in an encrypted format using
a custom AES implementation that matches CryptoJS behavior.
"""

class Settings:
    """Represents the root settings data structure.

    This class contains the complete settings data including schema version
    and user/device information. Settings are typically loaded from an
    encrypted settings file using the decrypt function.

    Attributes:
        schema_version: The version number of the settings schema.
        data: The main settings data containing user and device information.
    """

    @property
    def schema_version(self) -> int:
        """Get the schema version of the settings format.

        Returns:
            The schema version as an integer, used to determine the structure
            and format of the settings data.
        """

    @property
    def data(self) -> "Data":
        """Get the main settings data container.

        Returns:
            A Data object containing user auto-login information and device details.
        """

class Data:
    """Container for the main settings data.

    This class holds the primary settings information including auto-login
    credentials and device identification data.

    Attributes:
        auto_login: User authentication and auto-login settings.
        device: Device identification and configuration data.
    """

    @property
    def auto_login(self) -> "AutoLogin":
        """Get the auto-login settings.

        Returns:
            An AutoLogin object containing user authentication information
            such as username and refresh token.
        """

    @property
    def device(self) -> "Device":
        """Get the device settings.

        Returns:
            A Device object containing device identification information
            such as device ID and nickname.
        """

class AutoLogin:
    """User auto-login and authentication settings.

    This class contains user credentials and authentication tokens used
    for automatic login functionality.

    Attributes:
        username: The user's login username.
        refresh_token: The refresh token for maintaining authentication.
    """

    @property
    def username(self) -> str:
        """Get the user's login username.

        Returns:
            The username string used for user authentication.
        """

    @property
    def refresh_token(self) -> str:
        """Get the user's refresh token.

        Returns:
            The refresh token string used to maintain user authentication
            sessions without requiring re-login.
        """

class Device:
    """Device identification and configuration settings.

    This class contains information that uniquely identifies and describes
    the device where the RIDI application is running.

    Attributes:
        device_id: Unique identifier for the device.
        device_nick: Human-readable nickname for the device.
    """

    @property
    def device_id(self) -> str:
        """Get the unique device identifier.

        Returns:
            A string that uniquely identifies this device in the RIDI system.
        """

    @property
    def device_nick(self) -> str:
        """Get the device nickname.

        Returns:
            A human-readable name or nickname assigned to this device.
        """

def decrypt(key: str, path: str) -> "Settings":
    """Decrypt and parse a RIDI settings file.

    This function decrypts an encrypted RIDI settings file using a custom AES
    implementation that matches CryptoJS behavior. The function handles PKCS7
    padding, checksum verification, and JSON parsing of the decrypted content.

    The decryption process:
    1. Reads the encrypted settings file from the specified path
    2. Validates the file signature and checksum
    3. Applies PKCS7 padding to the key if needed based on UTF-16 length
    4. Performs AES-ECB decryption using CryptoJS-compatible implementation
    5. Removes PKCS7 padding from the decrypted data
    6. Parses the resulting JSON into a Settings object

    Args:
        key: The decryption key as a string. The key will be processed according
            to CryptoJS UTF-8 parsing and may be PKCS7-padded to a 16-byte boundary
            depending on its UTF-16 character length.
        path: The file path to the encrypted settings file to decrypt.

    Returns:
        A Settings object containing the parsed settings data with user
        authentication information and device details.

    Raises:
        RuntimeError: If the settings file cannot be found or read, has an invalid
            signature, fails checksum verification, cannot be decrypted, contains
            invalid PKCS7 padding, or the decrypted data is not valid JSON.

    Example:
        >>> from ridicrypt import utils
        >>> settings_path = utils.get_settings_path()
        >>> settings = decrypt("my_decryption_key", settings_path)
        >>> print(f"Username: {settings.data.auto_login.username}")
        >>> print(f"Device: {settings.data.device.device_nick}")

    Note:
        You can use utils.get_settings_path() to get the default system location
        for the RIDI settings file, which varies by operating system.
    """
