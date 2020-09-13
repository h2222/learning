#include <iostream>
#define X "this is what we call X"
using std::cout;
using std::endl;

int main()
{
    // g++ -save-temps compilation.cpp -o comp    that code will show all steps of compilation processing.
    // ldd compilation.cpp                         that code will show all library referenced by this file.
    // 
    cout << X << "Hello World\n" << endl;
    return 0;
}