function [t]=m_tan_se(s)

if mod(s,180)==90
    cos=0;
   t=m_sin_se(s)/cos;
else
    t=m_sin_se(s)/cos_se(s);
end
