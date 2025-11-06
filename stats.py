def count_words(text):
    return len(text.split())

def count_chars(text):
    seen = {}
    for c in text:
        char = c.lower()
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    return seen

def sort_char_dict(char_dict):
    unsorted_list = []
    for item in char_dict:
        unsorted_list.append({"char": str(item), "num": char_dict[item]})
    sorted_list = sorted(unsorted_list, key = lambda d: d['num'], reverse = True)
    return sorted_list
