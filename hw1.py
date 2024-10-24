import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word: str)-> int:
    vowels = "AaEeIiOoUu"
    count = sum(1 for vowel in word if vowel in vowels)
    return count
#counts the vowels in the unputted word
# Part 2
def short_lists(list1: list[list[int]]):
    list1=[]
    for i in range(len(list1)):
        if len(list1[i]) == 2:
            list1.append(list1[i])
    return list1
#if the len of the list is equal to 2, it'll append itself to the end of the list, creating a nested list.
# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


