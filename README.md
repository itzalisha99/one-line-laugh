# One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/itzalisha99/one-line-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/itzalisha99/one-line-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun — one funny line, at most 200 characters, judged two at a time by a house judge.

## The line

> I checked my bank balance and my phone asked if I wanted to turn on low power mode.

83 characters, one sentence. The setup is an everyday truth everyone recognises (checking a low balance); the turn at the end is the phone treating your poverty like a dying battery — a surprise that still makes sense once it arrives.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt`, with no trailing newline so the file is exactly 83 bytes. A `validate()` step mirrors the house gate (1–200 characters, UTF-8, one line, one sentence) and fails loudly instead of writing an invalid entry. The output is deterministic: repeated runs produce byte-identical files.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
