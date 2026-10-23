package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	var x float64
	max := math.Inf(-1)
	min := math.Inf(1)

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error: failed to read N -", err)
		return
	}

	if n < 1 {
		fmt.Println("Error: invalid input, N must be >= 1")
		return
	}

	for i := 0; i < n; i += 1 {
		if _, err := fmt.Scan(&x); err != nil {
			fmt.Println("Error: failed to read X -", err)
			return
		}

		max = math.Max(x, max)
		min = math.Min(x, min)
	}

	fmt.Println("Max:", max)
	fmt.Println("Min:", min)
}
