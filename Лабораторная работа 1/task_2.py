def calculate_books_on_diskette(pages_per_book, lines_per_page, characters_per_line, bytes_per_character, diskette_capacity_mb):
    diskette_capacity_bytes = diskette_capacity_mb * 1024 * 1024

    bytes_per_page = lines_per_page * characters_per_line * bytes_per_character

    total_bytes_per_book = bytes_per_page * pages_per_book

    books_on_diskette = diskette_capacity_bytes // total_bytes_per_book

    return books_on_diskette

pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4
diskette_capacity_mb = 1.44

result = calculate_books_on_diskette(
    pages_per_book,
    lines_per_page,
    characters_per_line,
    bytes_per_character,
    diskette_capacity_mb,
)
print(f"На дискету можно поместить {result} книги")