#include <iostream>
#include <vector>

using namespace std;


int main()
{
	// vector do not limit the size of container, and it also can shrink it capacity
	// to decrease container size.
	vector<int> v1;
	cout << "vector size: " << v1.size() << endl;

	// push_back: insert a element and push others back
	// emplace_back: insert a element at end of vector
	cout << "after insert elements" << endl;
	v1.push_back(1);
	v1.emplace_back(2);
	
	// size means how many element in this vector
	// capacity means how big the vector is
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl;

	// the capacity of vector will increase exponentially
	// e.g. (2, 4, 8, 16, 32, ...)
	cout << "obverse the capacity change" << endl;
	v1.push_back(3);
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl;

	// reserve: reserve the element in vector, if you reserve number > 
	// the element of vector, it also will open the size of reserve space
	// for vector capacity
	cout << "reserve space test" << endl;
	v1.reserve(100); // reverse 100 element but we dont have that much
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl;


	// shrink the vector capacity
	cout << "shrink" << endl;
	v1.shrink_to_fit();
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl;


	// we can also resize the container, which can change both the size and
	// capacity
	cout << "resize" << endl;
	v1.resize(10, 6); // resize(size, the element of filling increase size);
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl;

	// iterator the vector
	cout << "print vector" << endl;
	for (auto i : v1)
	{
		cout << i << " ";
	}
	cout << endl;


	// rid of a particular element using erase and iterators
	// rid beigin elememt of v1
	// erase fun can be used in String erase(frist, end) and iterator(first, end)
	cout << "test erase" << endl;
	v1.erase(begin(v1));
	cout << "vector size: " << v1.size() << endl;
	cout << "vector capacity: " << v1.capacity() << endl; // the rid do not change capacity
	for (auto i : v1)
	{
		cout << i << " ";
	}
	cout << endl;

	// get value by using index
	cout << "get value" << endl;
	cout << "v1[0]=" << v1[0] << " ";
	cout << "v1.at(0)=" << v1.at(0) << " ";
	cout << endl;


	return 0;
}
