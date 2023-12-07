#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes a node at index
 * of dlistiint_t linked list
 * @head: a double pointer to head of list
 * @index: index of the node to delete, starts at 0
 * Return: 1 if succesful, -1 if it fails
*/
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current;
	unsigned int count = 0;

	if (head == NULL || *head == NULL)
	{
		return (-1);
	}
	current = *head;
	while (current != NULL)
	{
		if (count == index)
		{
			if (current->prev != NULL)
			{
				current->prev->next = current->next;
			}
			if (current->next != NULL)
			{
				current->next->prev = current->prev;
			}
			if (count == 0)
			{
				*head = current->next;
			}
			free(current);
			return (1);
		}
		current = current->next;
		count++;
	}

	return (-1);
}
