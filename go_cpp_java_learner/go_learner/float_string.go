package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	f1 := float32(32.2) // 强制指定类型
	f2 := 543.1

	fmt.Println(f1, f2)
	fmt.Println(math.MaxFloat32)

	// 多行字符串
	s1 := `
		发送到发送到该死的感受到
		方式发送的发送到发送到
		发送到发送到发送到发送到高
	`
	fmt.Println(s1)

	// 求string 长度
	l := len(s1)
	fmt.Println(l)

	// 字符串拼接
	s2 := "d,a,s,d,a,s,d,a,s,d,a,s,d"
	fmt.Println(s1 + s2)

	//字符串分割
	s2s := strings.Split(s2, ",")
	fmt.Println(s2s)

	//list拼接, join
	s2j := strings.Join(s2s, "+")
	fmt.Println(s2j)

	// 判断字符串包含
	s2c := strings.Contains(s2, "发")
	fmt.Println(s2c)

	// 判断前缀和后缀
	s2f := strings.HasPrefix(s2, "good")
	s2b := strings.HasSuffix(s2, "good")

	fmt.Println(s2f, s2b)

	// 返回字符index
	idx := strings.Index(s2, "a")
	fmt.Println(idx)

}
