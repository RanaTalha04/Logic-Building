# Logic-Building

This repository will contain tasks that I will complete to improve my Logic Building.
<details>

## Week 1
## <summary>🧩 Day-1: Pattern Problems</summary>
### Problem 1: Right Triangle Star Pattern

Statement: Print a right-angled triangle of * of size n.

### Problem 2: Inverted Right Triangle
Statement: Print a inverted right-angled triangle of * of size n.

### Problem 3: Number Triangle

Statement: Print a numbered triangle of size n.

### Problem 4: Pyramid Pattern

Statement: Print a pyramid pattern of * of size n.


### Problem 5: Diamond Pattern

Statement: Print a Diamond pattern of * of size n.

## <summary> 🧩 Day-2: String & Number Reversal  </summary>
### 🔹 Task 1: Reverse a String (without built-ins)

#### Problem:
Take a string as input and print it in reverse without using [::-1] or reversed().

#### Example:

Input: "python"
Output: "nohtyp"


#### Hint:

Use a loop from last index to first.

Build a new string step by step.

### 🔹 Task 2: Reverse a Number (without string conversion)

#### Problem:
Take a number as input and reverse it.

#### Example:

Input: 12345
Output: 54321


#### Hint:

Use % 10 to get last digit.

Use // 10 to remove last digit.

Multiply reversed number by 10 and add digit.

### 🔹 Task 3: Palindrome String

#### Problem:
Check if a string is palindrome (same forwards & backwards).

#### Example:

Input: "madam" → Output: Palindrome  
Input: "hello" → Output: Not Palindrome


#### Hint:

Compare string with its reverse (manual).

### 🔹 Task 4: Palindrome Number

#### Problem:
Check if a number is palindrome.

#### Example:

Input: 121 → Palindrome
Input: 123 → Not Palindrome


#### Hint:

Reuse Task 2 logic (reverse number).
Compare reversed with original.

### 🔹 Task 5: Word Reversal in Sentence

#### Problem:
Take a sentence and reverse the order of words.

#### Example:

Input: "I love Python"
Output: "Python love I"

#### Hint:

Use split() to break into words.
Reverse using loop (avoid [::-1]).

## <summary> 🧩 Day-3: Palindrome & Word Reversal </summary>
### 🔹 Task 1: Palindrome Sentence (Ignore Spaces)

#### Problem:
Check if a sentence is palindrome when spaces are ignored.

#### Example:
Input: "nurses run"
Output: Palindrome


#### Hint:
Remove spaces first (replace(" ", "")).
Then apply palindrome logic like Task 2.

### 🔹 Task 2: Longest Palindrome Word in Sentence
#### Problem:
Find the longest palindrome word in a given sentence.

#### Example:
Input: "I saw madam at noon"
Output: "madam"


#### Hint:
Split sentence into words.
Check each word if it’s a palindrome.
Track the longest one.

## <summary> 🧩 Day-4: Factorial, Fibonacci sequence </summary>
### 🔹 Task 1: Factorial of a Number

#### Problem:
Write a function that takes a number n as input and returns its factorial.

#### Example:
Input: 5
Output: 120

#### Hint:
Factorial of a number n is the product of all integers from 1 to n.
By definition, 0! = 1.

### 🔹 Task 2: Fibonacci Sequence
#### Problem:
Write a function that generates the first n terms of the Fibonacci sequence.

#### Example:
Input: 7
Output: [0, 1, 1, 2, 3, 5, 8]

#### Hint:
Fibonacci sequence starts with 0, 1.
Each next term is the sum of the previous two terms.

## <summary> 🧩 Day-5: Armstrong & Perfect Numbers </summary>
### 🔹 Task 1: Armstrong Number
#### Problem:
Write a function that takes a number n as input and checks if it is Armstrong number or not.

#### Example:
Input: 153

Explanation:
1^3 + 5^3 + 3^3 = 153

Output: Armstrong

#### Hint:
A number is called an Armstrong number if the sum of its digits each raised to the power of the number of digits equals the number itself.

### 🔹 Task 2: Fibonacci Sequence
#### Problem:
Write a function that takes a number n as input and checks if it is Perfect number or not.

#### Example:
Input: 28
Divisors: 1 + 2 + 4 + 7 + 14 = 28
Output: Perfect

#### Hint:
A number is called a Perfect number if the sum of its proper divisors (excluding itself) is equal to the number.
</details>

## <summary> 🧩 Day-6: Prime Numbers </summary>
### 🔹 Task 1: Check Prime Number
#### Problem:
Write a function that takes a number n as input and checks if it is a Prime number or not.

#### Example:
Input: 3
Output: Prime

#### Hint:
A prime number is a whole number greater than 1 that has only two factors (divisors): 1 and the number itself

### 🔹 Task 2: Print Sum of n Prime numbers
#### Problem:
Write a function that takes n prime numbers as input and returns the sum of these n numbers.

#### Example:
Input: 3
[2, 3, 5]
Output: 10



## <summary> 🧩 Day-7: Mini Project - Number Guessing Game </summary>
#### Problem:
Write a program where:
. The computer randomly selects a number between 1 and 100.
. The user has to guess the number.
. After each guess, the program tells the user whether their guess is too high, too low, or correct.
. The game continues until the user guesses correctly.
. (Bonus) Limit the number of attempts and show how many tries the user took.

</details>