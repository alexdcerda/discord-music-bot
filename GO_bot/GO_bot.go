

package main




type run_bot struct {
	Name string
	Age  int
}


func NewUser(name string, age int) run_bot {
	return run_bot{Name: name, Age: age}
}

