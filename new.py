fw = 'sample-text-file.txt'

dictionary = {}

with open(fw,'r') as fh:
    text = fh.readlines()

for line in text:
    line = line.lower().replace(',','').replace('.','')
    words = line.split()
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] + 1

dictionary_count = sorted(dictionary.items(), reverse=True , key=lambda x : x[1])
print(dictionary_count)