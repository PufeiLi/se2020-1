#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592

double Factorial(int n)  //�׳�
{
	//long long ռ8���ֽ�
	double i, factorial = 1;

	for (i = 1; i <= n ; i++)
	{
		factorial *= i;
	}
	
	return factorial;
}

double cot_se(double x)
{
	if (x == 0 || fmod(x,180)== 0 || fmod(x,-180) == 0)  //�Ƕ������ֵ
	{
	return 9999;
	}
	else
	{
		double y = 0.0,z = 1.0;  //y = sinx;z = cos x
	int m1,m2;
	x = (fmod(x,360) * PI / 180);
	for(m1 = 1; m1 <= 20; m1++)    //sinx��̩�գ�m1���Ƽӵ��ڼ���
	{
		if (m1 % 2 == 0)
		{
			y -= pow(x, (2 * m1 - 1 )) / Factorial(2 * m1 - 1 );
		}
		else
		{
			y += pow(x, (2 * m1 - 1 )) / Factorial(2 * m1 - 1 );
		}
	}
	for(m2 = 1; m2 <= 20; m2++)       //cosx��̩�գ�m2���Ƽӵ��ڼ���
	{
		if (m2 % 2 == 0)
		{
			z += pow(x, (2 * m2 )) / Factorial(2 * m2 );
		}
		else
		{
			z -= pow(x, (2 * m2 )) / Factorial(2 * m2 );
		}
	}
	return  z/y;
	}
}

int main()
{
	//��ò�����ת��Ϊint
	double x;
	printf("��������Ҫ����ĽǶ�ֵ��\n");
	scanf("%lf", &x);
	printf("%.3lf\n", cot_se(x));
	system("PAUSE");
	return 0;
}