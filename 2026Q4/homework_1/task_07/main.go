package main

import (
	"fmt"
	"log"
)

func main() {
	var n int
	var sum int

	if _, err := fmt.Scan(&n); err != nil {
		log.Fatalf("Error: failed to read N - %v", err)
	}

	if n < 1 {
		log.Fatalf("Error: invalid input, N must be >= 1")
	}

	for i := 1; i <= n; i += 1 {
		if i%2 == 0 && i%3 == 0 {
			sum += i
		}
	}

	fmt.Println("Sum:", sum)
}
