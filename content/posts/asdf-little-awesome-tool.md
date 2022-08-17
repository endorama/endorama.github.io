---
title: "asdf, little awesome tool"
date: 2022-08-17T23:46:30+02:00
draft: true
type: post
tags: [devops, cli, tool, team, devx]
---

Some years ago I discovered a little tool with a huge potential. I started using it and since then it proved useful in so many ways it's now a mandatory tool in my toolset.

This tool is [`asdf`][0]. `asdf` is a CLI tool version manager. You may already be using multiple ones (`rbenv`, `nvm`, `goenv` to name a few) to manage versions of programming language tooling and accessories.

Having multiple tools for this purposes creates a series of disadvantages:
- setting up your workstation is more painful (multiple tools to install, multiple versions to manage); this become more complex when you work in a team and want to provide a great onboarding experience
- adopting a new tool force you to first search for a dedicated version manager, then install the tool (you may go without one, but that's going to bite your future self)
- how to share the same version in all environments, in particular dev and CI? Was that file `.go-version`, `.golang-version`? Each tool uses it's own convention, sometimes they align but having a consistent experience is not in their DNA;
- what's the command again? Each tool may have different CLI commands, making switching between them a pain; this may happen more easily if you're in a team;
- remember the [Good Old Times™ of “spaces VS tabs”][1]? Well, why start a 🔥 war around which tool to use?

Let's summarise why `asdf` is ground breaking: 
* helps developer onboarding across a wide set of tool;
* helps team collaborating;
* removes useless discussion drive by preference;
* has a consistent UI.

Would that be enough? NO 😜

It delivers more:
- [creating plugins][2] is **so easy** you can just add whatever you want (I did it [here][3], [here][4], [here][5] and [here][5]);
- creating plugins is most probably not needed because what you need is **already available**; [`asdf-community`][7] has 60 repositories (so around 60 plugins), just a `asdf plugin-add` away;
- are we forgetting the CI? Hell no! Note that this only works if you are using GitHub Actions, but if that's the case there are [actions ready to be used][8]. 

{{< tip >}}
In case you don't want to use the install action provided by the asdf community because it does not leverages other optimized setup actions I developed an action that parses the `.tool-versions` file extracting the tool version that can then be reused in other actions. No `asdf` needed!  
This action is available [here][link].

[link]: https://github.com/endorama/asdf-parse-tool-versions
{{< /tip >}}

If you reached this line, **STOP** right here and [go install][9] `asdf`.

[0]: https://asdf-vm.com/
[1]: https://www.reddit.com/r/programming/comments/p1j1c/tabs_vs_spaces_vs_both/
[2]: https://asdf-vm.com/plugins/create.html
[3]: https://github.com/endorama/asdf-desk
[4]: https://github.com/endorama/asdf-goreleaser
[5]: https://github.com/endorama/asdf-envchain
[6]: https://github.com/endorama/asdf-hugo
[7]: https://github.com/asdf-community
[8]: https://github.com/asdf-vm/actions
[9]: https://asdf-vm.com/guide/getting-started.html