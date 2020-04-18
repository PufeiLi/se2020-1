function e=Test_sin_se()
a=round(rand(1,1000)*360);%产生1000个0-360之间的数
%b=sind(a);%以角度制计算sin函数，sind是MATLAB固有函数
t1=0;
T=length(a);
for i=1:T %比较，计算错误的个数
    b(i)=sind(a(i));
    c(i) = sin_se( a(i) );
    if b(i)~=c(i)
        t1=t1+1;
    end
end
   erro=t1/T;    
   e=erro;
end