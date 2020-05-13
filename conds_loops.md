# Team:

### Luis Fernando Koh Avila:
https://github.com/luiskohavila/programming2
### Matthew Esquivel Brandt:
https://github.com/Git-Mekbot/programming2

# Unit 2: Control Structures

## Selective Control Structures

### Simple conditional

A simple conditional statement checks to see if one condition is true.

```
if(condition test) {
	//Statements to be executed repeatedly
}
```

### Double conditional

Double conditional structures allow you to choose between two options or possible alternatives depending on whether or not a certain condition is fulfilled.

```
if(condition test) {
	//Statements to be executed repeatedly
}
Else {
	//Statements to be executed repeatedly
}
```

### Multiple conditional 

Multiple conditionals are specialized decision making that allow comparing a variable against different possible results, executing for each case a series of specific instructions.

```
if(condition test) {
	//Statements to be executed repeatedly
}
else if(condition test) {
	//Statements to be executed repeatedly
}
else {
	//Statements to be executed repeatedly
}
```

### Nested conditional

```
if(condition test) {
if(condition test) {
		//Statements to be executed repeatedly
}
//Statements to be executed repeatedly
}
```

We say that a conditional structure is nested when there is another conditional structure inside the true or false branch of the first conditional structure.

## Iterative control structures

Describe concepts and characteristics of iterative control structures in algorithm coding: 

### Iteration

Is a process wherein a set of instructions or structures are repeated in a sequence a specified number of times or until a condition is met.
 
### For 

Control flow statement for specifying iteration, which allows code to be executed repeatedly.

```
for(initialization ; condition test ; update){
	//Statements to be executed repeatedly
}
```

### Nested For

A nested loop is a loop that is included in the statement block of another for loop. Loops can have any level of nesting (one loop within another loop within a third, etc.). Can be used to fill values in a matrix: 
```
  for(i=0;i<Ar;i++){
      for(j=0;j<Ac;j++){
          printf("(%d, %d): ",i+1, j+1);
          scanf("%d", &A[i][j]);
      }
  }
```
### While 

Control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
```
while (condition test)
{
      //Statements to be executed repeatedly 
      // Increment (++) or Decrement (--) Operation
}
```

### Do-While 

Control flow statement that executes a block of code at least once, and then repeatedly executes the block, or not, depending on a given boolean condition at the end of the block.

```
do
{
    //Statements 

}while(condition test);
```

### Break Instructions 

![break](https://www.tutorialspoint.com/cprogramming/images/cpp_break_statement.jpg)

Statement that breaks the loop one by one, i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops.

### Continue Instructions

![continue](https://www.tutorialspoint.com/cprogramming/images/cpp_continue_statement.jpg)

The continue statement skips the current iteration of a for, while , or do-while loop. The unlabeled form skips to the end of the innermost loop's body and evaluates the boolean expression that controls the loop.

