# Barebones Compiler

--- 
## What is Bare Bones?
This Compiler is Used for the Bare Bones language from the book  <a href="https://www.amazon.co.uk/Computer-Science-Overview-Glenn-Brookshear/dp/0321544285/ref=sr_1_1?ie=UTF8&s=books&qid=1225741559&sr=8-1" target="_blank"> Computer Science: An Overview: International Edition by J. Glenn Brookshear</a>

---
### Language Breakdown
The Barebones language consists of 3 Simple Commands and 1 simple loop:
- clear
- incr
- name
- while

Clear Sets the value at the index of the identifier to zero.

incr increases the value stored at the identifier by one
whereas decr reduces it by one

---

the while loop is a while not loop, repeating the following instructions between the while and end untill the statement is true

`while name not 0 do;`
`...`
`...`
`end;`

---
## My Solution
### Storage of lines
At the start of the compilation, the compiler takes the address of the text file containing the Bare Bones code.

A stack is used to hold all code within the file, with each index corrosponding to a line/block of code. Where all indents and whitespaces before the line is removed
##### Storage of while loops

Within the code stack, after a while loop is found, all the proceding code is stored within the stack, along with the condition of the while loop (this is explained later)

Example:
`clear X;`
`incr X;`
`incr X;`
`incr X;`
`while X not 0 do;`
`   decr X;`
`end;`
The above code is stored in the stack like so:
`[clear x;, incr X;, incr X;, incr X;, [while X not 0 do;, decr X;, end;]]`

### Running the code
Once all the code has been added to the stack, the compiler will run the program using the function run().

Using a for loop to loop through all indexes of the stack, each line is checked for the command key & variable name.

After this, a switch statement is used to check the command and run the proceding code.

- clear:
    - The variable list is searched for the index of the identifier
    - If not found a Zero is appended to the Variable value's list and the identifier is appended to the variable list
    - If found the corrosponding index containing the value of the variable is set to zero

- incr:
    - Variable list is searched for index of the identifier
    - The index for variable's value is incremented
- decr:
    - Variable list is searched for index of the identifier
    - The index for variable's value is reduced by 1


- while:
    - Uses recursion, to allow for nested while loops
    - The Identifier & the condition is found.
    - Value of variable is checked to see if it is equal to the conditions value
    - if it is the while look breaks/stops
    - if not the while condition is temporarily removed from the index in the stack.
    - the new index for the stack is recursively run within the program (allowing for nested while loops)
    - the while loop condition is added back to the start of the index
        - This allows for nested while loops to be run again, after the origional while loop to loops back to the neted loop again.

--- 

### Why python?

I write code in mainly C++, and I haven't touched python in 3 years therefore I found it useful to relearn python and experement with what i already know

Also, python is a lazy language... and i honeslty CBA
You can find my even lazier attempt without thinking it though in firstAttempt.py

### Why Bare Bones
this challenge was completed for the first year, first semester module Space Cadets @ the University of Southampton