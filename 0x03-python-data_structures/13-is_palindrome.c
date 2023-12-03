#include "lists.h"

int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        /* An empty list or a list with a single element is considered a palindrome */
        return 1;
    }

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;

    /* Use Floyd's Tortoise and Hare algorithm to find the middle of the list */
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        /* Reverse the first half of the list */
        listint_t *temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* If the length of the list is odd, move slow to the next node */
    if (fast != NULL) {
        slow = slow->next;
    }

    /* Compare the reversed first half with the second half */
    while (slow != NULL) {
        if (prev->n != slow->n) {
            return 0;  /* Not a palindrome */
        }
        prev = prev->next;
        slow = slow->next;
    }

    return 1;  /* It is a palindrome */
}
