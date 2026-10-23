package main

import "fmt"

func main() {
	var n int

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error: failed to read N -", err)
		return
	}

	if n > 0 {
		fmt.Println(n, "is positive")
	} else if n < 0 {
		fmt.Println(n, "is negative")
	} else if n == 0 {
		fmt.Println(n, "is zero")
	}

	if n%2 == 0 {
		fmt.Println(n, "is even")
	} else {
		fmt.Println(n, "is odd")
	}

	if n%3 == 0 {
		fmt.Println(n, "is devisible by 3")
	}

	if n%5 == 0 {
		fmt.Println(n, "is devisible by 5")
	}
}
