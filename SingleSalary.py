'''
Given a non-empty array of integers salaries, every element appears twice except for one. Find
that single one.
'''




def findSingleSalary(salaries:list)->int:
    '''

    :param salaries:
    :return: the single salary
    :Approch:  the function findSingleSalary iterates through the array and compares each element to all other elements.
     When it finds an element that doesn't have a duplicate, it returns that element as the single salary.
    '''
    singleSalary=0
    for count ,i in enumerate(salaries):
        for j in range(count+1,len(salaries)):
            if salaries[j] == i:
                break
            else:
                singleSalary=i
    return singleSalary

