#include "lists.h"

/**
 * add_dnodeint_end - Adds a new node at the end of a dlistint_t list
 * @head: a double pointer to the head of the list
 * @n: an integer data for the new node
 * Return: address of the new element, NULL if fail
*/
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *current;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	/*Create a new node, set data to n, next pointer to NULL*/
	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{ /*If list is empty, set prev pointer to NULL*/
		new_node->prev = NULL;
		/*Update head of list to new node*/
		*head = new_node;
	}
	else
	{ /*If not empty, traverse list to find last node*/
		current = *head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		/*
		* Set to link next pointer of last node
		* and prev pointer of new node
		*/
		current->next = new_node;
		new_node->prev = current;
	}

	return (new_node);
}
