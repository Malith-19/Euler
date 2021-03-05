def isPalindrome(n):
    str_n = str(n)
    if str_n == str_n[::-1]:
        return True
    return False


max_palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        multi = i*j
        if isPalindrome(multi) and multi>max_palindrome:
            max_palindrome = multi



print(max_palindrome)

