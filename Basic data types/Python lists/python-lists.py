n=int(input())
num_list=list()
for i in range(n):
    command=input()
    command_list=command.split()
    if command_list[0]=='insert':
        num_list.insert(int(command_list[1]),int(command_list[2]))
    elif command_list[0]=='print':
        print(num_list)
    elif command_list[0]=='remove':
        num_list.remove(int(command_list[1]))
    elif command_list[0]=='append':
        num_list.append(int(command_list[1]))
    elif command_list[0]=='sort':
        num_list.sort()
    elif command_list[0]=='pop':
        num_list.pop()
    elif command_list[0]=='reverse':
        num_list.reverse()
