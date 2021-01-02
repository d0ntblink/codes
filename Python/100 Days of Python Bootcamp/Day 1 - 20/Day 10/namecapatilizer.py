def format_name(first, last):
    while True :
        if first == "" or last == "" :
            return "Invalid Option"
        return first.capitalize() + " " + last.capitalize()
        
print(format_name(first=input("What is your first name ? ") , last=input("What is your last name ? ")))