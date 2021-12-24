import sys


def main(input_string):
    print(input_string[::-1])
st =input("Введите строку \n")
print("Различных символов ", len(set(st)))


if __name__ == '__main__':
    main(sys.argv[1])
