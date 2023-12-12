print("Input your string...")
text_file = open("prob2-1.txt", "w")
while True:
    ans = input()
    if ans == 'Q':
        print("Write porcess has been finished\n")
        break
    text_file.write(ans + '\n')
text_file.close()

print("\nYour inputs are below...")
text_file = open("prob2-1.txt", "r")

for line in text_file:
    print(line.strip())

text_file.close()

