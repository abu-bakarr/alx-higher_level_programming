#include "lists.h"
/**
 * lenls? (- len list)?
 *
 * @h: input head
 * Return: l
 */
int lenls(listint_t **h)
{
	int ln = 0;
	listint_t *t = *h;

	while (t)
	{
		ln++;
		t = t->next;
	}
	return (ln);
}
/**
 * is_palindrome? (- palind)?
 *
 * @h: input head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **h)
{
	listint_t *t = *h;
	int l = 0, i = 0, r = 0, s = 0, x1 = 0, x2 = 0;

	if (!t || !t->next)
		return (1);
	l = lenls(h);
	x1 = t->n;
	while (t)
	{
		if (i < l / 2)
		s += t->n;
		else
		{
			if (l % 2 != 0 && i == l / 2)
				s += 0;
			else
				s -= t->n;
		}
		x2 = t->n;
		t = t->next;
		i++;
	}

	if (s == 0 && x1 == x2)
		r = 1;
	return (r);
}
