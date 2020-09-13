#include <iostream>
#include <array>

using namespace std;
//using std::array; // array belong to std
//using std::cout;
//using std::endl;

int main()
{
	// create array with 3 elements
	array<int, 3> a_0;
	// initialize a_0;
	a_0[0] = 10;
	a_0[1] = 20;
	a_0[2] = 30;
	// or we can initialize elements at once
	a_0 = {10, 20, 30};
	
	// create + initialize array (this called uniform intialization)
	array<int, 3> a_1 {30, 40, 50};

	// c-style array create and initialize
	int c_arr[3] = {1, 2, 3};


	// what happen if we dont initialize everything?
	// the remainder gets zero-initialized (eg. a_2[1] and a_2[0] are 0)
	array<int, 3> a_2 {10};
	cout << a_2[0] << a_2[1] << a_2[2] << endl;
	
	// basic method can be used in array
	cout << "a_2 size = " << a_2.size() << endl; // array size
	cout << "First element of a_2 = " << a_2.front() << endl;// first element
	cout << "Last element of a_2 = " << a_2.back() << endl;// last element
	
	a_2.fill(10);
	cout << "a_2 = " << a_2[0] << a_2[1] << a_2[2] << endl; // fill array with same element


	cout << " ";
	cout << " ";
	// array and pointer
	cout << "array and pointer" << endl;
	array<int, 10> arr_new;
	for (int i = 0; i < arr_new.size(); i++)
	{
		arr_new[i] = i * 10;
	}
	// as we can see, in array, the current value address + 1 == the next value address
	for (int i = 0; i < arr_new.size(); i++)
	{
		cout << "index:"<< i << " value:" << arr_new[i] << " address:" << &arr_new[i] << " address+1:"<< &arr_new[i]+1 << endl;
	}
	cout << endl;

	// pointer arithmetic 
	// in array, the address of value like a stack, overleap togther, so we can use +1 to refer each value of stack
	int arr_n[3] = {41, 32, 53}; // must be c-style array
	int* ptr = arr_n; // the array is set of value memory address, so we use pointer `ptr` to refer each address
	cout << "arr_new[0] = *ptr = " << *ptr << endl;
	ptr++;
	cout << "arr_new[1] = *(ptr++) = " << *ptr << endl;


	// these letters can be changed?
	char hw_array[] = {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!'};

	// this is read-only memory (letter are fixed!)
	const char* hw_string = "Hello, world!";

	cout << hw_array << endl;
	cout << hw_string << endl;


	return 0;
}
