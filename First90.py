with open("book.txt") as myFile:
    content = myFile.read()
    
with open("first.txt","w") as File:
    con = File.write(content[:90])