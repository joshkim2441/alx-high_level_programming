#include "lists.h"

/**
 * insert_mode - inserts a number into a sorted sinlgy linked list
 * @head: a pointer to the head pointer
 * @number: the inserted number
 * Return: the address of the new node, NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new)
		return (NULL);

	new->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	new->next = NULL;
	current->next = new;

	return (new);
}