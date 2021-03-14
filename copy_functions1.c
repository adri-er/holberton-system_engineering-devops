#include "holberton.h"


/**
 * copy_string -
 *
 * @ptr_to_percent: pointer to string.
 * @param_list: list of arguments
 *
 * Return: pointer to secondary buffer
 */
char *copy_string(char *ptr_to_percent, va_list param_list,char *buffer)
{
	sbuffer = malloc(1024);
	char *format_ptr;

	if (sbuffer == NULL)
	{
		free (buffer);
		exit ();
	}

	format_buffer = malloc(250);
	if (format_buffer == NULL)
	{
		free (sbuffer);
		free (buffer);
		exit ();
	}

	format_ptr = clean_format(ptr_to_percent, format_buffer, 's');
	if (format_ptr == NULL)
	{
		free (sbuffer);
		free (format_buffer);
		return (NULL);
	}

	_strncat(sbuffer, va_arg(param_list, char *), 1024);

	/* aply format */

	free (format_buffer);
	return (sbuffer);
}
