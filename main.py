from string_functions import (
    formatted_string, additional_value, repeat_strings, count_substring_occurrences,
    extract_substring, find_words_with_latin, is_palindrome, trim_and_measure,
    replace_sentence_endings, to_snake_case, remove_digits, reverse_words_order
)

def call_all_functions():
    """Шаг 10: Вызов всех функций из шагов 1-9."""

    # Шаг 1
    print(formatted_string("World", 10, additional_value))

    # Шаг 2
    repeat_strings("Hello", "World", 3)

    # Шаг 3
    print(count_substring_occurrences("Hello, hello, HELLO!", "hello"))

    # Шаг 4
    print(extract_substring("This is a string", 5, 14))

    # Шаг 5
    strings_with_latin, count = find_words_with_latin("Hi, Hello", "world", "Hello world!")
    print(f"Strings with Latin letters: {strings_with_latin}, Count: {count}")

    # Шаг 6
    print(is_palindrome("A man, a plan, a canal: Panama"))

    # Шаг 7
    print(trim_and_measure("   This   is   a    test string.    "))

    # Шаг 8
    print(replace_sentence_endings("Hello! How are you? I am fine."))

    # Шаг 9
    print(to_snake_case("This is a Test-String"))
    print(remove_digits("Password123"))
    print(reverse_words_order("This is a test string"))

if __name__ == "__main__":
    call_all_functions()
