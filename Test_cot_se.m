function e=Test_cot_se()
a=round(rand(1,1000)*360);%����1000��0-360֮�����
%b=tand(a);%�ԽǶ��Ƽ���tan������tand��MATLAB���к���
t=0;
T=length(a);
for i=1:T %�Ƚϣ��������ĸ���
    b(i)=1/tand(a(i));
    c(i) = cot_se( a(i) );
    if b(i)~=c(i)
        t=t+1;
    end
end
  erro=t/T;    
  e=erro;
end