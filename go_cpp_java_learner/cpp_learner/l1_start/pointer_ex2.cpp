#include<iostream>

using namespace std;


int main()
{
	// char* s can not be changed,  char s[] can be changed
	

	// const char* ptr
	int i;
	char hwc[] = "hello world";
	string hw = "hello world string";
	char* hwp1 = hwc; // the pointer that point to hw char array
	const char* hwp2 = "hello world char*" ;

	cout << hwc << endl;
	cout << hw << endl;
	cout << hwp1 << endl;
	cout << hwp2 << endl;

	//char* ptr 指向字符的变量指针
	hwc[0] = '0';// 修改原字符数组会影响指针
	for (int i = 0; i < 5; i++)
	{
		cout << hwp1[i] << " "; // print pointer reference 
		hwp1[i] = 'x'; // 可以修改
		cout << hwp1[i] << " "; // print pointer reference 
	}
	cout << endl;
	
	// const char* ptr 指向字符的常量指针
	char hwc2[] = "hi, world";
	hwc[0] = 'O';  // 只能通过修改原字符串数组来, 来改变指针
	const char* hwp3 = hwc;
	for (int i = 0; i < 5; i++)
	{
		cout << hwp3[i] << " "; // 指针指向的地址并不能修改
	}
	cout << endl;


	// const char* ptr 可以改变指针的指向, 但不能直接改变指针指向的值
	hwp3 = hwc2;
	for (int i = 0; i < 9; i++)
	{
		cout << hwp3[i] << " ";
	}
	cout << endl;


	// char* const ptr 指向字符的常量指针
	// 不能修改指针的指向, 但可以修改指针指向的内容
	char* const hwp4 = hwc;
	hwp4[0] = 'S'; // 通过指针指向的地址修改内容, 原被指针指向的变量也会被改变;
	for (int i = 0; i < 5; i++)
	{
		cout << hwp4[i] << " ";
	}
	cout << endl;
	cout << "hwc first element is " << hwc[0] << endl;


	// 通过修改原变量char[] 改变指针指向的内容
	hwc[0] = 'E';
	for (int i = 0; i < 5; i++)
	{
		cout << hwp4[i] << " ";
	}
	cout << endl;

	return 0;
}
