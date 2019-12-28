# Question link:https://www.geeksforgeeks.org/lucky-numbers/

def generate_lucky_numbers(num,arr): # Genrate all lucky numbers
    if len(arr) < num:
        return arr
    else:
        i = num
        while i < len(arr):
            del arr[i]
            i = i + num
        return generate_lucky_numbers(num+1,arr)


def islucky(number):
    # Creating a list of all luck numbers
    lucky_numbers = generate_lucky_numbers(2,list(range(1,number)))
    if number in lucky_numbers:
        return True
    else:
        return False

