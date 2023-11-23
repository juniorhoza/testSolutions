'''
Given an array of integers numbers sorted in non-decreasing order, find the starting and ending
position of a given target value.
If target is not found in the array, return [-1, -1]
'''

def firstAndLastPosition(numbers:list,target:int)->list:
    '''

    :param numbers:
    :param target:
    :return:list
    '''
    positions=[-1,-1]
    if target not in numbers:
        return positions
    else:

       positions[0]=numbers.index(target)
       if(numbers[numbers.index(target)+1] == target):
            positions[1]=numbers.index(target)+1
       return positions



