#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at given position
 * @h: a double pointer to head of list
 * @idx: index of list where new node is added, starts at 0
 * @n: the integer data for the new node
 * Return: address of the new element, NULL if failed
*/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node;
	dlistint_t *current;
	unsigned int count = 0;

	if (h == NULL)
	{
		return (NULL);
	}

	if (idx == 0)
	{ /*add a new node at beginning of list*/
		return (add_dnodeint(h, n));
	}

	current = *h;
	while (current != NULL)
	{
		if (count == idx)
		{
			new_node = malloc(sizeof(dlistint_t));
			if (new_node == NULL)
			{
				return (NULL);
			}
			new_node->n = n;
			new_node->prev = current->prev;
			new_node->next = current;
			current->prev->next = new_node;
			current->prev = new_node;
			return (new_node);
		}
		current = current->next;
		count++;
	}
	if (count == idx) /*If index is equal to number of nodes in list*/
	{ /*add a new node at the end of the list*/
		return (add_dnodeint_end(h, n));
	}
	/*If index is greater than number of nodes in list*/
	return (NULL);
}
