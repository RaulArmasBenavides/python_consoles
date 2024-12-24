import re

# Read inputs
rows, cols = map(int, input().split())
matrix = []

# Read the matrix rows and ensure they have the correct length
for _ in range(rows):
    row = input()
    if len(row) != cols:
        raise ValueError(f"Each row must have exactly {cols} characters.")
    matrix.append(row)

# Combine columns into a single string (reading column-wise)
decoded_script = ''.join([matrix[row][col] for col in range(cols) for row in range(rows)])

# Use regex to replace non-alphanumeric characters between alphanumerics with a space
decoded_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)

# Print the final decoded script
print(decoded_script)