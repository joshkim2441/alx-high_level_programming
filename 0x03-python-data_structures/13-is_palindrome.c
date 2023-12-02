#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to head a a singly linked list
 * Return: 0 if not a palindrome, 1 if is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	prev = NULL;
	while (next != NULL)
	{
		slow = next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
	}
	*head = prev;

	return (is_palindrome);
}
