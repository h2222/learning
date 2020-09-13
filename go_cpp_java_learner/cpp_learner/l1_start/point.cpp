#include <iostream>

using namespace std;


/*
 * in this courese, we will introduce pointer * , memory address &*/

int main()
{
	int a;  // variable a
	int* b; // pointer, it can refer(point to) the momory address
	b = &a; // &a , get variable a memory address
	
	// set a to a new value 10
	a = 10;

	// print values and address
	// the pointer b's value is a memory address, which is same to a memory address
	// and b also has own memory address
	cout << "a : value = " << a << ", address = " << &a << endl;
	cout << "b : value = " << b << ", address = " << &b << endl; //pointer also is a variable, it has his own memory address
	cout << "the value of variable refered by pointer b, *b = a = " << *b << endl; // the operation is called de-reference, which means get value from the pointer that has refer a variable
	
	
	// what if we do no set variable to pointer, and print what is pointer dereferring value
	// null point
	int* c;
	cout << "*c = " << c << endl;
	
	// memory address transfer
	// x address --> pointer y(as value) --> pointer z (as value) --> dereference z value(x address) and change it value(change x value)
	cout << "test pointer" << endl;
	int x = 10;
	int* y = &x;
	int* z = y;
	*z = 0;
	cout << "x value = "<< x << endl;

	return 0;
}
