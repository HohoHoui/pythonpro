text_file = open("read_it.txt", "r")

print("Opening and closing the file.\n")
print("Reading characters from the file.")

print(text_file.read(1))
print(text_file.read(5))
text_file.close

text_file = open("read_it.txt", "r")
print("\nReading the entier file at once.")
whole_thing = text_file.read()
print(whole_thing)
text_file.close

text_file = open("read_it.txt", "r")
print("\nReading characters from a line.")
print(text_file.read(1))
print(text_file.read(5))
text_file.close

text_file = open("read_it.txt", "r")
print("\nReading one line at a time.")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close

text_file = open("read_it.txt", "r")
print("Reading the entire file into a list.")
lines = text_file.readlines()
print(lines)
text_file.close()

text_file = open("read_it.txt", "r")
print(len(text_file.readlines()))
text_file.close()

text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close

text_file = open("read_it.txt", "r")
print("\nLooping through the file. line by line.")
for line in text_file:
    print(line)
text_file.close

print("\n")

while(1):
    ans = input("Press the enter key to exit.")
    if ans == '':
        break

