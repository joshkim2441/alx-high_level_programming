#include "lists.h"

/**
 * get_dnodeint_at_index - Returns the nth node of a dlistint_t linked list
 * @head: a pointer to the head of the list
 * @index: index of the node starting from 0
 * Return: the nth node of the list, NULL if it doesn't exist
*/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current;
	unsigned int count = 0;

	current = head;
	while (current != NULL)
	{ /*Traverse the list*/
		if (count == index)
		{ /*When counter equals index, return current node*/
			return (current);
		}
		current = current->next;
		count++; /*Increment counter*/
	}

	return (NULL);
}
