quote = input("Enter your favorite quote: ")
author = input("Who said it? ")

with open("quotes.txt", "a") as f:
    f.write(f'"{quote}" - {author}\n')

print("Quote saved successfully with author name!")

