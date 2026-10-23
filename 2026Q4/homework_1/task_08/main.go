package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}

	ub := int(math.Sqrt(float64(n))) + 1

	for i := 2; i < ub; i += 1 {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	var n int

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error: failed to read N -", err)
		return
	}

	fmt.Println(n, "is prime -", isPrime(n))
}
