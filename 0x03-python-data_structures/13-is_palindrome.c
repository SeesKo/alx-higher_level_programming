#include "lists.h"

/**
 * reverse_list - Reverses a linked list in place.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowptr = *head;
	listint_t *fastptr = *head;
	listint_t *second_half = NULL;
	listint_t *temp = NULL;

	/* Find the middle of the linked list */
	while (fastptr != NULL && fastptr->next != NULL)
	{
		slowptr = slowptr->next;
		fastptr = fastptr->next->next;
	}

	/* Reverse the second half of the linked list */
	second_half = reverse_list(slowptr);
	temp = second_half;

	/* Compare the first half and reversed second half */
	while (*head != NULL && temp != NULL)
	{
		/* Not a palindrome */
		if ((*head)->n != temp->n)
			return (0);

		*head = (*head)->next;
		temp = temp->next;
	}

	/* It is a palindrome */
	return (1);
}
