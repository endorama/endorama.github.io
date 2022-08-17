---
title: "{{ replace .Name "-" " " | humanize }}"
date: {{ .Date }}
draft: true
type: {{ .Type | singularize }}
---

