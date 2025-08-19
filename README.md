# Logic-Building

This repository will contain tasks that I will complete to improve my Logic Building.
<details>
## <summary> 🧩 Day-1: Pattern Problems  </summary>
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
</details>

<details>
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
</details>

<details>
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
</details>

