package main

import "fmt"

// 声明变量
// 推荐驼峰式声明, nameZhang,   no name_zhang
var name string
var age int
var isTrue bool

// 批量声明
var (
	address string
	number  int
)

// 声明变量时同时赋值
var s1 int = 1

func test() (int, int) {
	return 10, 20
}

func main() {
	// 在go语言中, 变量声明必须使用
	name = "Hao"
	age = 18
	isTrue = true
	address = "133"
	number = 2323
	fmt.Println(name, age, isTrue, address, number)

	// 简短变量声明(只能在函数中使用)
	s2 := 2
	fmt.Println(s1, s2)

	// 省略符(_, 又叫匿名变量 )
	a, _ := test()
	fmt.Println(a)

}
