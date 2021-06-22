#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - loops infinite over a while.
 *
 * Return: None.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes.
 *
 * Returns: None
 */
void main(void)
{
	int i = 0;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
		}
	}
	for (i = 0; i < 5; i++)
		wait(NULL);
	infinite_while();
}
