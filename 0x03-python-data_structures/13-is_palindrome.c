#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1); /* Empty list or single-node list is a palindrome */

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	/* Move fast to the end and reverse the first half */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *next = slow->next;

		slow->next = prev;
		prev = slow;
		slow = next;
	}

	/* If the length is odd, skip the middle node */
	if (fast != NULL)
		slow = slow->next;

	/* Compare the reversed first half with the second half */
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0); /* Not a palindrome */

		prev = prev->next;
		slow = slow->next;
	}

	return (1); /* Palindrome */
}
