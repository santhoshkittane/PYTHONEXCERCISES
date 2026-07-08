from PIL import Image
from pyzbar.pyzbar import decode

image_path = "C:\\Users\\SanthoshKittane\\Desktop\\PYTHON\\"
file = input("Enter file name: ")
image_path = image_path + file
image = Image.open(image_path)
decoded_objects = decode(image)
if decoded_objects:
    for obj in decoded_objects:
        # Data is extracted as bytes, decode it to string
        qr_data = obj.data.decode("utf-8")
        print(f"Type: {obj.type}")
        print(f"Decoded Data: {qr_data}")
else:
    print("No QR codes found.")

