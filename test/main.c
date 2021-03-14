#include "../holberton.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    /* s c d i u o xX p r */
    /*char txt[] = "hola\n";*/
    char whatTest[] = "s";
    int i = 0;

   while (whatTest[i])
    {
        switch(whatTest[i])
        {
            case 's':
                test_string();
                break;
            case 'c':
                test_char();
                break;
            case 'd':
                test_char();
                break;
            case 'p':
                test_hex();
                break;
        }
        i++;
    }
    /*   other test*/



    return (0);
}
