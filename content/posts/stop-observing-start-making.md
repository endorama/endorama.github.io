---
title: "Stop observing, start making"
date: 2022-11-03T18:21:16+01:00
draft: false
type: post
tags: [o11y, development, devops]
---

Observability has become the read-it-everywhere buzzword of software development. Like others before it.

Observing any piece of technology is incredibly easy.  
Look at your screen, intensely.  
Do it some more.  
You are observing technology. If it's on, you are observing software too.

So what now? You basically know nothing more about your system now that you did before observing it (except for, is it on 🔥?).

The reason why _observing_ a piece of software is just a useless exercise is because observability is not an action.
There is no way you can **observe** a system, unless the system itself is **observable**.

> The term “observability” was coined by engineer Rudolf E. Kálmán in 1960.  
> In his 1960 paper, Kálmán introduced a characterization he called observability to describe mathematical control systems. In control theory, observability is defined as a measure of how well internal states of a system can be inferred from knowledge of its external outputs.

_The Mathematical Definition of Observability from [Observability Engineering by Charity Majors, Liz Fong-Jones, George Miranda][1]_

Observability is not the act of observing a system, is building its observable properties so you can **extract** meaningful **information** when observing it.
Gathering the data is the **first step** in "observability", but you **have to explore them** to conclude they are of any value.

So stop observing and start making your systems observable.

If this reasoning did not convince you yet, happy to provide more clues supporting this conclusion.

**Charity Majors in [Observability is a Many-Splendored Definition](https://charity.wtf/2020/03/03/observability-is-a-many-splendored-thing/)**

> Plenty of tools are terrific at helping you ask the questions you could predict wanting to ask in advance. […] But if you *can’t* predict all the questions you’ll need to ask in advance, or if you *don’t* know what you’re looking for, then you’re in o11y territory.

**Jean Yang in [Observability Isn't About Logs, Metrics, and Traces](https://www.akitasoftware.com/blog-posts/observability-isnt-about-logs-metrics-and-traces)**

> To generalize, observability is about helping people build models of their systems so they can: Understand your system better to move faster. Get visibility into how your system is actually running. Keep an eye on how your system changes.  

**Dotan Horovits in [Observability Is A Data Analytics Problem](https://insidebigdata.com/2022/04/07/observability-is-a-data-analytics-problem/)**

> However logs, metrics and traces are, by themselves, not Observability. In fact, many organizations collect logs, metrics and traces, and still end up with poor observability. […] But more importantly, we need to remember that these signals are, after all, the raw data. And we’re looking for the insights and the root cause analysis, to understand our system.

**Multiple authors @ Google in [Site Reliability Workbook](https://sre.google/workbook/reaching-beyond/)**

> Your Users, Not Your Monitoring, Decide Your Reliability  
> […] Your monitoring, logs, and alerting are valuable only insofar as they help you notice problems before your customers do. 

It's a long journey from here, but rewarding.


[1]: https://www.oreilly.com/library/view/observability-engineering/9781492076438/