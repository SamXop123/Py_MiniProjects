import sys
import pyfiglet

def main():
    # Handle command-line arguments
    if len(sys.argv) == 1:
        font = "standard"  # Default font
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        font = sys.argv[2]  # User-specified font
    else:
        print("Usage: python figlet.py [-f fontname]")
        sys.exit(1)

    # Get user input
    text = input("Input: ")

    try:
        # Generate ASCII art with the specified font
        ascii_art = pyfiglet.figlet_format(text, font=font)
        print("Output:")
        print(ascii_art)
    except pyfiglet.FontNotFound:
        print("Error: Font not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
