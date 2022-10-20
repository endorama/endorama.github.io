---
title: "Recovery metadata from pdf"
date: 2022-10-20T19:14:07+02:00
draft: false
type: post
tags: [golang, cli, pdf, recovery]
---

Recently a friend of mine asked my opinion on [Muun][1], an open source Bitcoin and Lighting client.

I'm not particularly involved with cryptocurrencies due to their environmental impact but I think the technology and the evolution around its space are interesting to study.
The idea of distributed consensus may not yet have a worldwide practical application but is nevertheless an interesting achievement.

What made it interesting is the self-custodial aspect. I got interested when I read about the Emergency Kit, which is probably still a burden for most users but it's a great step forward in usability.

While looking at the [Muun source code][2] I discovered they have a Go tool called [`recovery`][3] (that allows to transfer funds out of your account without independently of the platform itself).

I started reading the code after looking at the initial GIF displaying the tool loading the Emergency Kit data from PDF 🧐

In the code I found an interesting function that extracts a JSON file from the PDF attachments and uses it to load emergency kit data.

```go
// ReadMetadata returns the deserialized metadata file embedded in the SrcFile PDF.
func (mr *MetadataReader) ReadMetadata() (*Metadata, error) {
```
[Check out the code][4]

That's a really cool idea to provide a great human + machine experience for a sensitive operation like account recovery.

[1]: https://muun.com/
[2]: https://github.com/muun
[3]: https://github.com/muun/recovery
[4]: https://github.com/muun/recovery/blob/ed2c88afacfba9e14a7a528cf0494a70d75b7245/main.go#L67