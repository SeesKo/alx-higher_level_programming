#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowptr = *head;
	listint_t *fastptr = *head;
	listint_t *prev = NULL;

	/* Empty list or single-node list is a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Move fast to the end and reverse the first half */
	while (fastptr != NULL && fastptr->next != NULL)
	{
		fastptr = fastptr->next->next;

		listint_t *next = slowptr->next;

		slowptr->next = prev;
		prev = slowptr;
		slowptr = next;
	}

	/* If the length is odd, skip the middle node */
	if (fastptr != NULL)
		slowptr = slowptr->next;

	/* Compare the reversed first half with the second half */
	while (prev != NULL && slowptr != NULL)
	{
		if (prev->n != slowptr->n)
			return (0); /* Not a palindrome */

		prev = prev->next;
		slowptr = slowptr->next;
	}

	return (1); /* Palindrome */
}
