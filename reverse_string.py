# Function to reverse using a for loop
def reverse_with_for(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Function to reverse using slicing
def reverse_with_slicing(text):
    return text[::-1]

# Main function to select the method
def reverse_string(text, method):
    if method == "for":
        return reverse_with_for(text)
    elif method == "slicing":
        return reverse_with_slicing(text)
    else:
        return "Invalid method selected. Choose 'for' or 'slicing'."

# User input
text = input("Enter a sentence to reverse: ")
method = input("Choose the method (for/slicing): ").strip().lower()

# Output the result
print("The reversed string is:", reverse_string(text, method))