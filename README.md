# one-word-for-your-wifi-01

[![One Word for Your Wi-Fi](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reren-dev/one-word-for-your-wifi-01/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reren-dev/one-word-for-your-wifi-01/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

An entry for the [One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) bounty on [make.fun](https://make.fun).

## The word

**Ghosted** — the Wi-Fi vanishes mid-sentence with no explanation, like
being ghosted. It is there one second and gone the next, no goodbye, no
reason, and you are left staring at a loading spinner. It is funny at once,
true to how home Wi-Fi actually behaves, and it works as a network name all
on its own: joining a network called "Ghosted" is already the joke.

## How it works

`main.py` (Python 3.13 standard library only, no network, no wall clock)
validates the word — a single word, letters only, at most 20 characters —
then writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default
`/output`), atomically via a temp file plus `os.replace`, and reads it back
to verify exactly what the judge will see.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/output python3 main.py
cat /tmp/output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
