package main

import (
	"fmt"
	"io"
	"log"
)

func main() {
	p := 0
	n := 0
	z := 0

	for {
		var val int

		_, err := fmt.Scan(&val)

		if err != nil {
			if err == io.EOF {
				break
			}

			log.Fatalf("Error: failed to read X - %v", err)
			return
		}

		if val > 0 {
			p += 1
		} else if val < 0 {
			n += 1
		} else {
			z += 1
		}
	}

	fmt.Println("Postive  count:", p)
	fmt.Println("Negative count:", n)
	fmt.Println("Zeroes   count:", z)
}
