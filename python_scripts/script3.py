f = open("test_file.txt", "w+")

f.write("Hello this is line 1.\n")
f.write("This is line 2.\n")
print(f.readlines())
print(f.readlines())
f.close()

with open("test_file.txt", "r+") as f:
    for line in f:
        print(line, end='')

f = open("test_file.txt", "r+")

print(f.readline())
print(f.readline())

f.close()
