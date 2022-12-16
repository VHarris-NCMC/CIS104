def main():

    fname = "romeo.txt"
    fhand = open(fname, "r")

    words = []
    for line in fhand:
        splat = line.split()

        for word in splat:
            if word in words:
                continue
            words.append(word)


    words.sort()
    print(words)




main()