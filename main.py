def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = get_chars_dict_list(chars_dict)
    sort_chars_dict_list(chars_dict_list, True, sort_on_times_found)
    print_report(path, words, chars_dict_list)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if not lowered in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars


def get_chars_dict_list(chars_dict):
    chars_dict_list = []
    for c in chars_dict:
        chars_dict_list.append({"char": c, "times_found": chars_dict[c]})
    return chars_dict_list


def sort_chars_dict_list(chars_dict_list, reverse, key):
    chars_dict_list.sort(reverse=reverse, key=key)


def sort_on_times_found(dict):
    return dict["times_found"]


def print_report(path, num_words, chars_dict_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for c in chars_dict_list:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' character was found {
                c["times_found"]} times")
    print("--- End report ---")


main()
