/* Exercise 13-1: Write a program that uses pointers to set each element
of an array to zero. */
#include <stdio.h>
#define NUMBERS 6 // Defining the size of the array

int main(){ // Function main
  int numbers[NUMBERS] = {6,5,4,3,2,1}; // Variable array of numbers
  int *p_numbers; // Variable pointer
  int i; // Counter

  for(p_numbers = &numbers[0];p_numbers < &numbers[NUMBERS];p_numbers++){
  /*
  p_numbers = &numbers[0] <- Here I'm pointing to the value of each of the 6 numbers in the array
  p_numbers < &numbers[NUMBERS] <- I'm checking if the value of the variable has reach 6 (Total)
  p_numbers++ <- Adding 1 to the variable
  */
    *p_numbers = 0; // Giving the value of zero to each number in the array
  }
  
  for(i=0;i<NUMBERS;i++){ // For loop to print the values
    printf("The number [%i] is: %i\n",i,numbers[i]); // output
  }

  return 0;
}
