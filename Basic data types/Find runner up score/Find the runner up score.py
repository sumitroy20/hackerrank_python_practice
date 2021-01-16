n=int(input())
score_list=input().split()
score_list=list(map(int,score_list))
score_list.sort(reverse=True)
max_score=score_list[0]
runner_up_score=None

for i in range(n):
    if score_list[i]<max_score:
        runner_up_score=score_list[i]
        break;

print(runner_up_score)

