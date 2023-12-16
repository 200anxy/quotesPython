import random
file_paths = r"C:\Users\Aadarsh Nair\Desktop\Aadarsh_Code\Quotes\Quotes.txt"

# Usage

filecool = open(file_paths, 'r', encoding='utf-8') 
content = filecool.read()
quotes = content.split(';')  # Split the content by ';'
random_quote = random.choice(quotes)

print(random_quote)
filecool.close()
    


