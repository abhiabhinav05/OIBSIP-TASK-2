import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        print("No character types selected. Please select at least one.")
        return ""
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            raise ValueError("Password length must be positive.")
    except ValueError as e:
        print(e)
        return

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
