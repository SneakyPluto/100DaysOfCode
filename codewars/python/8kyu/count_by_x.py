def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    numbers = []
    if x and n >=1:
        for i in range(1, n + 1):
            numbers.append(x * i) # Multiply x by the current iteration number
    return numbers
print(count_by(2, 4)) #[2, 4, 6, 8]

#You have passed all of the tests! :)
#Alternative solution
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]