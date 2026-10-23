package main

import (
	"fmt"
	"log"
)

func main() {
	var n int
	var val int
	var sum int
	var avg float64
	var max int
	var min int
	evenCount := 0
	oddCount := 0

	if _, err := fmt.Scan(&n); err != nil {
		log.Fatalf("Error: failed to read N - %v", err)
	}

	if n < 1 {
		log.Fatalf("Error: invalid input, N must be >= 1")
	}

	for i := 0; i < n; i += 1 {
		if _, err := fmt.Scan(&val); err != nil {
			log.Fatalf("Error: failed to read value - %v", err)
		}

		sum += val

		if i == 0 {
			max = val
			min = val
		} else {
			if val > max {
				max = val
			}
			if val < min {
				min = val
			}
		}

		if val != 0 && val%2 == 0 {
			evenCount += 1
		}
		if val != 0 && val%2 == 1 {
			oddCount += 1
		}
	}

	avg = float64(sum) / float64(n)

	fmt.Println("===========")
	fmt.Println("Sum       :", sum)
	fmt.Println("Avg       :", avg)
	fmt.Println("Max       :", max)
	fmt.Println("Min       :", min)
	fmt.Println("Even count:", evenCount)
	fmt.Println("Odd count :", oddCount)
}
