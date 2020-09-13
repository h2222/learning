#include <iostream>

using namespace std;


void multiply_with_copy(int a, int b, int result)
{
	result = a * b;
	cout << "in func, the reuslt is " << result << endl;
}

void multiply_with_ref(int &a, int &b, int &result)
{
	result = a * b;
	cout << "in func, the reuslt is " << result << endl;
}

int main()
{
	int a = 5;
	int b = 6;
	int result = 0;

	cout << "test function with copied variable value to params" << " ";
	cout << "which mean the func only copy variable values to params" << " ";
	cout << "and do nothing for origin values" << " ";
	multiply_with_copy(a, b, result);
	cout << "the origin result is " << result << endl;
	cout << endl;


	// '&' means reference the memory address of variable, which mean 
	// you can referring the variable memory address to process the value of variable, and completely change that.
	cout << "test referecnce func with "<< endl;;
	multiply_with_ref(a, b, result);
	cout << "the orgin result is " << result << endl;
}
