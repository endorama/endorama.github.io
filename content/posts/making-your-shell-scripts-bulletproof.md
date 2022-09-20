---
title: "Making your shell scripts bulletproof"
date: 2022-09-19T21:13:23+02:00
draft: true
type: post
tags: [shell, bash, robustness]
---

Writing shell scripts in BASH is something I started doing around 2008 probably, but it's only after some years I started doing it in a way that was preventing me from shooting myself in the foot.

BASH is great and powerful, allows to harness the power of UNIX tools, but its syntax it's unforgiving and not easy to master (and at times even after more than 10 years, confusing).

In this post I'll go through some of my mandatory patterns to add robustness to my shell scripts.

## TL;DR:

The full template for these suggestions would be:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

## Using the interpreter from the environment

Use `env` for the shebang:
```
#!/usr/bin/env bash
```

There are occasions where this may not be advisable (especially if you use the shebang for other languages), but for BASH _generally_ is better to use `/usr/bin/env` for the shebang. See [this StackOverflow answer][1] for a broader discussion.

Using `/usr/bin/env` tells the OS to search for the specified executable in the user `PATH` instead on a fixed location, this makes it more portable. `env` is usually available at `/usr/bin/env`, you can double check that with `command -v env`.

## Catch unset variables

> Treat unset variables and parameters other than the special parameters "@" and "*" as an error when performing parameter expansion.

From [BASH manual][3], under `SHELL BUILTIN COMMANDS > set`.

One of the most common issues is running a BASH script with an undefined variable. BASH does not complain **at all** (and that's how I nuked 6.5TB of hard drives with a missing variable - but that's for another story) and execute your script as if an empty string was your value.

Why wouldn't you want to do that? Let's look at our example script:

```
#!/usr/bin/env bash

folder=$1
rm -fr /home/$USER/$folder
```

This simple script is supposed to delete user provided `$folder` in user home directory. What do you think will happen if `$1` (shell script first argument) is not provided? 😱 It will delete all your home folder. YAY. 
This is bad because `rm` is reasonably fast and unlinks the files, which means the OS may decide to write on the just created free space almost immediately; before you realize and hit CTRL+C (**don't do that**, read [here][2]) a huge portion will have been unlinked already. Recovering them is painful.

To prevent this you can use:
```
set -u
```
or its longest form:
```
set -o nounset
```

What to do with variables that you want to be empty, for example because you want to check for value? `nounset` refers to **unset** variables, which means any other value (even an empty one) satisfies this requirement.

My usual case is checking for environment variable, which can be done easily with:

```bash

if [ -z "${ENVVAR:-}" ]; then
    # here ENVVAR has non-zero length
else
    # here ENVVAR has zero length but does not trigger nounset option
fi
```

(`-z` is part of `test` utility and checks if the supplied argument is a zero-length string)

## Exit on error

> Exit immediately if a pipeline (which may consist of a single simple command), a list, or a compound command […], exits with a non-zero  status.

From [BASH manual][3], under `SHELL BUILTIN COMMANDS > set`.

When an error occurs in a BASH script, the script does not exit immediately but continue running; this can create weird situations (think about changing to a different folder, or running a setup command).

To prevent this use:
```
set -e
```
or its longest form:
```
set -o errexit
```

## Use the rightmost exit value for a pipeline

> If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands in the pipeline exit successfully.  

From [BASH manual][3], under `SHELL BUILTIN COMMANDS > set`.

When running a command pipeline (i.e `cat file | grep foo`) the exit status of the pipeline depends from the first command run. In this cat/grep case, if the file exist but does not contain `foo`, `cat` will exit with `0` but `grep` will exit with a non-zero exit code. Nevertheless the exit value for the entire expression would be `0`.

To prevent this use:
```
set -o pipefail
```

Combining `-e` and `-o pipefail` makes impossible to have "failing" commands (not part of conditions), like in the case above, because `-o pipefail` will make the pipeline exit with a non-zero code and `-e` will immediately halt the script. To prevent this, when you want to continue even in case of error you can end the pipeline with `|| true`; this instruction will run `true`, a utility that "do nothing, successfully" and change the rightmost exit code to `0`.

Es:
```bash
set -eo pipefail
cat file | grep foo || true
echo "continue"
```

Happy coding 😉

[1]: https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my
[2]: https://unix.stackexchange.com/a/101247/111295
[3]: https://man7.org/linux/man-pages/man1/bash.1.html
