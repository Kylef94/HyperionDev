import spacy
nlp = spacy.load('en_core_web_sm')

#cat monkey baanana test
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#note on the above:
#interesting that it picks up more of a similarity between monkey and banana(.40) vs .22 for cat and banana
#which makes sense but good to see model distinguishes this well
#
# word1 = nlp("Microsoft")
# word2 = nlp("Boeing")
# word3 = nlp("Apple")

#note on the above:
#interesting that it can work on company names relatively robustly, and can tell apple and microsoft are much more related than boeing

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#en_core_web_md vs en_core_web_sm
#sm less able to distingish between monkey cat and banana(scores higher for all words and significantly)
#but scores then higher across the board for the model sentence testsm so not entierely consistent , there seems to be
#more variance in the sm model outputs



#output for en_core_web_md
#
# 0.5929930274321619
# 0.40415016164997786
# 0.22358825939615987
# cat cat 1.0
# cat apple 0.2036806046962738
# cat monkey 0.5929930210113525
# cat banana 0.2235882580280304
# apple cat 0.2036806046962738
# apple apple 1.0
# apple monkey 0.2342509925365448
# apple banana 0.6646699905395508
# monkey cat 0.5929930210113525
# monkey apple 0.2342509925365448
# monkey monkey 1.0
# monkey banana 0.4041501581668854
# banana cat 0.2235882580280304
# banana apple 0.6646699905395508
# banana monkey 0.4041501581668854
# banana banana 1.0
# Where did my dog go -  0.6085941301496852
# Hello, there is my car -  0.8033180111627156
# I've lost my car in my car -  0.6787541571030323
# I'd like my boat back -  0.5624940517078084
# I will name my dog Diana -  0.6491444739190607

#output for en_core_web_md
#
# C:\Users\kfarr\Python\Python Projects\HyperionDev\T38 answers\semantic.py:20: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word1.similarity(word2))
# C:\Users\kfarr\Python\Python Projects\HyperionDev\T38 answers\semantic.py:21: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word3.similarity(word2))
# C:\Users\kfarr\Python\Python Projects\HyperionDev\T38 answers\semantic.py:22: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word3.similarity(word1))
# C:\Users\kfarr\Python\Python Projects\HyperionDev\T38 answers\semantic.py:28: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(token1.text, token2.text, token1.similarity(token2))
# 0.6770565478895127
# 0.7276309976205778
# 0.6806929391210822
# cat cat 1.0
# cat apple 0.6963739395141602
# cat monkey 0.6012927293777466
# cat banana 0.1981828361749649
# apple cat 0.6963739395141602
# apple apple 1.0
# apple monkey 0.7503186464309692
# apple banana 0.2811802327632904
# monkey cat 0.6012927293777466
# monkey apple 0.7503186464309692
# monkey monkey 1.0
# monkey banana 0.35610878467559814
# banana cat 0.1981828361749649
# banana apple 0.2811802327632904
# banana monkey 0.35610878467559814
# banana banana 1.0
# Where did my dog go -  0.4313613632347263
# Hello, there is my car -  0.5648939507997681
# C:\Users\kfarr\Python\Python Projects\HyperionDev\T38 answers\semantic.py:42: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   similarity = nlp(sentence).similarity(model_sentence)
# I've lost my car in my car -  0.548028403302901
# I'd like my boat back -  0.3007499696891998
# I will name my dog Diana -  0.3904074310483232


