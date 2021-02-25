N=int(input())

for i in range(0,N):
    string= input()
    print(string[0::2]+' '+string[1::2]) #slice first half starting from 0 every other element 2, 4, 6(even) +' '+Second half starting from 1 every other element 3, 5, 7(odd)