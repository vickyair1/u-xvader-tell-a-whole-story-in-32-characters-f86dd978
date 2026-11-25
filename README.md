# Tell a Whole Story in 32 Characters

[![Competition](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/vickyair1/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/vickyair1/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [Tell a Whole Story in 32 Characters](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) bounty on [make.fun](https://make.fun).

## The entry

```
She took the dog AND the WiFi
```

29 characters. One Wi-Fi network name that lands a joke and implies a
whole story: a breakup told in a single line. She walked out with the
dog — and with the Wi-Fi too, as if the router were a prized possession
worth fighting over in the split. The punchline is the Wi-Fi ranked
beside the dog, the two things that mattered most.

## How it works

`main.py` writes the entry deterministically to `entry.txt` (and to
`/output/entry.txt` when that sandbox output directory is available
and does not already hold another entry). No network, no randomness,
no input — the same bytes on every run.

```sh
python3 main.py
cat entry.txt
```

## Files

- `main.py` — the entry program (entrypoint)
- `entry.txt` — the generated entry (29 chars)
- `LICENSE` — MIT
