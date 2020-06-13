/* Exercise 13-2: Write a function that takes a single string as its
argument and returns a pointer to the first nonwhite character
in the string. */
#include <stdio.h>
#include <ctype.h>
char *take_nonwhite(char *string); // Function prototype

int main(){ // Function main
char word[] = "      Luis Koh"; // Variable

printf("The first nonwhite character is: %c\n",*take_nonwhite(word)); // Printing and calling the function

  return 0; // Ending the conde
}

char *take_nonwhite(char *string){ // Function with pointer taking the value of the word
int i; // Iterator
for(i=0;i<sizeof(string);i++){ // Pass through each character in the string
  if (string[i] != ' '){ // When this reach a nonwhite space
    return &string[i]; // Returns the value
  }
}
 return &string[i]; // Returns the value
}

