def count_letters(text):
    letter_count = {}

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

    return letter_count


def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency_dict = {}

    for letter, count in letter_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = round(frequency, 2)

    return frequency_dict


def print_frequency(input_text):
    if not isinstance(input_text, str):
        raise ValueError("Входные данные должны быть строкой")
    letter_count = count_letters(input_text)
    frequency_dict = calculate_frequency(letter_count)

    for letter, frequency in frequency_dict.items():
        print(f"{letter}: {frequency}")

print_frequency("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
print_frequency(123)