def word_count(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    freq = {}

    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq

sentence = "the cat and the hat"
print(word_count(sentence))