"""Quick check that generated code can be committed to GitHub."""


def greet(name: str = "GitHub") -> str:
    return f"Hello, {name}! This file was generated to verify an upload."


if __name__ == "__main__":
    print(greet())
