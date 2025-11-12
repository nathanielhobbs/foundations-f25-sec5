import sys

# this is an argument vector (that is a list of strings of python command line arguments)
print(sys.argv)

print('We will read this file',sys.argv[1])
print('We will write the file', sys.argv[2])




exit()

file_name = sys.argv[1]
with open(file_name) as f:
    print(f.read()) # this moves the stream pointer to the end by the time its finished
    print(f.read()) # this will print nothing

    f.seek(0)       # move the stream pointer to position 0
    print(f.read()) # this will print because the pointer has been reset

    f.seek(0)       # move the stream pointer to position 0
    print(f.readline()) # this will print because the pointer has been reset

    f.seek(0)       # move the stream pointer to position 0
    print(f.readlines()) # this will print because the pointer has been reset

