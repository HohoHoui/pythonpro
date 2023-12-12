text_file = open("write_it.txt", "w")
print("Creating a text file with the write() method.\n")

print("Reading the newly created file.")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close

text_file = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close


print("\nCreating a text file with the writelines() method.\n")
text_file = open("write_it2.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close
print("Reading the newly created file.")
text_file = open("write_it2.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close

print()

while True:
    ans = input("Press the enter key to exit.")
    if ans == '':
        break
