
line1 = ""
line2 = ""
line3 = ""
line4 = ""

errorlog = ""

with open('tbprocessed.txt', 'r', encoding="utf8") as f:

    for line in f:

        line1 = line2
        line2 = line3
        line3 = line4
        line4 = line

        if line.startswith("ERROR:"):
            errorlog += line1
            errorlog += line2
            errorlog += line3
            errorlog += line4

print(errorlog)

with open("errors.txt", "w", encoding="utf8") as f:
    f.write(errorlog)


