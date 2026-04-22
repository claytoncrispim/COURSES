# LinkedIn Learning – Python Essential Training: Challenges Explained

> **Note:** Any file with `solution` in its name was provided by the **instructor**, not written by the student.

---

## Table of Contents

1. [02_07 – Factorial](#0207--factorial)
2. [03_06 – Hex to Decimal Conversion](#0306--hex-to-decimal-conversion)
3. [04_06 – Encode ASCII Art (Run-Length Encoding)](#0406--encode-ascii-art-run-length-encoding)
4. [05_04 – Faster Prime Finding](#0504--faster-prime-finding)
5. [06_04 – Sum of Triangles](#0604--sum-of-triangles)
6. [07_04 – Drawing Shapes with Classes](#0704--drawing-shapes-with-classes)

---

## 02_07 – Factorial

**File:** `02_07_factorial.py`

### What is a factorial?

The factorial of a number is the result of multiplying that number by every whole number below it, down to 1.

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Approach in the file

The file contains many **commented-out attempts** — these are thinking steps the student went through while trying to figure out the solution. This is totally normal when learning!

The final working code (given by the instructor) uses two approaches:

**1. Iterative (using a loop):**
```python
def factorial(num):
    factorial = 1
    counter = 1
    while counter <= num:
        factorial = factorial * counter
        counter = counter + 1
    return factorial
```
Think of it like a machine that starts at 1 and keeps multiplying as it counts up to the target number.

**2. Recursive (a function that calls itself):**
```python
def recFactorial(num):
    if num == 0:
        return 1
    return num * recFactorial(num - 1)
```
Think of it like Russian nesting dolls — `factorial(5)` opens `factorial(4)`, which opens `factorial(3)`... until it reaches `0`, and then it comes all the way back multiplying as it goes.

> Both solutions are in `02_07_factorial.py`, provided by the instructor.

---

## 03_06 – Hex to Decimal Conversion

**Files:**
- `03_06_conv_hex_dec.py` ← student's solution
- `03_06_solution_one_conv_hex_dec.py` ← 📌 instructor's solution
- `03_06_solution_two_conv_hex_dec.py` ← 📌 instructor's solution

### What is hexadecimal?

Hexadecimal (hex) is a base-16 number system. Instead of digits 0–9, it uses 0–9 and A–F (where A=10, B=11, ... F=15).

Example: `A2` in hex = `10 × 16 + 2 = 162` in decimal.

### Approach 1 – Fixed length checks (student + instructor solution one)

Both the student and instructor's first solution use `if` statements to handle strings of length 1, 2, or 3:

```python
if len(hexNum) == 2:
    return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
```

It works, but it only handles hex numbers up to 3 characters long — it doesn't scale.

### Approach 2 – Loop with exponent (instructor solution two)

The instructor's second solution is smarter. It loops through every character and uses **powers of 16** based on the character's position:

```python
exponent = len(hexNum) - 1
for char in hexNum:
    converted = converted + (hexNumbers[char] * (16 ** exponent))
    exponent = exponent - 1
```

This works for a hex number of **any length**, not just 1–3 characters. Much more flexible!

---

## 04_06 – Encode ASCII Art (Run-Length Encoding)

**File:** `04_06_encode_ASCII_art.py`

### What is run-length encoding?

It's a simple way to compress text by replacing repeated characters with a count. For example:

```
'AAAAABBBBBCCCCC'  →  [('A', 5), ('B', 5), ('C', 5)]
```

### Approach in the file

The file contains a **commented-out student attempt**, followed by the working code written by the instructor.

The instructor's `encodeString` function:
- Walks through the string character by character
- Keeps track of the previous character and a counter
- When the character changes, it saves the `(character, count)` pair to a list

The `decodeString` function does the reverse — it takes the list of tuples and rebuilds the original string by repeating each character the right number of times:

```python
decodedStr = decodedStr + item[0] * item[1]
```

> Both `encodeString` and `decodeString` in this file were provided by the instructor.

---

## 05_04 – Faster Prime Finding

**Files:**
- `05_04_faster_prime_finding.py` ← student's solution
- `05_04_solution_faster_prime_finding.py` ← 📌 instructor's solution

### What is a prime number?

A number that is only divisible by 1 and itself. Example: 2, 3, 5, 7, 11...

### Why "faster"?

A naive approach checks every number up to `n-1` as a possible divisor. The trick is: you only need to check up to the **square root** of a number, because factors always come in pairs.

### Student's approach

The student's solution finds all primes up to a number using a loop and the square root trick, but it still tests division by **all numbers** up to the square root:

```python
for factor in range(2, int(number ** 0.5) + 1):
    if number % factor == 0:
        break
```

### Instructor's approach (solution)

The instructor's solution is more efficient — it only divides by **already-found primes**, not all numbers. This reduces the number of checks significantly:

```python
for factor in primes:
    if number % factor == 0:
        break
    if factor > sqrtNum:
        primes.append(number)
        break
```

If none of the known primes divide the number evenly before reaching the square root, it must be prime.

---

## 06_04 – Sum of Triangles

**File:** `06_04_sum_of_triangles.py`

### What is a triangle number?

A triangle number is the sum of all integers from 1 to `n`. For example:

```
triangle(4) = 4 + 3 + 2 + 1 = 10
```

### Approach: Recursion

The student's solution uses recursion (a function that calls itself):

```python
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)
```

It keeps calling itself with a smaller number until it hits the base case (`num == 1`).

### Bonus: Proving a square is two triangles

The file also shows that any square number can be expressed as the sum of two consecutive triangle numbers:

```
7² = 49 = triangle(7) + triangle(6) = 28 + 21
```

```python
def square(num):
    return triangle(num) + triangle(num - 1)
```

> The note in the file says the instructor's solution was exactly the same as the student's for this challenge!

---

## 07_04 – Drawing Shapes with Classes

**Files:**
- `07_04_drawing_shapes.py` ← student's solution
- `07_04_solution_drawing_shapes.py` ← 📌 instructor's solution

### What is the challenge?

The `Shape` parent class and the `Square` class were **given by the instructor** as starting code. The challenge was to use them as a reference and implement a `Triangle` class that draws a triangle made of `#` characters in the terminal — both a right-angled one and an equilateral-ish (centered/isosceles) one.

### Key concept: Inheritance

The parent class `Shape` defines the common structure (width, height, print character, and a `print()` method). Child classes **inherit** from it and only need to define `printRow()` — how each individual row looks. The `Square` class was provided as an example of how to do this.

### How does `print()` draw — top to bottom or bottom to top?

**Top to bottom.** The `print()` method loops `i` from `0` up to `height - 1`:

```python
def print(self):
    for i in range(self.height):
        self.printRow(i)  # i=0 is printed first → appears at the TOP
```

Since the terminal outputs each line sequentially downward, `i=0` is always the **top row** and `i=height-1` is always the **bottom row**. This means as `i` grows, so does the row — which is exactly why the triangle naturally grows from small at the top to wide at the bottom.

### Student's approach

The student implemented the `Triangle` class by printing `i` characters per row, where `i` is the row index:

```python
class Triangle(Shape):
    def printRow(self, i):
        print(self.printChar * i)
```

This produces a right-angled triangle, though the first row prints nothing (0 characters) since `i` starts at 0.

### Instructor's approach (solution)

The instructor's solution demonstrates two triangle variants:

**Triangle A – Right-angled triangle** (starts with 1 character on the first row):
```python
class TriangleA(Shape):
    def printRow(self, i):
        print(self.printChar * (i + 1))
```
Row `i` prints `i + 1` characters. Since `i` starts at 0 (top) and increases going down, the triangle grows naturally from top to bottom. The `+ 1` makes sure the very first row has 1 character instead of 0.

**Triangle B – Equilateral-ish (centered/isosceles) triangle:**
```python
class TriangleB(Shape):
    def printRow(self, i):
        triangleWidth = i * 2 + 1
        padding = int((self.width - triangleWidth) / 2)
        print(' ' * padding + self.printChar * triangleWidth)
```
Each row grows by 2 characters (`i * 2 + 1` gives 1, 3, 5, 7, 9...) and is padded with spaces on both sides to keep it centered. Again, because `i` increases top to bottom, the triangle naturally widens as it goes down — giving a symmetric, equilateral-ish shape.

---

## Quick Reference

| File | Type | Topic |
|---|---|---|
| `02_07_factorial.py` | Student + Instructor | Loops & Recursion |
| `03_06_conv_hex_dec.py` | Student | Strings & Math |
| `03_06_solution_one_conv_hex_dec.py` | 📌 Instructor | Strings & Math |
| `03_06_solution_two_conv_hex_dec.py` | 📌 Instructor | Strings, Loops & Math |
| `04_06_encode_ASCII_art.py` | Student attempt + 📌 Instructor | Loops & Lists |
| `05_04_faster_prime_finding.py` | Student | Loops & Math |
| `05_04_solution_faster_prime_finding.py` | 📌 Instructor | Loops & Math (optimized) |
| `06_04_sum_of_triangles.py` | Student (matches Instructor) | Recursion |
| `07_04_drawing_shapes.py` | Student (Shape & Square given by 📌 Instructor) | Classes & OOP |
| `07_04_solution_drawing_shapes.py` | 📌 Instructor | Classes & OOP |
