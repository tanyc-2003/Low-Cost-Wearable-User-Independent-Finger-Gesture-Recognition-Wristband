function z=zerocross(v)

  z=find(diff(v>0)~=0)+1;
  
