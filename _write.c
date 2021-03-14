#include "holberton.h"

/**
 * _write - writes the character c to stdout
 * @string: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int _write(char *buffer)
{
	int bytes_printed = write(1, buffer, _strlen(buffer));
	free (buffer);
	buffer = "";
	return (bytes_printed);
}
