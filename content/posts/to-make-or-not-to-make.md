---
title: "To make or not to make"
date: 2022-08-24T22:00:21+02:00
draft: true
type: post
tags: [devops, cli, tool, team, devx]
---

`make` is a renowned tool that is easily found in every project.
You can find it for a wide range of tasks, involved in all kinds of developer tooling gimmicks, but `make` is not a task runner, is a **build tool**, an extremely powerful build automation tool.
It's purpose is to **build** your program from its source files.

While this is great and for sure it can accomplish it's purpose, `Makefile`s have different disadvantages when used for purposes different than build automation:
- it has a complex syntax (es tabs vs spaces);
- documentation is sparse (`man` is cool but not what I hope for a collaboration tool);
- errors can be obscure;
- breaking a single `Makefile` into multiple ones is a pain;
- ironing out cross platform difference makes things worse.

These are not only `make`'s faults, as the issue lies in using it for something it was never meant to be used.
Writing great `Makefile`s is definetely possible, this [blog post](https://www.thapaliya.com/en/writings/well-documented-makefiles/) is an awesome example of it, but that requires high discipline and this does not play well with high pressure or tight deadlines.

Funny note while writing this post I discovered that someone implemented [FizzBuzz in GNU Make](https://www.reddit.com/r/programming/comments/412kqz/comment/cyzxqlx/) 🤯. You crazy 🤣

At this point it's clear there we may need an alternative, and indeed there are viable alternatives desined to be task runners with a decisive set of advantages:
- easier to use;
- kinder to your contributors;
- have a smaller learning curve;
- are overall simpler, in case you need to delve into the dirty bits;
- support advanced use cases (cross-platform specificity, import, overrides, help text).

Of all the available alternatives there is a set that stands out to me:
- `rake`
- `task`
- `just`

Before delving in a comparison, what are the features I look for?

I want this tool to be **ergonomic**: it should be intuitive (or at worst easy) to write task definition, dependencies and leverage external tools.  
I want this tool to be **powerful**: I need advanced features, like cross-platform overrides or imports.
I want this tool to be **welcoming**: documentation should be good and detail how to do things, allowing me to iterate fast.

## Rake

[Rake](https://ruby.github.io/rake) is a make-like build utility for Ruby. 
It uses a DSL to write terse and coincise tasks in Ruby code, automating the toil.

To me this is the best tool out there, its major drawback is being written in Ruby. This makes adding it to any pipeline for other languages a chore and require contributors to know Ruby. Not to mention having to install Ruby in your CI just for this. I would not advise to use this unless you're in a Ruby project.

## Task

[Task](https://taskfile.dev) is a task runner / simpler Make alternative written in Go.
It's a single binary, which makes it incredibly convenient to use and `Taskfile`s are written in YAML, which not being the best markup language out there is very effective and widespread.

This is my preferred choice as of today, is packed with a lot of features, from simple to very advanced and being a YAML file its syntax is decent.
This is a list from it's great feature set: allows to use Go template engine, has a cross-platform shell interpreter (works **on Windows**, for real!), Taskfile import, `.env` support, variables, dry run mode and a file watcher (and there are more!).

## Just

[Just](https://just.systems/) is a handy way to save and run project-specific commands.
It's a single binary like Task. It's DSL is as good as Rake, feels like a Makefile but is packed with features suited for a task runner.

Features include: multiple language support, parameters, `.env` support, running recipes in different folders.

I don't particularly like the [fallback to parent feature](https://just.systems/man/en/chapter_54.html) that feels a bit unpredictable or the need to write recipes in different languages within the same file (I generally put them in separate files and run them) thus is the one that gets my least preferred, but is very impressive and has some interesting patterns.

## Conclusions

Since some years ago I found my go to task runner in `task`, it evolved since I started using it (current `Taskfile` version is `3`) and packs all the feature I need (plus some more). But most of all I can use it without even looking at the documentation for simple use cases and can dive into the docs when I want to make things more complex.

An example is [`2ami` `Taskfile`](https://github.com/endorama/2ami/blob/master/Taskfile.yml) that helped me streamline the tool [release pipeline](https://github.com/endorama/2ami/blob/master/.github/workflows/release.yml) where I build it, compute checksum and create a GitHub release for 3 different Operating Systems.