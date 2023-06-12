#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the start of the list
 * Return: pointer to reversed list
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
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if the list is not a palindrome
 *         1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	while (second_half != NULL && is_palindrome)
	{
		if ((*head)->n != second_half->n)
			is_palindrome = 0;
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_list(prev_slow->next);
	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (is_palindrome);
}
