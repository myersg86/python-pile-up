def main():
    occurrences = {}
    while True:
        words = input('Enter line: ')
        if words =='':
            break
        for word in words.split(): 
            occurrences[word]=occurrences.get(word,0)+1
    for word in sorted(occurrences):
        print(word, occurrences[word])
main()


