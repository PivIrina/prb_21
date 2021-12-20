import sys

def main(input_string):
    print(input_string[::-1])
print ("Введите n и t: ")
n,t =map(int, input().split())
print ("Введите a: ")
worlds = input()
worlds_array = [int(i) for i in worlds.split(" ")]
a = 1
while (a < t):
    a=a+worlds_array[a-1]
    if (a==t):
        print ("YES")
        break
    if (a > t):
        print ("NO")
        break

if __name__ == '__main__':
    main(sys.argv[1])
