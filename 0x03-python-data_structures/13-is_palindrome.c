#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: A pointer to a pointer to the head of the linked list
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1); /* An empty list or list with one element is a palindrome */

    listint_t *fast, *reverse, *mid_reverse;
    size_t size = 0, i;

    /* Count the number of nodes in the list */
    fast = *head;
    while (fast)
    {
        size++;
        fast = fast->next;
    }

    /* Find the middle node of the list */
    fast = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        fast = fast->next;

    /* If the number of nodes is even and the middle nodes are different, not a palindrome */
    if ((size % 2) == 0 && fast->n != fast->next->n)
        return (0);

    fast = fast->next->next;

    /* Reverse the second half of the list */
    reverse = reverse_listint(&fast);
    mid_reverse = reverse;

    fast = *head;

    /* Compare the values of the first half and the reversed second half */
    while (reverse)
    {
        if (fast->n != reverse->n)
            return (0);
        fast = fast->next;
        reverse = reverse->next;
    }

    /* Restore the original list structure by reversing the second half again */
    reverse_listint(&mid_reverse);

    return (1);
}

