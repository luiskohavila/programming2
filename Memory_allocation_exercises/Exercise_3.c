// Function that returns the maximum value of an array of numbers.
// By: Luis Koh
#include <stdio.h>
#include <stdlib.h>

int functionmax(int number[],int longitude); // Function prototype

int main(){
  int longitude, *numbers_ptr,i; // Variables
  printf("How many numbers do you want?: "); // Ask for the number of elements
  scanf("%d",&longitude); // Then, save it in longitude
  numbers_ptr = malloc(longitude*sizeof(int)); // Assign a memory space in the memory multiplying
  											  // the longitude by the size of an integer  
  printf("Type the values: \n"); // Ask for values
  for(i=0;i<longitude;i++){ // Pass trough all the values in the memory
  	  printf("Number %i: ",i+1); // And ask for each value
	  scanf("%d",numbers_ptr+i); // Save it on the variable as an array
  }

  printf("The max number is: %i\n",functionmax(numbers_ptr,longitude)); // Calling the function
  free(numbers_ptr); // And free the dynamic memory space used
  return 0;
}

int functionmax(int number[],int longitude){ // Function
  int i, max; // Variables
  max = 0; // Defining the first element as the highest
  for (i=0;i<longitude;i++){ // Checking every character in the array
    if (number[i] > max){ // If other character is greather than the max
      max = number[i]; // Save it on the variable max
    }
  }
  return max; // Return to the function main the maximum value
}
