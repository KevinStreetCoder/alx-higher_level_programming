#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
return *head;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return 1;

listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev_slow = *head;
listint_t *mid = NULL;
listint_t *second_half = NULL;
int is_palindrome = 1;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL) // Odd number of nodes, move slow to the next node
{
mid = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;
reverse_listint(&second_half);

listint_t *p1 = *head;
listint_t *p2 = second_half;

while (p1 != NULL && p2 != NULL)
{
if (p1->n != p2->n)
{
is_palindrome = 0;
break;
}
p1 = p1->next;
p2 = p2->next;
}

reverse_listint(&second_half);

if (mid != NULL)
{
prev_slow->next = mid;
mid->next = second_half;
}
else
{
prev_slow->next = second_half;
}

return is_palindrome;
}
