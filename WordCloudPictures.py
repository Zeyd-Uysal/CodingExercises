import wordcloud

f = open("demofile.txt", "r")
text = ""
words = {}
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just"]
for x in f:
    line = ""
    for j in x:
        if j.isalpha() or j.isspace():
            line += j
    text += line + ""
for i in text.split():
    i = i.lower()
    if not (i in uninteresting_words):
        if i in words.keys():
            words[i] += 1
        else:
            words.update({i: 0})
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(words)
cloud.to_file("image.jpg")
