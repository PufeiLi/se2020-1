function [avgError,flag]=Test_cos_se()
a=round(rand(1,1000)*360);%随机产生一个1*1000(double)数列，其中的值范围：0-360
%b=cosd(a);%以角度制计算cos函数，cosd是MATLAB固有函数
T=length(a);
%------------------------------------------------
%进行1000次的计算误差分析

  %将标准库中的cosd()与编写的cos_se()运算值进行误差计算：
     %对每一次误差计算的操作：
          %(1)两者误差值大于设定标准误差，即cos_se()计算错误，flag++
          %(2)两者误差值大于设定标准误差，即cos_se()计算无误
     %如上的操作重复1000（T）次，最终误差计算=测试计算中发生错误的次数/总测试数
for i=1:T %比较，计算错误的个数
    b(i)=cosd(a(i));%标准值
    c(i) = cos_se( a(i) );%测试值
    erro(i)=abs(b(i)-c(i));%计算每次误差=|标准值-测试值|
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
