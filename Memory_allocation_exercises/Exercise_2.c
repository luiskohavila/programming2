// Program that calculates the leap year for a given range
// By: Luis Koh
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int *year; // Pointer year
	int i,j; // Iterators
	int aux = 1500; // Auxiliar
	
	// Give to year a space of 600 ints in the dynamic memory
	// when programming is running
	year = malloc(600*sizeof(int));
	
	for(i=0;i<600;i++){ // Pass trough all the values in the memory
		year[i] = aux; // And gives to year the value of the auxiliar
		aux++; // Then add one to the auxiliar
	}

	for (j=0;j<600;j++) // Pass trough all the values in the memory on year variable
	{
		if((year[j]%400==0)||(year[j]%4==0 && year[j]%100!=0)){ //The conditions
		printf("%d\n",year[j]); // If it is leap year, print it
		}
	}
	free(year); // And free the dynamic memory space used
}
