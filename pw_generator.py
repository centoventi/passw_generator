import argparse
import secrets
import string

def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_symbols=True):
    chars = ""

    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("You must enable at least one character type.")

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        include_upper=not args.no_upper,
        include_lower=not args.no_lower,
        include_digits=not args.no_digits,
        include_symbols=not args.no_symbols,
    )

    print(password)

if __name__ == "__main__":
    main()