package main

import "fmt"

func main() {
	var n int
	var sum int
	var avg float64

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error: failed to read N -", err)
		return
	}

	if n < 1 {
		fmt.Println("Error: invalid input, N must be >= 1")
		return
	}

	for i := 1; i <= n; i += 1 {
		sum += i
	}

	avg = float64(sum) / float64(n)

	fmt.Println("Sum:", sum)
	fmt.Println("Avg:", avg)
}
