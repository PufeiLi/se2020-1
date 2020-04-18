function e=Test_cot_se()
a=round(rand(1,1000)*360);%产生1000个0-360之间的数
%b=tand(a);%以角度制计算tan函数，tand是MATLAB固有函数
t=0;
T=length(a);
for i=1:T %比较，计算错误的个数
    b(i)=1/tand(a(i));
    c(i) = cot_se( a(i) );
    if b(i)~=c(i)
        t=t+1;
    end
end
  erro=t/T;    
  e=erro;
end