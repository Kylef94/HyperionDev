import spacy


def compare_hulk():
    """This functions takes in a list of movies for the txt file and compares them
    against the hulk movie for similarity"""

    #load spacy library
    nlp = spacy.load('en_core_web_md')

    #set up dict for storing movies descriptions
    movies = {}

    #load movies
    with open('movies.txt', 'r') as f:
        data = f.readlines()

        #loop through data, clean and add to dict
        for movie in data:
            desc = movie[9:].strip('\n')
            movies.update({movie[:7]: desc})

    #string for hulk movie loaded with nlp
    hulk_movie = nlp('Will he save the world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick' \
                 'Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk' \
                 'lands on the planet Sakaar where he is sold into slavery and trainer as a gladiator')

    #vars for loop
    max_similar = 0
    most_similar_movie = None

    #loops throuhg movies dict, compares with Hulk movie description, and keeps track of the most similar movie
    for movie in movies.keys():
        desc = movies[movie]
        similarity = nlp(desc).similarity(hulk_movie)

        #logic to determine if this is most similar movie so far, and storing result
        if similarity > max_similar:
            max_similar = similarity
            most_similar_movie = movie

    #output
    return most_similar_movie

if __name__ == "__main__":
    print(compare_hulk())