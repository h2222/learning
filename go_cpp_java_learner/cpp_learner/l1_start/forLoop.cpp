#include <iostream>
#include <array>
#include <vector>
using namespace std;


int main()
{
	array<int, 5> arr {0, 1, 2, 3, 4};

	// Range-based for loop, have no warray about out of indexing
	// (we can not use range-based for loop in c-style array)
	cout << "Range-based for loop" << endl;
	for (auto i : arr) 
	{
		cout << i << " ";
	} 
	cout << endl;

	// iterator
	// iterator can be used to access STL containers.
	// we can iterate through them(container), and dereference them to acess their values
	// it meanless to get index of array if we use iterator, so we use begin() or xx.begin()and end() or xx.end()
	// to represent begin and end
	cout << "iterator for loop" << endl;
	for (auto it = begin(arr); it < end(arr); it++)
	{
		cout << it << " "; // it is memory address of elements
		cout << *it << " ";// *it is real values, * is derefernce symbol
	}
	cout << endl;
	
	// or we can control what we should stop iterator
	for (auto it = begin(arr); it < begin(arr) + 2; it++)
	{
		cout << it << " "; // it is memory address of elements
		cout << *it << " ";// *it is real values, * is derefernce symbol
	}
	cout << endl;

	// reverse iterator to print array backward
	// end() --> rbegin(),   begin() --> rend()
	cout << "Reverse-iterator" << endl;
	for (auto it = rbegin(arr); it < rend(arr); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
	

	// python-style for-each loop
	cout << "for-each style loop" << endl;
	for (int i : {1, 2, 3, 4, 5, 6})
	{
		cout << i << " ";
	}
	cout << endl;

	// for loop by using vector
	// Fill the vector to iterate over
	cout << "loop to initialize vector" << endl;
	vector<int> int_vector;// vector is container that you dont initialize size
	int temp;
	for (unsigned i = 0; i < 6; i++)
	{
		temp = rand() % 100; // get random int value
		cout << temp << " ";
		int_vector.push_back(temp); // put value into the backward of vector
	}
	cout << endl;
	
	// update vector value by +1
	// we can set std version by:
	// g++ -std=c++11 -o xxx forLoop.cpp
	cout << "update vector values" << endl;
	for (auto &i : int_vector)
	{
		cout << &i<< " ";
		cout << i+1<< " ";
	}
	cout << endl;


	// c-style loop
	// 0u means singedness integer, that is mean you dont care about +/-
	// or you can change i type to unsigned i = 0; is same
	cout << "c-style loop" << endl;
	for (auto i = 0u; i < arr.size(); i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}
