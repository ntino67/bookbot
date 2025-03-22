def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count


def count_characters(text):
    char_counter = {}
    low_text = text.lower()
    for char in low_text:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
    return char_counter


def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    sorted = []
    for key in dict:
        if key.isalpha():
            temp = {}
            value = dict[key]
            temp["name"] = key
            temp["num"] = value
            sorted.append(temp)

    sorted.sort(reverse=True, key=sort_on)
    return sorted


def print_report(word_count, char_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_count:
        count = dict["num"]
        char = dict["name"]
        print(f"{char}: {count}")
    print("============= end ===============")
