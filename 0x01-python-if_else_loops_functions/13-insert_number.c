#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node in a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 * Return: NULL if function fails
 *         pointer to new node if successful
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;
	int num;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	temp = *head;
	num = number;
	if (temp == NULL || num <= temp->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp != NULL && temp->next != NULL && temp->next->n < num)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (new);
}
