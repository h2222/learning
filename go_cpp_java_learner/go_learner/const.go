package main

import "fmt"

// 常量, constant  const, 不变量

const pi = 3.14
const l = "Good"

// 批量声明1常量
const (
	one = 1
	two = 2
)

// 批量声明时, 如果某一个常量没有赋值, 则认为跟上一行赋值的常量的值相同
const (
	three = 3
	threeCopy1
	threeCopy2
)

// iota, 常量计数器, 初始为0(只要const关键字出现, iota一定被置为0), 每增加一"行"个常量 iota 的值 +1
const (
	goi0 = iota
	goi1
	goi2
)

// 匿名常量也是常量, iota 也会计数
const (
	gon0 = iota
	gon1
	_
	gon2
)

// 新增一行, iota +1, 在同一行声明常量, iota 保持不变
const (
	gov0, gov1 = iota + 1, iota + 2 // gov0 = 0+1,  gov1=0+2
	gov3, gov4 = iota + 1, iota + 2 // gov3 = 1+1,  gov4=1+2
)

// 存储大小单位设置
const(
	_ = iota
	KB = 1 << (10*iota)  // (二进制) 1 左移 10*1 位, 1000000000 (二进制) --> 2^10(十进制) --> 1024 byte
	MB = 1 << (10*iota) // 1 右移 10*2 位
	GB = 1 << (10*iota) // 1 右移 10*3 位
	TB = 1 << (10*iota) // 1 右移 10*4 位
	PB = 1 << (10*iota) // 1 右移 10*5 位
)


func main() {
	fmt.Println(pi, l)
	fmt.Println(one, two)
	fmt.Println(three, threeCopy1, threeCopy2)
	fmt.Println(goi0, goi1, goi2)
	fmt.Println(gon0, gon1, gon2)
	fmt.Println(gov0, gov1, gov3, gov4)
	fmt.Println(KB, GB, MB, TB, PB)
}
