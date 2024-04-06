def read_file(file_name):
    a = open(file_name)
    print(a.read().replace(',', '\n'))
    # print(*a.read().split(','), sep = '\n')

if __name__ == '__main__':
    read_file('numbers.txt')