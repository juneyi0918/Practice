N=int(input())
min_diff=4
for _ in range(N):
    problem,diff=input().split()
    diff=int(diff)
    if diff<=min_diff:
        min_diff=diff
        ans=problem

print(ans)