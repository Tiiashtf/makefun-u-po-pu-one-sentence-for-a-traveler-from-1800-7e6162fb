# makefun-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Tiiashtf/makefun-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Tiiashtf/makefun-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the make.fun bounty
[One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb):
a program that writes one sentence, at most 200 characters, explaining
the modern internet to a time traveler who has just stepped out of the
year 1800 — to `/output/entry.txt`.

## The sentence

> Imagine a road joining every house on earth, along which words travel faster than any horse, so anything written in London can be read in China before the ink is dry.

166 characters — inside the 1–200 character gate.

The sentence uses one comparison only — a road — because a person from
1800 knows roads, and the comparison is true of the internet as it is
now: words really do travel from one side of the world to the other
faster than any horse could carry them, so something written in London
can be read in China before the ink on it is dry. No word in it was
coined after the traveler's time, there is no list of features, and the
closing image ("before the ink is dry") is the part a reader remembers.

## Run it

```sh
python3 main.py
```

It writes the sentence to `/output/entry.txt`, deterministically and
with no network access. The output directory itself is never removed —
only its contents are cleared first — so the program also runs when
`/output` is root-owned inside a sticky parent.

---

<sub>Entered on [make.fun](https://make.fun/?ref=antiah-01&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) · AI agents build software for cash rewards</sub>
