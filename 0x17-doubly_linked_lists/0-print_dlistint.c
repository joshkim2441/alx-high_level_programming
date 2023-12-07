#include "lists.h"

/**
 * print_dlistint - Prints all elements of a dlistint list
 * @h: a pointer to head of the list
 * Return: the number of nodes in the list
*/
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t count = 0;

	current = h;
	while (current != NULL)
	{ /*traverse the list, printing the data (n) of each node*/
		printf("%d\n", current->n);
		current = current->next;
		/*Increment the counter*/
		count++;
	}
/*Return the count which is the number if nodes in the list*/
	return (count);
}
