---
title: "Golang string comparison benchmark"
date: 2022-11-10T22:48:03+01:00
draft: false
type: post
tags: [golang, benchmark, comparison]
---

I recently read [No Safe Efficient Ways to Do Three-way String Comparisons in Go - Go 101 Blog](https://go101.org/blog/2022-10-01-three-way-string-comparison.html) about performing string comparisons and some performances issue that the `strings.Compare` function has.

The main statement of the post is 
> Benchmark code constantly shows strings.Compare uses 2x CPU time of bytes.Compare when comparing unequal same-length byte sequences (we view both strings and byte slices as byte sequences here).

It got me curious so I jumped to the editor to check what was happening. I was not interested in debunking the claim, I was interested in understanding how different string comparison implementation performances differed.

In the linked post you can find the source code for `strings.Compare` and `bytes.Compare`.

My initial assumptions:
- `strings.Compare` is 2x slower than `bytes.Compare` as stated in the article
- built-ins are faster than `strings.Compare` as implied by Golang documentation, that states: "It is usually clearer and always faster to use the built-in string comparison operators ==, <, >, and so on."
- converting string to bytes and using `bytes.Compare` may be beneficial (especially for longer strings)

To test my assumptions I implemented 4 test cases (and corresponding `_long` versions): 
1. `BuiltIn` test; string comparison using built-in operators
2. `Strings` test; string comparison using `strings.Compare`
3. `Bytes` test; bytes comparison using `bytes.Compare` with string to bytes conversion just for the comparison
4. `BytesWithBytes` test; bytes comparison using `bytes.Compare` with byte sequences (as control)

You can find The Code™ in this repository: [endorama/go-strcmp-bench](https://github.com/endorama/go-strcmp-bench).

## The setup

* Golang 1.19.2
* Benchmark run with `go test -bench=. -v  --benchmem -count=20` and shown with `benchstat`
* 2 short strings (6 chars) and 2 long strings (255 chars) and their bytes conversion. There is an interesting worst case scenario in `strings.Compare`: its performances are at worst when comparing 2 unequal strings of equal length. For this reason the strings are **equal length** and **differ for the last char**.

## Benchmark results with short strings

```
name                    time/op
BuiltIn-12              15.3ns ± 3%
Bytes-12                42.3ns ± 3%
BytesWithBytes-12       9.23ns ± 2%
Strings-12              15.6ns ± 1%
```

* As expected `strings.Compare` is ~2x slower than `bytes.Compare`.
* Unexpectedly, using built-in is not that much faster?
* More unexpectedly, converting to bytes is massively less performing, ~3x less than comparing strings and ~4x less than comparing bytes.

## Benchmark results with long strings

```
name                    time/op
BuiltIn_long-12         32.1ns ± 5%
Bytes_long-12            366ns ± 6%
BytesWithBytes_long-12  20.7ns ± 3%
Strings_long-12         37.4ns ± 3%
```

* As expected, `strings.Compare` is still 2x slower than `bytes.Compare`. ✔
* Built-in is **slightly better**. 🤔
* Don't look at bytes conversion. 🙈

## Conclusions / TL;DR

```
name            time/op (short)  time/op (long)  diff to bytes  diff to strings
BuiltIn         15.3ns  ± 3%     32.1ns ± 5%     ~2x to 1.5x    1x
Bytes           42.3ns  ± 3%     366ns   ± 6%    ~4x to ~18x    ~3x to ~11x
BytesWithBytes  9.23ns ± 2%      20.7ns ± 3%     1x             ~0.6x
Strings         15.6ns  ± 1%     37.4ns ± 3%     ~1.5x to ~2x   ~1x
```

* built-in is not (that) faster 🤷
* use `strings.Compare` if you think is more readable and you have short strings or you're not performing a lot of comparisons
* **don't** convert a `string` to `bytes`, as it nukes performances 🪃 
    * is [possible to make this faster](https://twitter.com/go100and1/status/1583715982904029185) using unsafe pointers, but 🐉 here be dragons 🐉 

I haven't delve into a deep comparison for `built-ins` and `strings.Compare` for this time.