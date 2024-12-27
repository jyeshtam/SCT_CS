from PIL import Image
import random

# Function to load an image
def load_image(image_path):
    return Image.open(image_path)

# Function to save an image
def save_image(image, output_path):
    image.save(output_path)

# Function to encrypt image by swapping pixels
def encrypt_image(image, key):
    pixels = list(image.getdata())  # Get pixel data
    random.seed(key)  # Use the key for reproducible randomness
    random.shuffle(pixels)  # Shuffle pixel values
    encrypted_image = Image.new(image.mode, image.size)  # Create a new blank image
    encrypted_image.putdata(pixels)  # Put shuffled pixels into the new image
    return encrypted_image

# Function to decrypt image by reversing the process
def decrypt_image(image, key):
    pixels = list(image.getdata())
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)  # Shuffle indices based on the key
    decrypted_pixels = [None] * len(pixels)  # Create a blank list for decrypted pixels
    for i, index in enumerate(indices):
        decrypted_pixels[index] = pixels[i]
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    return decrypted_image

# Function to apply mathematical operation on pixels
def apply_math_operation(image, key):
    pixels = list(image.getdata())
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]  # XOR operation
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    return encrypted_image

# Main function
if __name__ == "__main__":
    # File paths
    input_path = "input.jpg"  # Replace with your input image file
    encrypted_path = "encrypted.jpg"
    decrypted_path = "decrypted.jpg"
    
    # Load the input image
    img = load_image(input_path)
    
    # Define a key for encryption (integer value)
    key = 12345  # You can change this key
    
    # Encrypt the image
    encrypted_img = encrypt_image(img, key)
    save_image(encrypted_img, encrypted_path)
    print("Image encrypted and saved as", encrypted_path)
    
    # Decrypt the image
    decrypted_img = decrypt_image(encrypted_img, key)
    save_image(decrypted_img, decrypted_path)
    print("Image decrypted and saved as", decrypted_path)
