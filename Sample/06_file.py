with open("example.txt", "r") as f: 
    lines = f.readlines() 
    line_count = len(lines) 

with open("example.txt", "r") as f: 
    content = f.read() 


word_count = len(content.split()) 
character_count = len(content) 

print("Number of Lines:", line_count) 
print("Number of Words:", word_count) 
print("Number of Characters:", character_count)