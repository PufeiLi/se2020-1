function e=Test_sin_se()
a=round(rand(1,1000)*360);%����1000��0-360֮�����
%b=sind(a);%�ԽǶ��Ƽ���sin������sind��MATLAB���к���
t1=0;
T=length(a);
for i=1:T %�Ƚϣ��������ĸ���
    b(i)=sind(a(i));
    c(i) = sin_se( a(i) );
    if b(i)~=c(i)
        t1=t1+1;
    end
end
   erro=t1/T;    
   e=erro;
end