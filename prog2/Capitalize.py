sentence_sample=input("Please enter a sentence to capitalize :")

print(sentence_sample.title())

print("\n\n")

def revsent(x):
    return (x) [::-1]


normal_sentence = input("please enter a string to reverse :")

new_sent=revsent(normal_sentence)

print(new_sent)

print("\n\n")

def splitsent(x):
    return(x.split())

split_sentence=input("Pleae enter sentence to split :")

new_split=splitsent(split_sentence)

news_sent = revsent(split_sentence)

print(new_split)
print("\n\n")
print(new_split)





