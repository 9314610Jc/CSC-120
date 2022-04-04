from statistics import mean

intList = []
def Reverse(lst):
    lst.reverse()
    return lst
def Shift(lst):
    lst.reverse()
    lst.insert(0, lst.pop())
    return lst



def ask():
    a = input('enter an integer 1-10')
    intList.append(int(a))
    b = input('do you want to enter another integer? [y/n]')
    if b != 'y':
        print(intList)
        print('largest number: ' , max(intList))
        print('smallest number: ' , min(intList))
        print("Sum of all elements : ", sum(intList))
        print('Length of list: ' , len(intList))
        print('Average of list: ' , mean(intList))
        print('list reversed: ' , Reverse(intList))
        print('Last element moved to front:', Shift(intList))
    else:
        ask()
ask()



