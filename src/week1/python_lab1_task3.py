def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return character count, word count, and whether it contains 'Python'."""
    text = text or ""
    total_chars = len(text)
    word_count = len(text.split())
    has_python = "python" in text.lower()
    return total_chars, word_count, has_python


if __name__ == "__main__":
    s = input("Enter a sentence: ")
    total, words, has_py = analyze_sentence(s)
    print(f"Total characters: {total}")
    print(f"Word count: {words}")
    print(f"Contains 'Python': {has_py}")
