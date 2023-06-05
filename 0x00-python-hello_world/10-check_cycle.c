#include "lists.h"

/**
 * check_cycle - checks if list contains cycle
 * @list: the list
 * Return: 0 if no cycle
 *         1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1); /* cycle found */

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0); /* no cycle found */
}
