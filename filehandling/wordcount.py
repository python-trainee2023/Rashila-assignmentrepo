def countwords(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            words=text.split()
            count=0
            for word in words:
                if word.endswith('e'):
                    count +=1
            return count

    except FileNotFoundError:
        print(f"file {filename} not found.")


result = countwords('myfile.txt')
print(f"Number of words ending with 'e': {result}")