function [t]=cot_se(s) %����cordic�㷨ʵ��
%��ʼ��
x = 1;
y = 0;
z = s * pi /180;%����ǶȦ�
a = 0;
d = 1;
k = 0.6073; %kΪ����
x = k*x;
while a<100 %�˴������ж�d�ĸ��ſ���ѭ��������ѭ����Ӧ��a�������ơ�
    if z>=0
        d = 1;
    else d = -1;
    end
%����
    xNew = x;
    x = xNew-(y*d*(1/2^a));
    y = y+(xNew*d*(1/2^a));
    z = z-(d*(atan(1/2^a)));
    a = a+1;
end
t = x/y;
end
