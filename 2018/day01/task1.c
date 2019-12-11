#include <stdio.h>

int main()
{
	int totalSum = 0;
	char signChar;
	while ((signChar = getchar()) != EOF)
	{
		int sign = signChar == '+' ? 1 : -1;

		int localSum = 0;
		char c;
		while ((c = getchar()) != '\n')
		{
			localSum = localSum * 10 + c - '0';
		}

		totalSum += localSum * sign;
	}

	printf("%d\n", totalSum);
}
