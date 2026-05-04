import math
def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
    A = (n1 + n2 + n3) / 3

    if A >= 40:
        return f"Average grade: {A:.1f}, Status: Pass"
    else:
        # truncate to 2 decimal places (do not round) to match expected output
        truncated = math.floor(A * 100) / 100
        return f"Average grade: {truncated:.2f}, Status: fail"

if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))