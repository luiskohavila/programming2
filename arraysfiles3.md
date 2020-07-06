# Team:

### Luis Fernando Koh Avila:
https://github.com/luiskohavila/programming2
### Matthew Esquivel Brandt:
https://github.com/Git-Mekbot/programming2

# Unit 4: Arrays and Files

## [Classification of Arrays]

### [Concepts and characteristics of arrangements](https://overiq.com/c-programming-101/one-dimensional-array-in-c/#:~:text=Arrays%20can%20be%20single%20or,array%20or%202%2DD%20array.)
An array is a collection of one or more values of the same type. Each value is called an element of the array. The elements of the array share the same variable name but each element has its own unique index number (also known as a subscript). 
An array can be of any type, For example: int, float, char etc. If an array is of type int then it’s elements must be of type int only.

- One dimensional array: Conceptually you can think of a one-dimensional array as a row, where elements are stored one after another.

![onearray](https://study.com/cimages/multimages/16/1223543576347.png)

```
// Example program to find the average of n numbers using onedimentional arrays

#include <stdio.h>
int main()
{
     int marks[10], i, n, sum = 0, average;

     printf("Enter number of elements: ");
     scanf("%d", &n);

     for(i=0; i<n; ++i)
     {
          printf("Enter number%d: ",i+1);
          scanf("%d", &marks[i]);
          
          // adding integers entered by the user to the sum variable
          sum += marks[i];
     }

     average = sum/n;
     printf("Average = %d", average);

     return 0;
}
```

- Multidimensional: A multi-dimensional array is an array that has more than one dimension having multiple levels. The simplest multi-dimensional array is the 2D array, or two-dimensional array. It's technically an array of arrays
![multiarrray](https://cdn.programiz.com/sites/tutorial2program/files/two-dimensional-array_0.jpg)

```
printf("Type the values in the matrix A\n");
  int A[Ar][Ac], B[Br][Bc], C[Ar][Bc];
  int i, j, k;
  //Find each row
  for(i=0;i<Ar;i++){
  	  //Find each column
      for(j=0;j<Ac;j++){
      	  //Ask for values
          printf("(%d, %d): ",i+1, j+1);
          //Save the values
          scanf("%d", &A[i][j]);
      }
  }
```
## [Organization and Management of Files](https://www.computerhope.com/jargon/f/file.htm)

A file is an object on a computer that stores data, information, settings, or commands used with a computer program.

### Concepts and characteristics of dataflow
Dataflow programming is a programming paradigm that models a program as a directed graph of the data flowing between operations, thus implementing dataflow principles and architecture.

### Concepts and characteristics of files
- Text: A text file is a computer file that only contains text and has no special formatting such as bold text, italic text, images, etc.

- Binaries: A binary file is a computer file that is not a text file. The term "binary file" is often used as a term meaning "non-text file".

### [Characteristics of file managements](https://www.geeksforgeeks.org/basics-file-handling-c/)
- Creation: A file is created using a software program on the computer.
- Opening, Close: A file can be opened to show its contents or closed to hide them.
- Reading, Writing: Files can be read, as in extracting information from them, or written, as in information is being added onto them.
- Query: A query is a request for data or information from a database table or combination of tables.
- Modification: There are multiple ways to modify a file, such as writing, appending, reading, copying, searching, renaming, deleting and even moving said file.

### File opening parameters in C
- “r”:
Search file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the first character in it. If the file cannot be opened fopen( ) returns NULL.
- “w”:
Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
- “a”:
Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer that points to the last character in it. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
- “r+”:
Searches file. If is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the first character in it. Returns NULL, if unable to open the file.
- “w+”:
Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist a new file is created. Returns NULL, if unable to open file.
- “a+”:
Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the last character in it. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
```
// Example of C program to illustrate fopen() 
  
#include <stdio.h> 
#include <stdlib.h> 
  
int main() 
{ 
  
    // pointer demo to FILE 
    FILE* demo; 
  
    // Creates a file "demo_file" 
    // with file access as write-plus mode 
    demo = fopen("demo_file.txt", "w+"); 
  
    // adds content to the file 
    fprintf(demo, "%s %s %s", "Welcome", 
            "to", "my world"); 
  
    // closes the file pointed by demo 
    fclose(demo); 
  
    return 0; 
} 
```

