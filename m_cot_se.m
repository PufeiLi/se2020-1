function [t]=m_cot_se(s) 
if mod(s,180)==0
    sin=0;
   t=cos_se(s)/sin;
else
    t=cos_se(s)/m_sin_se(s);
end
