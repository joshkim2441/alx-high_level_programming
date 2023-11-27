#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *walk, *run;

	if (!list)
	return (0);

	walk = list;
	run = list->next;

	while (walk && run && run->next)
	{
		if (walk == run)
			return (1);

		walk = walk->next;
		run = run->next->next;
	}
	return (0);
}
