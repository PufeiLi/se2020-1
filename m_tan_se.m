function [t]=m_tan_se(s)

if mod(s,180)==90
    cos=0;
   t=sin_se(s)/cos;
else
    t=sin_se(s)/cos_se(s);
end