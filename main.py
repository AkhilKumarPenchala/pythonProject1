def readNnames(file_name, N):
    with open(str(file_name), 'r') as file:
        for line in file.readlines()[-N:]:
            print(line,end='')


if __name__ == '__main__':
    readNnames("Names.txt",4)




