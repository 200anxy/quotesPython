import random
file_paths = r"C:\Users\Aadarsh Nair\Desktop\Aadarsh_Code\Quotes\Quotes.txt"

# Usage

x = open(file_paths, 'r', encoding='utf-8')
content = x.read()
quotes = content.split(';')  # Split the content by ';'
random_quote = random.choice(quotes)

print(random_quote)
x.close()
