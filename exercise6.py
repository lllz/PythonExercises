def palindrome():
    x = input("Tell me a word: ")
    mid = int (len(x)/2)
    for i in range(0, mid):
        if x[i] != x[-(i + 1)]:
            break
        i += 1
        return True
