package main

import "fmt"

func printTable(n int) {
	for i := 1; i <= 10; i += 1 {
		fmt.Println(i, "x", n, "=", i*n)
	}
}

func main() {
	var n int

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error: failed to read N -", err)
		return
	}

	printTable(n)
}
