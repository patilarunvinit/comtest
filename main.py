set_of_word = ["tweeting","tweet","we","someone","highlights"]

with open('text.txt') as text:
    lines = text.readlines()
    a=0
    for i in range(len(lines)):
        sentence = lines[i]
        list=[]
        word = ""
        for j in range(len(sentence)):
            if sentence[j]==" " or j==(len(sentence)-1):
                list.append(word)
                word=""

            else:
                word+=sentence[j]

        if len(list)==1 and list[0]=="":
            continue

        else:
            a += 1
            degree_of_profanity = sum(1 for t in list if t in set_of_word) / len(list)
            print(f"profanity of tweet no {a} is  {degree_of_profanity}")
