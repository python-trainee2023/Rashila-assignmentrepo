def searchBookDetails(authorname):
    try:
        found = False

        with open('book.txt', 'r') as f:
            for line in f:
                book_details = line.strip().split(',')
                if book_details[0].strip() == authorname:
                    print(line.strip())
                    found = True

        if not found:
            print(f"No books found by {authorname}")


    except FileNotFoundError:
        print("File not found.")


authorname = input("Enter author name for details: ")
searchBookDetails(authorname.title())
