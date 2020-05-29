# Team:

### Luis Fernando Koh Avila:
https://github.com/luiskohavila/programming2
### Matthew Esquivel Brandt:
https://github.com/Git-Mekbot/programming2

# Unit 3: Subprograms and Recursion

## [Subprograms](https://courses.washington.edu/css342/zander/css332/passby.html)

### Parameters in C functions
A Parameter is the symbolic name for "data" that goes into a function. There are two ways to pass parameters in C: Pass by Value, Pass by Reference.

### By Value:
It means to make a copy in memory of the actual parameter's value that it is passed in, a copy of the contents of the actual parameter, this is used when we are only “using” the parameter for computation instead of changing it for the client program.

### By Reference
Also called “By Address” is a copy of the address of where the actual parameter is stored and it’s used when changing the parameter passed by the client program.

There are two ways to make a pass by reference parameter:

 **ARRAYS:**

- Arrays are always passed by reference in C. Any change made to the parameter containing the array will change the value of the original array.

**The ampersand used in the function prototype.**

- function  **(& parameter_name )**

- To make a normal parameter into a pass by reference parameter, we use the "& param" notation. The ampersand (&) is the syntax to tell C that any changes made to the parameter also modify the original variable containing the data.

## [Recursion](https://www.geeksforgeeks.org/recursion/)
It’s the process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.

### Direct
If a function calls itself, it's known as direct recursion. This results in a one-step recursive call: the function makes a recursive call inside its own function body.
```
// An example of direct recursion
void directRecFun()
{
    // Some code....

    directRecFun();

    // Some code...
}
```

### Indirect
Indirect recursion occurs when a function is called not by itself but by another function that it called (either directly or indirectly).
```
// An example of indirect recursion
void indirectRecFun1()
{
    // Some code...

    indirectRecFun2();

    // Some code...
}
void indirectRecFun2()
{
    // Some code...

    indirectRecFun1();

    // Some code...
}
```

