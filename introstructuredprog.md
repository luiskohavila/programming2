# Team:

### Luis Fernando Koh Avila:
https://github.com/luiskohavila/programming2
### Matthew Esquivel Brandt:
https://github.com/Git-Mekbot/programming2

# Unit 1: Structured Programming

## Classification of Programming Paradigms

### Programming paradigm:
Are a way to classify programming languages based on their features.

### Declarative

- [Functional](https://www.computerhope.com/jargon/f/functional-programming.htm):
Programming paradigm where programs are constructed by applying and composing functions.

- [Dataflow](https://www.computerhope.com/jargon/d/dataflow-programming.htm):
Programming paradigm that models a program as a directed graph of the data flowing between operations, thus implementing data flow principles and architecture.

- [Logic, Constraint-based](https://www.computerhope.com/jargon/l/logic-programming.htm):
Programming paradigm in which program statements express facts and rules about problems within a system of formal logic.

- Template-based:
Programming paradigm in which programs are constructed by using pre built templates.

- Structured:
Programming paradigm aimed at improving the clarity, quality, and development time of a computer program by making extensive use of the structured control flow constructs of selection and repetition, block structures, and subroutines.

### Imperative

- [Von Neumann](https://www.computerscience.gcse.guru/theory/von-neumann-architecture):
Is based on the stored-program computer concept, where instruction data and program data are stored in the same memory.  This design is still used in most computers produced today.

- [Interpreted (Scripting)](https://www.computerhope.com/jargon/s/script.htm):
Is a computer language with a series of commands within a file that is capable of being executed without being compiled.

- [Object-oriented](https://www.computerhope.com/jargon/o/oop.htm):
It is a programming language paradigm. In an object-oriented program, the code can be structured as reusable components, some of which may share properties or behaviors.

### [Implementation methods](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/)

Interpreted Programming:
- Directly execute source language program
- Fetch source program, decode it, execute it
- Interpreter executes while program executing

Compiled Programming:
- Translate program from source language to target language
- Program in target language is then executed
- Compiler finished before program executed

## Data Representations and Operators

### [Programming languages](https://javarevisited.blogspot.com/2018/08/5-programming-language-every-programmer-learn.html)
Formal languages, which comprise a set of instructions that produce various kinds of output.
Examples:
- Python
- Java
- C
- JavaScript
- Scala

### [Spaghetti Code](https://www.urbandictionary.com/define.php?term=spaghetti%20code)
It is code which flagrantly violates the principles of structured, procedural programming. Usually this means using lots of GOTO statements hence the term, which suggests the tangled and arbitrary nature of the program flow.

### [Sequential Algorithms](https://www.sciencedirect.com/topics/computer-science/sequential-algorithm)
Algorithm that is executed sequentially once through, from start to finish, without other processing executing as opposed to concurrently or in parallel.

### [Source Code](https://searchapparchitecture.techtarget.com/definition/source-code)
Collection of code, possibly with comments, written using a human-readable programming language, usually as plain text.

### Data Representation in Structured Programming Language

- [Identifiers](http://aboutc.weebly.com/identifiers.html):
An identifier is a string of alphanumeric characters that begins with an alphabetic character or an underscore character that are used to represent various programming elements such as variables, functions, arrays, structures, unions and so on. Actually, an identifier is a user-defined word.

- [Variables](https://www.kidscodecs.com/variables/):
Variables are names used to hold one or more values. Instead of repeating these values in multiple places in your code, the variable holds the results of a calculation, database call, results of a database query, or other value. Instead of multiple calculations or the load of multiple database calls to retrieve the same data, the variable is stored in computer memory once and used wherever it is needed in your code. We cannot use keywords as a name of our variable.

- [Constants](https://press.rebus.community/programmingfundamentals/chapter/constants-and-variables):
A constant is a data item whose value cannot change during the program’s execution. Thus, as its name implies – the value is constant.
Constants are used in two ways. They are:
    - Literal constant
    - Defined constant

|  Language  |                     Example                     |
|:----------:|:-----------------------------------------------:|
|      C     | #define PI 3.1416                               |
|     C#     | const double PI = 3.14159;                      |
|     C++    | #define PI 3.1416 or const double PI = 3.14159; |
|    Java    | const double PI = 3.14159;                      |
| JavaScript | const PI = 3.14159;                             |
|   Python   | PI = 3.14159                                    |

- [Reserved Words](https://www.datamentor.io/r-programming/reserved-words/):
Words that are reserved by a program because the word has a special meaning. Reserved Words can be commands or parameters. Every programming language has a set of keywords that cannot be used as variable names.

- Types of Data:

#### 32 bit computer
| Data type | Size |                          Range                          |
|:---------:|:----:|:-------------------------------------------------------:|
|    char   |   1  |                       -128 to 127                       |
|   short   |   2  |                    -32,768 to 32,767                    |
|    int    |   4  |             -2,147,483,648 to 2,147,483,647             |
|    long   |   4  |             -2,147,483,648 to 2,147,483,647             |
| long long |   8  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
|   float   |   4  |                       -3.4E +/- 38                      |
|   double  |   8  |                       1.7E +/- 308                      |

#### 64 bit computer
| Data type | Size |                          Range                          |
|:---------:|:----:|:-------------------------------------------------------:|
|    char   |   1  |                       -128 to 127                       |
|   short   |   2  |                    -32,768 to 32,767                    |
|    int    |   4  |             -2,147,483,648 to 2,147,483,647             |
|    long   |   4  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| long long |   8  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
|   float   |   4  |                       -3.4E +/- 38                      |
|   double  |   8  |                       1.7E +/- 308                      |


- [Data Type Conversion](https://docs.actian.com/ingres/11.0/index.html#page/EmbedSQL/Data_Type_Conversion.htm):
Data type conversion occurs automatically for different numeric types such as from floating-point database column values into integer C variables, and for character strings, such as from varying-length Ingres character fields into fixed-length C character string buffers.

### Operators of Structured Programming Language

- [Conditional](https://www.dotnettricks.com/learn/c/conditional-statements-if-else-switch-ladder):
Conditional statements help you to make a decision based on certain conditions. These conditions are specified by a set of conditional statements having boolean expressions which are evaluated to a boolean value true or false.

If statement: The single if statement in C language is used to execute the code if a condition is true.
    - If the expression is evaluated to nonzero (true) then if block statement(s) are executed.
    - If the expression is evaluated to zero (false) then Control passes to the next statement following it.

If-Else statement: The if-else statement in C language is used to execute the code if condition is true or false.
    - If the expression is evaluated to nonzero (true) then if block statement(s) are executed.
    - If the expression is evaluated to zero (false) then else block statement(s) are executed.

If-Else If ladder: The if-else-if statement is used to execute one code from multiple conditions. It is a chain of if..else statements in which each if statement is associated with else if statement and last would be an else statement.

Switch statement: Is used to test a list of cases. A switch statement contains one or more case labels which are tested against the switch expression. When the expression matches a case then the associated statements with that case would be executed.

- [Logical](https://press.rebus.community/programmingfundamentals/chapter/logical-operators/):

|  Language  | AND |  OR  | NOT |
|:----------:|:---:|:----:|:---:|
|      C     |  && | \|\| |  !  |
|     C++    |  && | \|\| |  !  |
|     C#     |  && | \|\| |  !  |
|    Java    |  && | \|\| |  !  |
| JavaScript |  && | \|\| |  !  |
|   Python   | and |  or  | not |

#### Logical And(&&)
| x     | y     | x and y |
|:-----:|:-----:|:-------:|
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

#### Logical Or(||)
| x     | y     | x or y |
|:-----:|:-----:|:------:|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

#### Logical Not(!)
|   x   | not x |
|:-----:|:-----:|
| False |  True |
|  True | False |

- [Relationship](https://press.rebus.community/programmingfundamentals/chapter/relational-operators/):
An operator that gives a Boolean value by evaluating the relationship between two operands. These include numerical equality and inequalities.

| Operator |          Meaning          |
|:--------:|:-------------------------:|
|     <    |         less than         |
|     >    |        greater than       |
|    <=    |   less than or equal to   |
|    >=    |  greater than or equal to |
|    ==    |    equality (equal to)    |
| != or <> | inequality (not equal to) |

### [Basic Functions of Input & Output](https://www.studytonight.com/c/c-input-output-function.php)
- Input: Input means to provide the program with some data to be used in the program
	- scanf: Save a value specifying the type of data with an %, and them the name of the variable with after an &
	- gets: It is used to get a string
	- puts: Writes the string str and a trailing newline to stdout.

- Output: Output means to display data on screen or write the data to a printer or a file.
	- printf: Function returns the number of characters printed by it

## Version Control

### [Distributed Version Control](https://www.perforce.com/blog/vcs/what-dvcs-anyway)

In software development, distributed version control is a form of version control in which the complete codebase, including its full history, is mirrored on every developer's computer.
- Advantages:
    - Branching and merging can happen automatically and quickly
    - Developers have the ability to work offline
    - Multiple copies of the software eliminate reliance on a single backup
- Most popular types of version control:
    - Helix Core (Perforce)
    - Git
    - SVN
    - ClearCase
    - Mercurial
    - TFS

 
#### Steps to make a commit
 ```
 git init
 git add *
 git commit -m "first commit"
 git push -u origin master
 ```
### Branches
![How does it work](https://miro.medium.com/max/1000/1*8c7mfzA9kVjVYuTbQm4Lcg.png)

