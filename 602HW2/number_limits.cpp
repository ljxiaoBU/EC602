//Copyright 2017 Lijun Xiao ljxiao@bu.edu
#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>


int main(){


  double Rs,Ri,Rm;
  // calculate Rs, Ri, and Rm for half/binary16 vs int16_t

  Rs=1/pow(2,-14);
  Rm=65504/(pow(2,15)-1);
  Ri=(pow(2,15)-1)/pow(2,11);
  std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
  Rs=1/FLT_MIN;
  Rm=FLT_MAX/INT32_MAX;
  Ri=INT32_MAX/pow(2,24);
  std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for double/binary64 vs int64_t
  Rs=1/DBL_MIN;
  Rm=DBL_MAX/INT64_MAX;
  Ri=INT64_MAX/pow(2,53);
  std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;
  
  return 0;
}