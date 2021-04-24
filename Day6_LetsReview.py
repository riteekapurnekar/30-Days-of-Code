# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    st = input()
    print(st[::2], st[1::2])   
    
    # here st[::2] means the elements of the list st starting from index 0 till end with a count of 2 will be printed
    # st[1::2] means the elements of the list st starting from index 1 till end with a count of 2 will be printed
