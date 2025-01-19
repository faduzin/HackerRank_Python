def numberLength(n):

  # Return length of given number
    return len(str(n))

def reverseDigits(n):
    if (n % 10) == n:
        return n

    last = n % 10
    remaining = n // 10
    l = numberLength(remaining)

    return last*pow(10, l) + reverseDigits(remaining)

if __name__ == '__main__':
    n = int(input())
    input_list = list(map(int, input().split()))
    print((all(not values < 0 for values in input_list) and any(value == reverseDigits(value) for value in input_list))) 