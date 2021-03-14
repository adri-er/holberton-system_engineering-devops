#ifndef HOLBERTON_H
#define HOLBERTON_H

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <unistd.h>
#include <stdarg.h>

int _printf(const char *format,...);

int steps(char *ptr_to_percent, va_list param_list, char *buffer);

char *(*select_func(char specifier))(char *, va_list, char *);

char *clean_format(char *ptr_to_percent, char *buffer_format, char specifier);

int _write(char *buffer);

int str_length(char *);

char *_strncat(char *, char *, int n);

char *copy_string(char *ptr_to_percent, va_list param_list, char *buffer);

char *copy_int(char *ptr_to_percent, va_list param_list, char *buffer);

/**
 * cp_func - 
 *
 * @esp: 
 * @ptr_func: 
 */
struct cp_func
{
	char esp;
	char *(*ptr_func)(char *ptr_to_percent, va_list param_list, char *buffer);
};

typedef struct cp_func copy_func;


#endif /* HOLBERTON_H */
