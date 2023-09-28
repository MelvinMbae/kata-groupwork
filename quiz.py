# Solution for problem 1

# Option 1

my_function = input("Enter your string:")
arr = list(my_function)
arr2 = []
numbers_to_delete = 0

for i in arr:
    if arr.count(i) >= 2 and i not in arr2:
        numbers_to_delete += arr.count(i) % 2
        arr2.append(i)

print("Deletions needed:", numbers_to_delete)

# Option 2

# def my_function(input_string):

#     characters = ""

#     current_characters = 0

#     for letters in characters:
#         if letters == characters:
#             current_characters += 1
#         else:
#             current_characters = 1

# for letter in my_function:
#     if letter in my_function

# Option 3


def my_function(S):
    letter_count = {}

    for letter in S:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    print(letter_count)

    deletions_needed = 0

    for count in letter_count.values():
        if count % 2 != 0:
            deletions_needed += 1

    return deletions_needed


print(my_function("acbcbba"))
print(my_function("axxaxa"))


# solution for problem 2
def reverse_word(word):
    return word[::-1]


print(reverse_word("please reverse this word"))
