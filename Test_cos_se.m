clc,clear
a=round(rand(1,1000)*360);%����1000��0-360֮�����
%b=cosd(a);%�ԽǶ��Ƽ���cos������cosd��MATLAB���к���
t=0;
T=length(a);
for i=1:T %�Ƚϣ��������ĸ���
    b(i)=cosd(a(i));
    c(i) = cos_se( a(i) );
    if b(i)~=c(i)
        t=t+1
    end
end
  erro=t/T;      