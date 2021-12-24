import sys
 
    
def main(input_string):
    print(input_string[::-1])
palindrome =input("Введите строку \n")
reverse = palindrome[::-1]
if (palindrome == reverse):
    print("Палиндром")
else:
    print("Не является палиндром")

    
if __name__ == '__main__':
    main(sys.argv[1])
