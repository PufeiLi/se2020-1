#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592

float tan_se(float);
float Factorial(int n)      //�׳�
{
	//long long ռ8���ֽ�
	float i, factorial = 1;

	for (i = 1; i <= n ; i++)
	{
		factorial *= i;
	}
	
	return factorial;
}

float tan_se(float x)
{
	if (x != 0 && (fmod(x,90)== 0 || fmod(x,-90) == 0))
	{
	return 9999;
	}
	else
	{
		float y = 0.0,z = 1.0;  //y = sinx;z = cos x
	int m1,m2;
	x = (fmod(x,360) * PI / 180);    
	for(m1 = 1; m1 <= 20; m1++)    //sinx ��̩�գ�m1���ƺ���ӵ��ڼ���
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
	for(m2 = 1; m2 <= 20; m2++)    //cosx ��̩�գ�m2���ƺ���ӵ��ڼ���
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
	return  y/z;
	}
}

