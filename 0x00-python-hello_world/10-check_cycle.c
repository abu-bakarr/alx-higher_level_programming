#include "lists.h"
/**
 *check_cycle - function that checks
 *if a linked list has a cycle in int
 *@list: linked list
 *Return: 0 
*/
int check_cycle(listint_t *list)
{
    listint_t *current;
    listint_t *check;

    current = list;
    check = list;

    while (check != NULL && check->next != NULL)
    {
        current=current->next;
        check=check->next->next;

        if (current == check)
            {
                return (1);
            }
    }

    return (0);
}
