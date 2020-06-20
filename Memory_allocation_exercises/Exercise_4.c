// Program that eliminates blank spaces
// By: Luis Koh
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  
  int i, size = 0; // Variables
  char *original_string = calloc(1, 1); // Other variable initialized with 1 byte of memory
  printf("Type a string: "); // Ask for a string
  scanf("%[^\n]", original_string); // Save the string until reach the \n

  size = strlen(original_string); // Take the string size
  
  char *aux_string = calloc(size+1, 1); // Assigning 1 byte for each character + 1, in the dynamic
  									  // memory while the program is running

  memset(aux_string, '\n', size); // Sets in the pointer's memory a '\n' in each one of its data with the size int
  for(i = 0; i < size; i++){ // For that passes in all the characters
    if(original_string[i] == 32){ // If the character is equal to a blank space
      continue; // Continue
    } else{
      aux_string[i] = original_string[i]; // Else, save it on the auxiliary string
    }
  }

  for(i = 0; i < size; i++){ // For that passes each character in the string
    if(aux_string[i] != '\n'){ // if que chatacter is different to '\n'
      printf("%c", aux_string[i]); // print it
    }
  }
  
  // Free que dynamic memory used in both variables during the program
  free(aux_string);
  free(original_string);
  
  printf("\n"); 
}
