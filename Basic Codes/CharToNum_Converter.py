def alphabet_position(text):
    result = ""
    for char in text:
        if char.isalpha():
            char = char.lower()
            position = ord(char) - ord('a') + 1
            result += str(position) + " "
    return result.strip()

text = input("Enter your string:").strip()
alphabet_position(text)
