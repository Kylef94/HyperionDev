import spacy

nlp = spacy.load("en_core_web_md")

gardenpathSentences = ["After Bill drank the water proved to be poisoned.",
             "Without her contributions would be impossible",
             "The old man the boat",
             "The girl told the story cried",
             "The florist sent the flowers was pleased"]

for sentence in gardenpathSentences:
    tokens = nlp(sentence)
    print([(t.text, t.pos_) for t in tokens])

#ENTITY 1 - SCONJ
print(spacy.explain("SCONJ"))

#what was the entity/explanantion:
#subordinating conjunction - introduces a subordinate clause, which makes sense as this was for the word 'after
#other word examples are after, provided, because

#ENTITY 2 - ADP
print(spacy.explain("ADP"))
#what was the entity/explanantion:
#adposition - combines with a phrase to help convey the context meaning, and as this was provided for the word 'without'
#this makes sense as such words only make sense to give context to another phrase