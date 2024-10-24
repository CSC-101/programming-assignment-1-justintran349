from curses.textpad import rectangle

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
def ascending_pairs(lists: list) -> list:
    list1 = []
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            if lists[i][0] > lists[i][1]:
                list1.append([lists[i][1], lists[i][0]])
            else:
                list1.append(lists[i])
        else:
            list1.append(lists[i])
    return list1
#function gets a nested list and if the len is = 2 it will swap index if the first is greater than the second.
# Part 4
def add_prices(price1, price2):
    dollars = price1.dollars + price2.dollars
    cents = price1.cents + price2.cents
    while cents>100:
        cents-=100
        dollars+=1
    return data.Price(dollars,cents)
#gets inputed dollars and cents, turns it into the total price in dollars

# Part 5
def rectangle_area(rectangle1):
    return ((rectangle1.top_left.y - rectangle1.bottom_right.y) *
            (rectangle1.bottom_right.x - rectangle1.top_left.x))
#gets inputed a rectangle and it finds the distance from the 2 points
# Part 6
def books_by_author(name:str, books: list):
    listone = []
    for i in books:
        for one in range(len(i.authors)):
            if name in i.authors[1]:
                listone.append[i.title]
    return listone
#gets inputed a author name and a list of their books and checks if they match, if it does they append
#the book to a new list and returns it.
# Part 7
def circle_bound(rectangle):
    diameter = (rectangle.top_left.y - rectangle.bottom_right.y)**2 + (rectangle.bottom_right.x - rectangle.top_left.x)**2)/2
    radius = diameter/2
    center_y = rectangle.top_left.y - (rectangle.top_left.y - rectangle.bottom_right.x - rectangle.top_left.x)/2
    center_x = rectangle.bottom_right.x - (rectangle.bottom_right.x - rectangle.top_left.x)/2
    return data.Circle(data.Point(center_x,center_y),radius)
#finds the radius using the center_x and center_y and the diameter
# Part 8
def below_pay_average(employees:list)->list:
    lists = []
    sum = 0
    for i in range(len(employees)):
        sum += employees[i].pay_rate
    average = sum / len(employees)
    for i in range(len(employees)):
        if employees[i].pay_rate < average:
            lists.append(employees[i].name)
    print("Average:", average)
    return lists
#finds which employees have a below average wage