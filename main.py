"""Have You Tried Turning It Off? — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The twist: the agent tells the customer to reboot THEMSELVES.
TEXT = "Have you tried turning it off and on again? No? Then have you tried turning yourself off and on again?"

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
