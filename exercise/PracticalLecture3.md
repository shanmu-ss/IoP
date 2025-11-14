## Day 3 - Lecture Exercise

- Deadline to submit the assignment at 7pm 

### Exercise 1 : Get Started with Functions

a. Write a function maxof2, which takes 2 input parameters and returns the highest value. 

b. Reusing the previous function maxof2, write a function maxof3 which returns the max value of its 3 input parameters

```python

def maxof2(a,b):
    if a>b:
        return a
    else:
        return b

def maxof3(a, b, c):
    temp = maxof2(a, b)
    if temp > c:
        return temp
    else:
        return c

print(maxof2(3,5))
print(maxof3(3,5,6))

```
### Exercise 2: Function for Sphere

- Write a function sphere that calculates the volume of sphere. As input, the function will take on argument, radius r and perform the calculation. on output the function returns the volume of sphere

- Hint: Formula for volume of sphere: v = 4/3 pi r^3

```python
def sphere_volume(r):
    volume = (4/3) * 3.14 * (r ** 3)
    return volume

print(sphere_volume(float(input("Enter radius: "))))
```

### Exercise 3: While Loop

a. Write a script that find the lowest integer n whose square is greater than 1234 i.e., n^2 > 1234
b. Write a python script that uses a while loop to display the first 20 elements of the multiplication table of 7. for each element, if the value is also a multiple of 3, append a star(*) to it.


```python
def lowestInteger():
    a = 1
    while a**2 <= 1234 :
        a += 1
    print(f"Lowest integer: {a}")

def iteration():
    a = 1
    while a <= 20:
        value = a * 7
        if value % 3 == 0:
            print(f"{value} *")
        else:
            print(value)
        a += 1

lowestInteger()
iteration()
```

### Excercise 4: Ticketing System

```python
while True:
    ageString = input("Enter your age: ")
    if ageString == 'quit':
        break
    age = int(ageString)
    if age <= 3:
        print(f"your age is {age} and the ticket is Free.")
    elif 3 <= age <= 12:
        print(f"your age is {age} and the ticket is $10.")
    elif age >= 12:
        print(f"your age is {age} and the ticket is $15.")
```

### Exercise 5: Favorite book

```python
def favorite_book(title):
    print(f'One of my favorite book is {title}')

favorite_book('Ikigai')
```

### Exercise 6: List Comprehensions 

```python
myList = [1,2,3,4,5,6,7,8,9,10,12,15,16,20,43,29]

print(f'even number: {[n for n in myList if n % 2 == 0]}')
print(f'odd number: {[n for n in myList if n % 2 != 0]}')
print(f'Divisible by 3 & 4 {[n for n in myList if n % 3 == 0 and n % 5==0]}')
```