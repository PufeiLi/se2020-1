function sin=m_sin_se(A)
%% sin（x)= x - x^3/3! + x^5/5! 使用泰勒级数计算sin函数
x = (A/180)*pi;%把输入的角度转换为弧度
 
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