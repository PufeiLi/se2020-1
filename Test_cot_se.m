function [avgError,flag]=Test_cot_se()
a=round(rand(1,1000)*360);%随机产生一个1*1000(double)数列，其中的值范围：0-360
%b=tand(a);%以角度制计算tan函数，tand是MATLAB固有函数
%t=0;
T=length(a);
%------------------------------------------------
%进行1000次的计算误差分析

  %将标准库中的1/tand()与编写的cot_se()运算值进行误差计算：
     %对每一次误差计算的操作：
          %(1)两者误差值大于设定标准误差，即cot_se()计算错误，flag++
          %(2)两者误差值大于设定标准误差，即cot_se()计算无误
     %如上的操作重复1000（T）次，最终误差计算=测试计算中发生错误的次数/总测试数

for i=1:T %比较，计算错误的个数
    b(i)=1/tand(a(i));%标准值
    c(i) = cot_se( a(i) );%测试值
    if abs(b(i))==Inf&&abs(c(i))==Inf %考虑a(i)=90的情况
         erro(i)=0;
     else
      erro(i)=abs(b(i)-c(i));%计算每次误差=|标准值-测试值|
     end
    erro(i)=abs(b(i)-c(i));
end
for j=1:T
if erro(j)>0.001
      flag=1;
      break;
  else
      flag=0;
end
end
 avgError=sum(erro)/T;
end
