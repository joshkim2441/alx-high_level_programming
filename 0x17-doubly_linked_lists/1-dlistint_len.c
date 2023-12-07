#include "lists.h"

/**
 * dlistint_len - Returns number of elements in a dlistint_t list
 * @h: a pointer to the head of the list
 * Return: number of elements in list
*/
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t count = 0;

	current = h;
	/*Traverse the list*/
	while (current != NULL)
	{
		current = current->next;
		/*Increment the counter*/
		count++;
	}
	/*Return the number of nodes in the list*/
	return (count);
}
