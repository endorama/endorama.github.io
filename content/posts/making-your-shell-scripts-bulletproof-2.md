---
title: "Making your shell scripts bulletproof pt.2"
date: 2022-11-28T21:31:39+01:00
draft: false
type: post
tags: [shell, bash, robustness]
---

I posted some suggestion to improve robustness of shell scripts in {{< ref "making-your-shell-scripts-bulletproof.md" >}}, but there are a few more that I usually use that I think may be useful, so here is part 2 of it.

## Don't split words on space

>  The Internal Field Separator that is used for word splitting after expansion and to split lines into words with the read builtin command. The default value is `<space><tab><newline>`.

From [BASH manual][3], under `SHELL BUILTIN COMMANDS > Shell Variables`.

The default value of this variable means BASH split lines on spaces too. Most of the time this is a very confusing behaviour, as we are not used to consider a space a sentence terminator or split point (compared to newline or tab character).

To change this to only newlines and tabs use:
```bash
IFS=$'\n\t'
```

99% of the time I never ever noticed the difference in my shell scripts, and if you really need splitting on space you can always prefix your command with `IFS=$' '`.

You may also want to save the original IFS value and you can do so by:
```bash
ORIGINAL_IFS=$IFS
IFS=$'\n\t'
```

This way you can still use the old IFS value by prefixing commands with `IFS=$ORIGINAL_IFS`.

## Use traps

....

## Use shellcheck

I don't think I came across something more beneficial to my shell script writing than Shellcheck. [Shellcheck][2] is a static analysis tool for shell scripts (BASH is supported too).

The reason why you must run this is that will help you avoid all those errors you may be unconsciously making right now.

## Stop formatting your code

...manually!. Use [`shfmt`][4] to do it automatically! `shfmt` is part of a Golang-based shell parser and interpreter, a really cool project.

## Test BASH scripts with `bats`

Unit testing, in BASH. **HELL YEAH**! [`bats`][1] is a small framework to do unit testing in BASH (you can actually use it for any command that BASH can run, but let's stay focused here).

Happy coding 😉

[1]: https://github.com/bats-core/bats-core/
[2]: https://github.com/koalaman/shellcheck
[3]: https://man7.org/linux/man-pages/man1/bash.1.html
[4]: https://github.com/mvdan/sh#shfmt