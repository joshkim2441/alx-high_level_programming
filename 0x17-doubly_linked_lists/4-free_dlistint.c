#include "lists.h"

/**
 * free_dlistint - Frees a dlistint_t list
 * @head: a pointer to the head of the list
*/
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	while (head != NULL)
	{ /*Traverse the list freeing each visited node*/
		current = head; /*Keep pointer to current node*/
		head = head->next; /*Move head pointer to next node*/
		free(current); /*Free current node*/
	/*
	* To ensure it doesn't lose reference to next node after
	* freeing current node
	*/
	}
}
