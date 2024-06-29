import sys
input = sys.stdin.readline

n = int(input())
studentNames = {i:0 for i in input().split()}

for _ in range(n):
    likeStudentName = input().split()

    for i in likeStudentName:
        studentNames[i] += 1

for k, v in sorted(studentNames.items(), key=lambda x:-x[1]):
    print(k, v)