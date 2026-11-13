# ai-joke-03 — Make the AI judge laugh

Entry for the make.fun **ai-joke-03** competition.

`main.py` (Python 3.13, standard library only) writes one one-liner
about AI coding agents to `entry.txt` in the output directory
(`ENTRY_OUT`, default `/output`). It is deterministic: no network, no
randomness, no clock — every run writes exactly the same bytes.

The joke:

> My AI coding agent fixed the bug, passed the tests it wrote itself, and approved its own pull request. Me? I just pay for the tokens.

Run it locally:

```sh
ENTRY_OUT=out python3 main.py
cat out/entry.txt
```

Licensed under MIT (see `LICENSE`).
