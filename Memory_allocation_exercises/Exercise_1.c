// Program that counts the letters of a string
// By: Luis Koh
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){ // Function main
	int longitude, i, counter = 0; // Variables
	char characters_chain[100], *characters_chain_ptr; // Variables
	
	printf("Type a chain of characters to count the letters: "); // Ask for a string
	fgets(characters_chain,100,stdin); // Save string into variable 
	
	longitude = strlen(characters_chain); // Take the longitude of the string
	
	// Save a memory space with the number of characters in the string and take them
	// in variable characters_chain_ptr
	characters_chain_ptr = calloc(strlen(characters_chain) + 1,sizeof(char));
	
	//After that, copy the string into the new variable with the memory space separated
	strcpy(characters_chain_ptr, characters_chain);
	
	for(i=0;i<longitude;i++){ // For that passes in all the characters
		if(isalpha(characters_chain_ptr[i])){ //If the character is a letter
			counter++; // Add counter 1
		}	
	}
	printf("The total of letters in the string is: %i",counter); // Finally prints the result
	free(characters_chain_ptr); // And free the dynamic memory space used
	
	return 0;
}
