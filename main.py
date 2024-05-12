import os
import sys
import time
from pathlib import Path
from operator import itemgetter


def display_info() -> None:
    """Displays info about the bot"""
    print("Hello, I am Griffin, your friendly book bot.")
    print("I will generate a report on the books listed in the 'books/'")
    print("Generating report...")
    time.sleep(1.5)
    os.system("clear")


def print_book_info(book_path) -> None:
    """Gets info about a book and prints it"""
    with open(book_path) as f:
        text_content = f.read()
        num_words = words_count(text_content)
        frequency = letter_frequency(text_content)
        sorted_frequency = sort_frequency(frequency)

        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        for frequency in sorted_frequency:
            print(f"The '{frequency[0]}' character was found {frequency[1]} times")
        print("--- End report ---")


def sort_frequency(frequency: dict) -> list:
    """sorts frequency dict based on frequency, from highest to lowest"""
    return sorted(frequency.items(), key=itemgetter(1), reverse=True)


def letter_frequency(text: str) -> dict[str, int]:
    """returns frequency of letters as a dict in a given string"""
    frequency = {}
    for character in text:
        character = character.lower()
        if not character.isalpha():
            continue
        if character not in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1
    return frequency


def words_count(text: str) -> int:
    """return word count in a given string"""
    return len(text.split())


def main() -> None:
    display_info()
    basepath = Path("books/")
    if not basepath.is_dir():
        print("'books/' not found!", file=sys.stderr)
        sys.exit(1)
    books = (entry for entry in basepath.iterdir() if entry.is_file())
    for book in books:
        print_book_info(book)


if __name__ == "__main__":
    main()
