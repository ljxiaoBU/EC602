// Copyright 2017 Lijun Xiao ljxiao@bu.edu

#include <ctime>
#include <iostream>
#include <math.h>



int main() {

	clock_t start_clock, end_clock;
	
	uint16_t i;


	start_clock=clock();
	for(i=1;i!=0;i++)
		{};
	end_clock=clock();
	double seconds=static_cast<double>(end_clock-start_clock)/CLOCKS_PER_SEC;

	double int16micro=seconds*pow(10,6);
	double int1=int16micro*pow(10,3)/pow(2,16); //nanoseconds per int1
	double int8nanoseconds=int1*pow(2,8);
	double int32sec=int1*pow(2,32)/pow(10,9);
	double int64year=int1*pow(2,64)/pow(10,9)/60/60/24/365;

	std::cout << "estimated int8 time (nanaoseconds): " << int8nanoseconds << std::endl;
	std::cout << "measured int16 time (microseconds): " << int16micro << std::endl;
	std::cout << "estimated int32 time (seconds): " << int32sec << std::endl;
	std::cout << "estimated int64 time (years): " << int64year << std::endl;




  

  
 


return 0;
}