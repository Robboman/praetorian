import base64
import struct

# Base64 string
base64_string = "<b64 string>"

# Decode Base64 string
image_data = base64.b64decode(base64_string)

# PNG file sig check
png_signature = b'\x89PNG\r\n\x1a\n'
if image_data[:8] != png_signature:
    raise ValueError("Not a valid PNG file!")

def read_chunks(data):
    # Start after file sig (will error out otherwise)
    index = 8
    chunks = []

    while index < len(data):
        # Get chunk length
        length = struct.unpack('>I', data[index:index+4])[0]
        index += 4
        
        # Get chunk type
        chunk_type = data[index:index+4].decode('ascii')
        index += 4
        
        # Get chunk data
        chunk_data = data[index:index+length]
        index += length
        
        # Get chunk CRC
        crc = struct.unpack('>I', data[index:index+4])[0]
        index += 4
        
        # Save chunk
        chunks.append((chunk_type, length, chunk_data, crc))
    
    return chunks

# Extract chunks
chunks = read_chunks(image_data)

# Print chunks
for chunk_type, length, chunk_data, crc in chunks:
    print(f"Chunk Type: {chunk_type}")
    print(f"Chunk Length: {length} bytes")
    if chunk_type == "tEXt" or chunk_type == "zTXt":
        try:
            print(f"Text Data: {chunk_data.decode('latin1')}")
        except UnicodeDecodeError:
            print(f"Binary Data (Base64): {base64.b64encode(chunk_data).decode('ascii')}")
    else:
        print(f"Chunk Data (Base64): {base64.b64encode(chunk_data).decode('ascii')}")
    print(f"CRC: {crc}")
    print("-" * 50)
