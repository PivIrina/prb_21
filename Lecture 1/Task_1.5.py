import sys

def main(input_string):
    print(input_string[::-1])
print ("Введите n и t: ")
n,t =map(int, input().split())
print ("Введите позиции: ")
positions = input()
pos = list(positions)
m = 0
while (m != t):
    m +=1
    for i in range(len(pos)):
        if (pos[i] =="G" and pos[i-1] =="B"):
            pos[i],pos[i-1] = pos[i-1],pos[i]
position ="".join(pos)           
print(position)
if __name__ == '__main__':
    main(sys.argv[1])

