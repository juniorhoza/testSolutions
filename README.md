# **This Documentation will refer to the Python answers**

## **Finding the Single Salary in an Array**

This Python function, findSingleSalary, helps find a unique salary within an array where every element appears twice except for one.

### **How It Works**
The findSingleSalary function uses the following steps:

    1. Iterating and Comparing: 
        It iterates through the provided array of salaries using nested loops.
        
    2. Checking for Duplicates: 
        For each salary in the array, the function compares it to all other salaries in the array.
        
    3. Identifying the Single Salary: 
        When it finds a salary that doesn't have a duplicate, it updates the single salary variable to that value.
        
### Approach
The approach taken by the function is to check each salary against all other salaries in the array. When it encounters a salary that doesn't have a duplicate, it returns that as a single salary.


![image](https://github.com/juniorhoza/testSolutions/assets/40476836/f315c077-360e-46ef-a8d8-ac3d74f64487)


### **Usage**
You can use this function by passing your array of salaries to findSingleSalary, and it will output the single salary that appears only once.

**Example:**

    salaries = [25000, 25000, 19000, 19000, 50, 1, 1]
    print(findSingleSalary(salaries))
> [!NOTE]
>  For cases where the target is not found in the array, the function returns 0


 ## **Finding Start and End Positions of a Target Value**

This Python function, firstAndLastPosition, locates the starting and ending positions of a target value within a sorted array of integers.

### **How It Works**
The firstAndLastPosition function performs the following steps:

    1. Initial Setup: 
        It initializes the positions list with [-1, -1], representing the starting and ending positions. If the target value is not present in the array, it returns this default list.
        
    2. Finding Positions: 
        If the target value exists in the array, it proceeds to find the starting position by using the index() function to locate the first occurrence of the target.
        

    3- Determining the Ending Position: 
        If the target appears more than once, it checks for the next occurrence of the target after the starting position and updates the ending position accordingly.

### **Approach**

The function begins by checking if the target exists in the array. If found, it determines the starting position using index(). If a subsequent occurrence exists after the starting position, it updates the ending position accordingly.

![image](https://github.com/juniorhoza/testSolutions/assets/40476836/3144212e-98a7-425f-8784-628f8a44a173)


### **Usage**

To use this function, provide a sorted array of numbers and the target value. It will return a list containing the starting and ending positions of the target value within the array.


        numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5]
        target_value = 3
        print(firstAndLastPosition(numbers, target_value))
        
> [!NOTE]
>  For cases where the target is not found in the array, the function returns [-1, -1].
