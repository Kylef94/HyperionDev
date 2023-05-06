def print_values_of(dictionary, keys):
    for key in keys:
        #was dictionary[k], corrected
        print(dictionary[key])

simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh ", #had '' in between other '' which broke the string, changed outer '' to ""
                        "maggie": " (Pacifier Suck)"}

#function call listed strings instead of passing in as one list
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

