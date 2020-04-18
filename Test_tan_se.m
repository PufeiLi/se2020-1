function [avgError,flag]=Test_cos_se()
a=round(rand(1,1000)*360);%产生1000个0-360之间的数
%b=tand(a);%以角度制计算tan函数，tand是MATLAB固有函数
t=0;
T=length(a);
for i=1:T %比较，计算错误的个数
    b(i)=tand(a(i));
    c(i) = tan_se( a(i) );
    if abs(b(i))==Inf&&abs(c(i))==Inf
        erro(i)=0;
    else
     erro(i)=abs(b(i)-c(i));%每次误差
    end
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
