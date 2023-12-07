#include "lists.h"

/**
 * sum_dlistint - returns the sum of all the data (n)
 * of a dlistint_t linked list
 * @head: a pointer to the head of the list
 * Return: the sum of all the data (n) of the
 * list, 0 if the list is empty
*/
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current;
	int sum = 0;

	current = head; /*Traverse the list*/
	while (current != NULL)
	{ /*add data (n) of each node to a sum*/
		sum += current->n;
		current = current->next;
	}
	/*Return the sum*/
	return (sum);
}
