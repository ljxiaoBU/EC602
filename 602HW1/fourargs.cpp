// Copyright 2017 Lijun Xiao ljxiao@bu.edu
#include <iostream>
int main(int argumentcount, char **arguments){
	int i;
	for(i=1;i<=4;i++)
	std::cout<<arguments[i]<<std::endl;
    if(argumentcount>4){
    	for(i;i<=argumentcount;i++)
    		std::cerr<<arguments[i]<<std::endl;

    }

	
	
	return 0;
		
	
 }
 