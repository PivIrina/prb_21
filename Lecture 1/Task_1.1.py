import sys


def main(input_string):
    print(input_string[::-1])
print ("Введите строку")
txt = input()
print ("Количество символов",len(txt)-txt.count(' '))


if __name__ == '__main__':
    main(sys.argv[1])

    
