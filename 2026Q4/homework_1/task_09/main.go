package main

import (
	"fmt"
	"log"
)

type account struct {
	balance int
}

func new(amount int) *account {
	return &account{
		balance: amount,
	}
}

func (a *account) print() {
	fmt.Println("Текущий баланс: ", a.balance)
}

func (a *account) topUp(amount int) {
	a.balance += amount
	fmt.Println("Внесено:", amount)
}

func (a *account) withdraw(amount int) {
	if a.balance < amount {
		fmt.Println("Ошибка: Недостаточно средств")
	} else {
		a.balance -= amount
		fmt.Println("Списано:", amount)
	}
}

func readAmount() int {
	var amount int
	if _, err := fmt.Scan(&amount); err != nil {
		log.Fatalf("Error: failed to read amount - %v", err)
	}
	return amount
}

func main() {
	fmt.Println("Введите текущий баланс:")
	b := readAmount()

	acc := new(b)

	for {
		fmt.Println("=====================")
		fmt.Println("Выберите действие:")
		fmt.Println("1. Посмотреть баланс")
		fmt.Println("2. Пополнить баланс")
		fmt.Println("3. Снять средства")

		var op int
		if _, err := fmt.Scan(&op); err != nil {
			fmt.Printf("Ошибка: Неверная операция")
			continue
		}

		switch op {
		case 1:
			acc.print()
		case 2:
			amount := readAmount()
			acc.topUp(amount)
		case 3:
			amount := readAmount()
			acc.withdraw(amount)
		default:
			fmt.Println("Ошибка: Неверная операция")
		}
	}
}
