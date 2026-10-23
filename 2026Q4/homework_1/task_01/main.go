package main

import "fmt"

func main() {
	var lhs int
	var rhs int
	var op string
	var res int

	if _, err := fmt.Scan(&lhs); err != nil {
		fmt.Println("Error: failed to read left number -", err)
		return
	}
	if _, err := fmt.Scan(&rhs); err != nil {
		fmt.Println("Error: failed to read right number -", err)
		return
	}
	if _, err := fmt.Scan(&op); err != nil {
		fmt.Println("Error: failed to read operation -", err)
		return
	}

	switch op {
	case "+":
		res = lhs + rhs
	case "-":
		res = lhs - rhs
	case "*":
		res = lhs * rhs
	case "/":
		if rhs == 0 {
			fmt.Println("Error: devision by zero")
			return
		}
		res = lhs / rhs
	default:
		fmt.Println("Error: unsupported operation '", op, "'")
		return
	}

	fmt.Println("Result:", lhs, op, rhs, "=", res)
}
