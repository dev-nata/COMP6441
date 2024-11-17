import hashlib

# Function to calculate the SHA256 hash of a file
def calculate_sha256(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
    return sha256_hash

# Function to modify the file by adding spaces at the end of lines
def modify_file_with_spaces(file_path, output_path, spaces_to_add):
    with open(file_path, 'rb') as f:
        lines = f.readlines()
    
    # Add spaces to each line
    modified_lines = [
        line.rstrip(b'\n') + (b' ' * spaces_to_add) + b'\n' if line.strip() else line
        for line in lines
    ]
    
    # Write the modified lines to a new file
    with open(output_path, 'wb') as f:
        f.writelines(modified_lines)

# File paths for the provided files
real_file_path = 'confession_real.txt'  # Replace with actual path
fake_file_path = 'confession_fake.txt'  # Replace with actual path

# Output file paths
modified_real_path = 'confession_real_modified.txt'
modified_fake_path = 'confession_fake_modified.txt'

# Variables to track progress
spaces_to_add = 0
matching_last_two = False

while not matching_last_two:
    # Increment the number of spaces to add
    spaces_to_add += 1
    
    # Modify files
    modify_file_with_spaces(real_file_path, modified_real_path, spaces_to_add)
    modify_file_with_spaces(fake_file_path, modified_fake_path, spaces_to_add)
    
    # Calculate hashes
    real_hash = calculate_sha256(modified_real_path)
    fake_hash = calculate_sha256(modified_fake_path)
    
    # Check if the last 2 digits match
    matching_last_two = real_hash[-2:] == fake_hash[-2:]

# Print results
print(f"Spaces added: {spaces_to_add}")
print(f"Real File Hash: {real_hash}")
print(f"Fake File Hash: {fake_hash}")
