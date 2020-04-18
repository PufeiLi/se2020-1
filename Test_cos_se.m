function [avgError,flag]=Test_cos_se()
a=round(rand(1,1000)*360);%产生1000个0-360之间的数
%b=cosd(a);%以角度制计算cos函数，cosd是MATLAB固有函数
T=length(a);
for i=1:T %比较，计算错误的个数
    b(i)=cosd(a(i));
    c(i) = cos_se( a(i) );
    erro(i)=abs(b(i)-c(i));%每次误差
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
