 

#  Given two lists, write a function to find the common elements between them and return them in a new list.

def my_names():
    list1=["Ann","joy","rehema","kam","kelly"]

    list2=["kelly","Ann","trecy","john","rem"]
    print(set(list1).intersection(list2))
# Write a function that takes in a list of numbers and returns a new list containing only the prime numbers.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



# Write a program that takes in a list of words and sorts them based on the number of vowels in each word.
def number_value():
    com_num=["books","pens","pencile","testbook","setbook"]
    com_num.sort()
    print (com_num)
    print('Sorted list:',com_num)
# Given a list of integers, write a function that returns the smallest element in the list.
def small_value():
    list=[30,4,51,6,10,8,9]

def int_num():
    a = {"James": 95, "Jane": 98, "Matt": 85, "Ashely": 90}
    sorted(a.items())
    
def concatenate_kwaargs(*syt):
    answer=""
    for str in syt:
        answer += str
    return answer    


def concatenate_kwargs(**str):
    answer=""
    for stm in str.values():
        answer+=stm
    return answer  