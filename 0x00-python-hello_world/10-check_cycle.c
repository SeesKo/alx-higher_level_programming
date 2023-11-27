#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slowptr, *fastptr;

	/* Check if list is empty or has 1 node only (no cycle) */
	if (list == NULL || list->next == NULL)
		return (0);

	/* Initailize both slow and fast moving pointers */
	slowptr = list->next; /* slowptr moves 1 step at a time */
	fastptr = list->next->next; /* fastptr moves 2 steps at a time */

	/* Iterate till fastptr reaches end of */
	/* the list or a cycle is detected */
	while (fastptr != NULL && fastptr->next != NULL)
	{
		/* If the 2 pointers meet, a cycle is detected */
		if (slowptr == fastptr)
			return (1);

		/* Moving the slowptr by 1 step */
		slowptr = slowptr->next;

		/* Moving the fastptr by 2 steps */
		fastptr = fastptr->next->next;
	}

	/* If no cycle is detected */
	return (0);
}
