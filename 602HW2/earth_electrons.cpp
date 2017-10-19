//Copyright 2017 Lijun Xiao ljxiao@bu.edu
#include <iostream>
#include <cmath>

int main(){

	long double earthmass=5.972*pow(10,24)*1000;  // g
	long double atomspermole=6.022*pow(10,23);
	
	long double electronsperatom=14;
	long double gramspermole=28.08;

	long double electronsnumber=earthmass/gramspermole*atomspermole*electronsperatom;

	long double estimate=electronsnumber/pow(2,43);

	long double lower=estimate*0.9;

	long double upper=estimate*1.1;

	std::cout<<estimate<<std::endl;
	std::cout<<lower<<std::endl;
	std::cout<<upper<<std::endl;


	return 0;




}