---
title: "2ami"
date: 2022-09-17T00:32:25+02:00
draft: false
type: post
tags: [golang, cli, security, opensource]
---

Some years ago I was learning Golang and researching a 2FA tool to use in the command line (that I wanted to integrate with ULauncher, a Linux alternative to Alfred). The only tool I found was saving all secrets in a plain text file and I really wanted to avoid that.

So 2ami was born! 2ami is a small CLI tool that allows to generate 2FA tokens. Is a single binary you can run and uses your OS secure storage to store secrets. It's simple but complete and being my companion for years now.

I recently released 0.6.0, the first cross platform (Linux, macOS, Windows) build after fighting a lot with the CI (it needs CGO) and thanks to GitHub Actions (which I keep admiring for how powerful and effective they are).

If you want to checkit out ➡ https://lnkd.in/dWY-Y_6e