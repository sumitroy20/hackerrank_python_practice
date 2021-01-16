n=int(input())
student_dict=dict()
for i in range(n):
    inputs=input().split()
    name=inputs[0]
    marks=list(map(float,inputs[1:]))
    student_dict[name]=marks

average=sum(student_dict[input()])/3
print('%.2f' % average)

