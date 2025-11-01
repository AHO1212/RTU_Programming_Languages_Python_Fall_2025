def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    cleaned = (name or "").strip()
    if not cleaned:
        return "Hello! Welcome to Python!"
    return f"Hello, {cleaned.capitalize()}! Welcome to Python!"


if __name__ == "__main__":
    user_name = input("What is your name? ")
    print(greet_user(user_name))
