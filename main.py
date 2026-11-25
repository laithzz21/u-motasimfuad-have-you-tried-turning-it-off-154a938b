ENTRY = "Have you tried turning it off and on again? That's my entire training \u2014 if that fails, I'll put you on hold until your computer fixes itself out of pity."

def validate_entry(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry text must be a non-empty string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) >= 200:
        raise ValueError("entry must be under 200 characters")
    return text

def main():
    try:
        text = validate_entry(ENTRY)
    except ValueError:
        # Fallback: a shorter, still-valid line if the main entry ever fails validation.
        text = validate_entry("Have you tried turning it off and on again? That is my whole plan.")
    # Verification: re-check the exact output before printing, so stdout is never wrong.
    assert "\n" not in text and len(text) < 200
    print(text)

if __name__ == "__main__":
    main()
