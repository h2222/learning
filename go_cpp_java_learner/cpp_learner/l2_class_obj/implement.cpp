// this program implements a vector using a class

#include <iostream>

#include "interface.h" // your own inferface

using namespace std;

// method associated with the vectors1 to print out the vector
void vector1::print_value()
{
	cout << "start x:" << start_x << ", start_y:" << start_y << endl;
	cout << "end x:" << end_x << ", end y:" << end_y << endl;
}

