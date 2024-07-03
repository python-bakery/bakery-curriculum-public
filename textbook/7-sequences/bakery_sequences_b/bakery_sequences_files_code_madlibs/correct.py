words= []
with open('words.txt') as words_file:
    for word in words_file:
        words.append(word.strip())

with open('story.txt') as story_file:
    for line in story_file:
        for word in words:
            line =  line.strip().replace(word, "____")
        print(line)
