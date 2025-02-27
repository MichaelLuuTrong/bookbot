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