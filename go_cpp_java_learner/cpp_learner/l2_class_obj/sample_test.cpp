// this program implements a vector using a class

#include <iostream>

#include "interface.h" // your own inferface

using namespace std;


void print_no_class(vector1 v)
{
	cout << "start x:" << v.start_x << ", start_y:" << v.start_y << endl;
	cout << "end x:" << v.end_x << ", end y:" << v.end_y << endl;
}


int main()
{
	// create a vector
	vector1 v1;
	v1.start_x = 1.0;
	v1.start_y = 2.0;
	v1.end_x = 3.0;
	v1.end_x = 4.0;

	// call the method
	cout << "test class method" << endl;
	v1.print_value();
	
	// call the funcion
	cout << "test function" << endl;
	print_no_class(v1);

	// g++ -C interface.h
	// g++ -o test implement.cpp
	return 0;
}
