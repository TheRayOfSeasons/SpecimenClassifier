def slicedict(dictionary, string, removeEmpty=False):
    if removeEmpty:
        return {
            key:value for key,value in dictionary.items() 
            if key.startswith(string) and
            value != '' and
            value is not None
        }
    else:
        return {
            key:value for key,value in dictionary.items() 
            if key.startswith(string)
        }


def to_dictionary_list(choices):
    listed_choices = []
    for choice in choices:
        dictionary = {
            'value': choice[0],
            'display': choice[1],
        }
        listed_choices.append(dictionary)
    return listed_choices
