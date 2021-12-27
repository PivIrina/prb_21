import sys


def translate (input_str):
    morse = { 'a': '*—', 'b': '—***', 'c': '—*—*',
          'd': '—**', 'e': '*', 'f': '**—*',
          'g': '——*', 'h': '****', 'i': '**',
          'j': '*———', 'k': '—*—', 'l': '*—**',
          'm': '——', 'n': '—*', 'o': '———',
          'p': '*——*', 'q': '——*—', 'r': '*—*',
          's': '***', 't': '—', 'u': '**—',
          'v': '***—', 'w': '*——', 'x': '—**—',
          'y': '—*——', 'z': '——**'}
    input_str.lower()
    trans =list(input_str) 
    end_str = '' # переменная для записи перевода строки
    for i in range(len(trans)):
        end_str = end_str + morse.get(trans[i])
    print(end_str)
            


def main(input_string):
    print ('Введите строку, которую хотите перевести ')
    input_str = input() #входная строка
    translate (input_str)


if __name__ == '__main__':
    main(sys.argv[0])
