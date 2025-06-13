def get_word_count(input):
    if not isinstance(input, str):
        try:
            input = str(input)
        except Exception: 
            return 0
    return len(input.split())

def create_character_statistics(text):
    stats = {}
    if not isinstance(text, str):
        try:
            text = str(text)
        except Exception: 
            return stats

    text = text.lower()
    for char in text: 
        count = stats.setdefault(char, 0)
        count += 1

        stats[char] = count

    return sort_dict(stats)

def sort_dict(dictionary):
    stats = []
    for key in dictionary:
        stats.append({"character": key, "num": dictionary[key]})

    def num_sort(dictionary):
        return dictionary["num"]

    stats.sort(reverse=True, key=num_sort)
    return stats
