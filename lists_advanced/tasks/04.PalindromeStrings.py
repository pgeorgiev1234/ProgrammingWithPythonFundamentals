strings = input().split()
desired_polly = input()
palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(desired_polly)} times")
