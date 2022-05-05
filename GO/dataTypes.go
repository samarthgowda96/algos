package main

import "fmt"

//using var
var name = "sammy"
var age = 26
var newAge int64 = 1000

// Using const

const bike string = "Kawasaki"

//bike = "zx10r" // cant reassign if its defined as a constant

func main() {
	// string
	// bool
	// int
	// int int8 int16 int32 int64
	// unit uint8 uint16 uint32 uint64 uint64 uinptr
	// byte - alias for uint8
	// rune - alias for int32
	//float32 float64
	// complex64 complex128
	// Shorthand assignment // Cant declare these kind out of main function
	newName := "Gowda"
	const height float32 = 5.6 // has to define if its float64, by default it is float32

	// one liner declaration

	wife, children := "Stay single boy", "LOL"
	fmt.Println(name, age, newAge, bike, newName, height, wife, children)
	fmt.Printf("%T\n", age) // to get the type of he variable
	fmt.Printf("%T\n", newAge)
	fmt.Printf("%T\n", height)
}
