n=int(input())
student_list=list()
for i in range(n):
    name=input()
    grade=float(input())
    student_list.append((grade,name))

student_list.sort()

min_grade=student_list[0][0]

second_min_grade=min_grade

for i in range(n):
    if student_list[i][0]>second_min_grade:
        second_min_grade=student_list[i][0]
        break

new_list=list()

for i in range(n):
    if student_list[i][0]==second_min_grade:
        new_list.append(student_list[i])
    else:
        pass

new_list.sort()

for name in new_list:
    print(name[1])



