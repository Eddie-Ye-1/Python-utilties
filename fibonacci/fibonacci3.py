def fibonacci_no_incursion(n):
    if n==0 or n==1:
        return n
    current = 2
    fibonacci_list = [0,1]
    while current<=n:
        fibonacci_list.append(fibonacci_list[current-1] + fibonacci_list[current-2])
        current +=1

    return fibonacci_list[n]

print(fibonacci_no_incursion(9))

