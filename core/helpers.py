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
