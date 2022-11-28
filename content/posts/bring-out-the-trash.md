---
title: "Bring out the trash!"
date: 2022-11-28T20:31:39+01:00
draft: false
type: post
tags: [disk, cleanup, nix, snap]
---

I recently stumbled upon the usual issue with all my development machines: "no space left on device".

As it happens frequently, I had to spin up the trusted disk analyser, [Baobab](https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer?action=show&redirect=Apps%2FBaobab) and dig into it.

Something was filling up my 512GB disk, but exactly what?

## My home folder

Well, that wasn't that suprising, but:
1. My Trash was `31.2GB`! 
2. I used [asdf]({{< ref "asdf-little-awesome-tool" >}}) to manage programming language interpreter/runtimes, this was taking `~30GB`, 24 of them being taken by Golang installations and relative packages
3. My `code` folder, where I keep all code I've been hacking/working on, was `~24GB` ⛰ Massive!

## Nix

I started playing with [Nix](https://nixos.org/) and [Home Manager](https://github.com/nix-community/home-manager) to manage external binaries I want to add to my workstation (that runs elementary OS Hera at the moment).

It replaces [Homebrew](https://brew.sh/), that I loved but has it's drawbacks on Linux: compiling things was a total nightmare, and it happened quite a lot.

I was also extremely intrigued by the declarative approach Nix that promises reproducible configurations, something I'm trying to achieve to reduce surprises (works on my computer means work on remote server, this is a dream for a SysAdmin).

In the end I had 99GB in `/nix` 😱

To clean them up I discovered I needed to run GC and optimise the `nix-store`:

```
$ nix-store --gc
$ nix-store --optimise
$ nix-collect-garbage -d
```

These commands combined cleaned up around `50GB` of disk space 😎

I followed along [this](https://nixos.wiki/wiki/Cleaning_the_nix_store) and [this](https://nixos.wiki/wiki/Storage_optimization) articles.

## Snaps

The next step were snaps, where `~7GB` where used.

2 steps here:
- reduced the number of retained versions to 2 (default is 3)
- cleanup all disabled snaps

I followed instructions on [this article](https://www.debugpoint.com/clean-up-snap/), with the addition of using this command to check for active services:
```
$ snap info "$snapname" | grep -w active
```