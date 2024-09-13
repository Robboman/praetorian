from stegano import generators, lsb

encoded_image_path = "<image_path>"

# LSB method from steg lib
extracted_message = lsb.reveal(encoded_image_path, generator=generators.alpha)

# Output
if extracted_message:
    print("Hidden Message: ", extracted_message)
else:
    print("No hidden message found.")