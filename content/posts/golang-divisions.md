---
title: "Golang divisions"
date: 2022-09-15T12:31:05+02:00
draft: false
type: post
tags: [golang, math, til]
---

At work today I read a piece of code in Golang that got me curious:

```go
maxQuerySize := 500
// metricDataQueries is user provided
sliceLength := len(metricDataQueries)/maxQuerySize + 1
// what's the value of sliceLength?
for i := 0; i < sliceLength; i++ { 
    whatever
}
```

This is a simple integer division, but the result is then used as a parameter to the for loop.
Integer division has a drawback, that can create a bug in this case: the remainder, as `float` in for loop declarations are supported only if no truncation happens when converting to `int` (i.e. `10.0` works, `10.1` don't).

How does Go handle this? The answer is as simple as it gets: remainder is ignore and the result is the quotient. The reason why this happens is explained in Go specs, under [Constant expressions](https://go.dev/ref/spec#Constant_expressions):
> Any other operation on untyped constants results in an untyped constant of the same kind; that is, a boolean, integer, floating-point, complex, or string constant. If the untyped operands of a binary operation (other than a shift) are of different kinds, the result is of the operand's kind that appears later in this list: integer, rune, floating-point, complex.

Which means that to have "true" division you need to convert _at least one argument_ to `float`:

```go
a := 10.0 / 2
b := 10 / 2.0
c := 10.0 / 2.0
d := 10 / 2
fmt.Println(reflect.TypeOf(a)) // float
fmt.Println(reflect.TypeOf(b)) // float
fmt.Println(reflect.TypeOf(c)) // float
fmt.Println(reflect.TypeOf(d)) // int
```
[go.dev/play](https://go.dev/play/p/UfjOH9rGIAi)

Doing integer division effectively "floors" the result of the operation. What if we want the ceil of it?

Go `math` package has [`Ceil(x float64) float64`](https://pkg.go.dev/math#Ceil) for this, which implies doing a "true" division and applying `Ceil` on the result.

All of this was not really surprising, but it's cool to see this being implemented in a very ergonomic way. 

Just a note: if you want to get a float value you must convert to `float` all division arguments **before** the division.

Do this: `float64(2) / float64(10) // 0.2` and **not** this: `a := float64(2 / 10) // 0`.