for _ in range(int(input())):
    name,grade=input().split()
    grade=int(grade)
    if grade>=97:
        grade='A+'
    elif grade>=90:
        grade='A'
    elif grade>=87:
        grade='B+'
    elif grade>=80:
        grade='B'
    elif grade>=77:
        grade='C+'
    elif grade>=70:
        grade='C'
    elif grade>=67:
        grade='D+'
    elif grade>=60:
        grade='D'
    elif grade>=0:
        grade='F'
        
    print(name,grade)