import sys
from pathlib import Path

from ridicrypt import decrypt, settings, utils

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python decrypt.py <encrypted_file> <dat_file> <output_file>"
        )
        sys.exit(1)

    encrypted_file = sys.argv[1]
    dat_file = sys.argv[2]
    output_file = sys.argv[3]

    global_key = utils.get_global_key()
    settings = settings.decrypt(global_key, utils.get_settings_path())
    device_id = settings.data.device.device_id
    key = decrypt.to_str(device_id[:16], dat_file)[68:84]

    try:
        if Path(encrypted_file).suffix == ".epub":
            try:
                decrypt.zip(key, encrypted_file, output_file)
            except RuntimeError:
                decrypt.binary(key, encrypted_file, output_file)
        decrypt.binary(key, encrypted_file, output_file)
        print(f"Decrypted {encrypted_file} to {output_file}")
    except RuntimeError as e:
        print(f"Decryption failed: {e}")
        sys.exit(1)
