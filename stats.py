def word_counter(text: str):
    return len(text.split())

def character_counter(text: str):
    lowercase_text= text.lower()
    character_dict = {}
    for character in lowercase_text:
        if character not in character_dict:
            character_dict[character] = 1
        elif character in character_dict:
            character_dict[character] = character_dict[character] + 1
    return character_dict

def get_value_from_dict_in_list(dict_of_count:dict):
    return list(dict_of_count.values())[0]

def get_key_from_dict_in_list(dict_of_count: dict):
    return list(dict_of_count.keys())[0]

def dict_to_sorted_list(dict_of_counts: dict):
    # dict to unsorted list
    list_of_dicts = [{character: value} for character, value in dict_of_counts.items()]
    
    # sort by value in key-value pair
    # can use lambda function instead
    list_of_dicts.sort(key=get_value_from_dict_in_list, reverse = True)
    
    # remove non-alpha characters
    list_of_alphas = []
    for character_and_count_dict in list_of_dicts:
        # can use lambda function instead
        if get_key_from_dict_in_list(character_and_count_dict).isalpha():
            list_of_alphas.append(character_and_count_dict)

    return list_of_alphas

    