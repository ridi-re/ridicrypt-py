import sys

from ridicrypt import decrypt, global_key, settings

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python decrypt.py <epub_file> <dat_file> <output_file> <method:legacy|new>")
        sys.exit(1)

    epub_file = sys.argv[1]
    dat_file = sys.argv[2]
    output_file = sys.argv[3]
    method = sys.argv[4]

    global_key = global_key.get()
    settings = settings.decrypt(global_key)
    device_id = settings.data.device.device_id
    epub_key = decrypt.to_str(device_id[:16].encode('utf-8'), dat_file)[68:84]
    epub_key_bytes = epub_key.encode('utf-8')
    if method == "legacy":
        decrypt.zip_legacy(
            epub_key_bytes, epub_file, output_file
        )
    elif method == "new":
        decrypt.zip(
            epub_key_bytes, epub_file, output_file
        )
    print(f"Decrypted {epub_file} to {output_file}")
