function sin=m_sin_se(A)
%% sin��x)= x - x^3/3! + x^5/5! ʹ��̩�ռ�������sin����
x = (A/180)*pi;%������ĽǶ�ת��Ϊ����
 
%%
symbol=-1;
sum=-1;
my_eps=10^-15;
temp_sum=1;
power=-1;
while abs(temp_sum)>my_eps
    sum=sum+temp_sum;
    symbol=-symbol;
    power=power+2;
    temp_sum=symbol*x^power/factorial(power);
    
end
sin = sum;
end