# Book Catalog

You're building a small library system.  Before you can track loans or shelves, you need to model the books themselves.

## Requirements

1. In `Book.py`, write a `Book` class with an `__init__` method that takes the following parameters and assigns them as instance attributes:
   - `title` (str)
   - `author` (str)
   - `page_count` (int)
   - `genre` (str)

2. Add a method `describe()` that prints a one-line summary of the book.  For example:
   ```
   "Nineteen Eighty-Four" by George Orwell — 328 pages (fiction)
   ```

3. At the bottom of `Book.py` (or in a new `main.py`), create **at least four** different `Book` instances representing books from **at least two** different genres, and call `describe()` on each.

## Things to think about
- What attributes belong to *the class itself* vs. *each instance*?
- If every Book defaulted to `page_count = 0`, where would that default live: on the class or in `__init__`?
- What's the difference between calling `book.describe()` and `Book.describe(book)`?

## Stretch
- Add a class attribute `total_books` that increments every time a new `Book` is instantiated.  Print it after creating your four books.
- Add a method `short_title()` that returns the title truncated to 20 characters with `...` appended if it was cut off.
- Put your books in a list and print them sorted by `page_count`.

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
