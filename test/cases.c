#include "../holberton.h"

void print_all(const char * const format, ...);



void test_string(void)
{
	int a= _printf("i=%sh\n","Hola Mundo");
    int b= printf("o=%sh\n","Hola Mundo");
    printf("a=%d\tb=%d\n", a,b);

    a= _printf("i=%sh%s\n","Hola Mundo"," 100");
    b= printf("o=%sh%s\n","Hola Mundo"," 100");
    printf("a=%d\tb=%d\n", a,b);

    a= _printf("i=%sh%s %s\n","Hola Mundo"," 100", "10 \ns");
    b= printf("o=% sh%s %s\n","Hola Mundo"," 100", "10 \ns");
    printf("a=%d\tb=%d\n", a,b);
}

void test_char(void)
{
	_printf("Character:[%c]\n", 'H');
    printf("Character:[%c]\n", 'H');
}
void test_int(void)
{
	int len = _printf("Percent:[%%]\n");
    int len2 = printf("Percent:[%%]\n");
	_printf("Length:[%d, %i]\n", len, len);
    printf("Length:[%d, %i]\n", len2, len2);
	_printf("Negative:[%d]\n", -762534);
    printf("Negative:[%d]\n", -762534);
	_printf("Len:[%d]\n", len);
    printf("Len:[%d]\n", len2);
}

void test_address(void)
{
	void * addr = (void *)0x7ffe637541f0;
	_printf("Address:[%p]\n", addr);
    printf("Address:[%p]\n", addr);
}
void test_ui(){
	unsigned int ui = (unsigned int)INT_MAX + 1024;
	_printf("Unsigned:[%u]\n", ui);
    printf("Unsigned:[%u]\n", ui);
}
test_octal()
{
	unsigned int ui = (unsigned int)INT_MAX + 1024;
	_printf("Unsigned octal:[%o]\n", ui);
    printf("Unsigned octal:[%o]\n", ui);
}
test_hex()
{
	unsigned int ui = (unsigned int)INT_MAX + 1024;
     void *addr = (void *)0x7ffe637541f0;
	 _printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
    printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
}
