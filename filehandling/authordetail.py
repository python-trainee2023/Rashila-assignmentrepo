def searchBookDetails(authorname):
    try:
        with open('book.txt', 'r') as f:
            for line in f:
                book_details = line.strip().split(',')
                if book_details[0].strip() == authorname:
                    print(line.strip())
                else:
                    print(f"No such {authorname}")

    except FileNotFoundError:
        print("file not found.")


authorname = input("Enter author name for details: ")
searchBookDetails(authorname)
