#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: A pointer to a pointer to the head of the linked list.
 */
void reverse_list(listint_t **head)
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
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @list1: A pointer to the head of the first linked list.
 * @list2: A pointer to the head of the second linked list.
 * Return: 1 if the lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int result;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* Empty list or list with one element is a palindrome */

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next; /* Odd number of nodes, skip the middle node */

	prev_slow->next = NULL; /* Break the first half from the second half */
	reverse_list(&slow);
	result = compare_lists(*head, slow);
	reverse_list(&slow);
	prev_slow->next = slow; /* Reconnect the first half and the second half */

	return (result);
}

