
# Load the image
image_path = "gemastik_5.png"
image = Image.open(image_path)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Decode the QR code
decoded_objects = decode(image)

# Print the decoded data
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))

