#include <iostream>
using namespace std;

// print input value (int. float, double) 
int print_value(int v1)
{
    return v1;
}
float print_value(float v2)
{
    return v2;
}
double print_value(double v3)
{
    return v3;
}

// or we can use template to solve all type problems in one function
template <typename T>
T print_value_in_one(T v)
{
	cout << "value: " << v << endl;
	return v + 1;
}



int main()
{
    int v1 = 3;
    float v2 = 2.5;
    double v3 = 3.333333;
    // test overloading func
	cout << "test overloading" << endl;
    v1 = print_value(v1);
    v2 = print_value(v2);
    v3 = print_value(v3);
    cout << v1 << " " << v2 << " " << v3 << endl;
    
 	// 3 in 1 functiion
	cout << "test template" << endl;
    auto r1 = print_value_in_one<double>(v3);
	// and it also can set type of func
	auto r2 = print_value_in_one<int>(v1);
	cout << "get results: " << r1 << "\t" << r2 << endl;
    return 0;
}
