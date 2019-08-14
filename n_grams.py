inp_file = open("tempfile.txt")
n = int(input("Enter number grams"))

for line in inp_file:
    count = 0
    words = line.split()
    for word in words[:-n+1]:
        print(" ".join(words[count:count+n]))
        count+=1

inp_file.close()
