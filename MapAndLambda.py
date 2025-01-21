cube = lambda x: x*x*x

def fibonacci(n):  
    sequence = [0,1]
    if n > 2:
        [sequence.append(sequence[i-2] + sequence[i-1]) for i in range(2,n)]
    else:
        return sequence[:n]
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
