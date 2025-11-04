# IoP
Introduction to python


# Day 2

### Exercise: 1

1. working with strings: 

    - write a script that asks the user for a string and displays this strings in reverse order. for example, msg="bonjour", output should be "ruojnob"

    - write a program that displays the message from the user in lower, upper, and title case. 

```python
var_input = input(f"Enter the string: ",)

print(var_input[::-1])
print("Lowercase:", var_input.lower())
print("Uppercase:", var_input.upper())
print("Title case:", var_input.title())

```

### Exercise 3 

- Write a script that counts the number of occurrences of a value in my_list. That is, the number of times this values appears in the list. 

- The script will prompt the user to enter a value on the keyboard

- Check the value exist in my_list, if yes, then display the number of occurrences of that values 

- if its is not present in the list, the result will be 0.

``` python
### List of numbers
my_list = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]

myValue = int(input("Enter the number to valid the occurance:")) 

temp = []

for i in my_list:
    if i == myValue: 
        temp.append(i)
        print(temp)

myCount = len(temp)

print(myCount)

```

### Exercise 4: 

- Using the same list as in exercise 3 

- write a python script that removes all occurences of a user-entered value and then displays the edited list. 

- Make a disctonary which consist of the numbers from the list in question 3, item is key and the occurance is value.


```python
# Given list 
my_list = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]

# Function to validate and update the dictories values from given list and its occurances
def dict_occurance(my_list):
    dict = {} 
    for i in my_list: 
        if i in dict: 
            dict[i] +=1 
        else: 
            dict[i] = 1

    print("Occurrences dictionary:", dict)


# Input value from the user
myValue = int(input("Enter the number to valid the occurance:"))

# new list to append the excluded value from given list
new_list = []

for i in range(len(my_list)):
    if my_list[i] == myValue:
        print(f"Found at index {i}")
    else:
        new_list.append(my_list[i])

print("Updated list:", new_list)
dict_occurance(my_list)
```

### Exercise 5:

Write a program that ask the user to enter their name and score in three subjects let say english, french, psanish (enter data ofr minimum 3 student 

calculate the average of each student 

average>= 90%
excellent 80-90
good 60-80
less than 60 fail 
display the grades obaintend by each students 

``` python
# Number of students
num_students = 3

students = []
for i in range(num_students):
    print(f"Enter details for Student {i + 1}:")
    name = input("Name: ")
    english = int(input("English score of the student: "))
    french = int(input("French score of the student: "))
    spanish = int(input("Spanish score of the student: "))

    scores = [english, french, spanish]
    average = sum(scores) / len(scores)

    if average >= 90:
        grade = "Excellent"
    elif 80 <= average < 90:
        grade = "Good"
    elif 60 <= average < 80:
        grade = "Average"
    else:
        grade = "Fail"

    students.append({
        "name": name,
        "average": round(average, 2),
        "grade": grade
    })

for student in students:
    print(f"{student['name']}: Average = {student['average']}%, Grade = {student['grade']}")

```
