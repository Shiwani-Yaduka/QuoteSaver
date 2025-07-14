quote = input("Enter your favorite quote: ")
with open("quotes.txt", "a") as f:
    f.write(quote + "\n")
print("Quote saved successfully!")

