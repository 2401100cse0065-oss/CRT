def number_triangle(n: int) -> str:
    result = []
    
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        result.append(row)
    
    return "\n".join(result)


if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))