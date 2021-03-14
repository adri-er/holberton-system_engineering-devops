#include "holberton.h"

/**
 * steps -
 *
 * @ptr_to_percent:
 * @param_list:
 *
 * Return: number of format caracters.
 */
int steps(char *ptr_to_percent, va_list param_list, char *buffer)
{
	char sp_chars[] = "%s";
	int index_format, index_sp_chars;
	char *(*ptr_func)(char *ptr_to_percent, va_list param_list, char *buffer);
	char *sbuffer;

	for (index_format = 1; ptr_to_percent[index_format]; index_format++)
	{/*itera hasta encontrar un caracter especial o un caeacter nulo*/
		for (index_sp_chars = 0; sp_chars[index_sp_chars]; index_sp_chars++)
		{/*itera para cada caracter especial */
			if (ptr_to_percent[index_format] == sp_chars[index_sp_chars])
			{/*hubo una coincidencia con un caracter especial*/
				if (ptr_to_percent[index_format] == '%')
				{/*se debe imprimir un simbolo %*/
					return (0);
				}
				else
				{/*hubo una coincidencia con un especificador de formato*/
					ptr_func = select_func(ptr_to_percent[index_format]);
					sbuffer = ptr_func(ptr_to_percent, param_list, buffer);
					if (sbuffer == NULL)
					{/* formato no es valido*/
						return (0);
					}
					else
					{/* agregamos el texto formateado al buffer*/
						_strncat(buffer, sbuffer, 1024);
						free(sbuffer);
						return (index_format);
					}
				}
			}
		}
	}

	/*no se encontro caracter especial*/
	return (0);
}
