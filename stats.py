
def num_words(text):
    #split takes a list and seperates it into a list
    list = text.split()
    return len(list)

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_count(chars):
    sorted_dict = {key: value for key,
                   value in sorted(chars.items(),
                                   key=lambda item: item[1], reverse=True)}
    return sorted_dict


    #for key in sorted(chars, key=chars.get):
     #   sorted_dict[key] = chars[key]
    #return sorted_dict



    


