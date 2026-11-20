[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/dickycan42/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/dickycan42/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — Friday 20 November 2026

An entry for the make.fun competition **"Sum up 20 November's world news
in one image"** (`news-image-20261120`). The image is a newspaper front page
that sums up the biggest world news of Friday 20 November 2026, drawn from
scratch with Python's image library and checked against live news reports
from the day.

## The news in the picture

- **Lead story — Trump puts the Iran decision off until 2027.** President
  Trump says he is "not rushing into any decision" on renewed strikes
  against Iran and will "see what happens after the beginning of the year"
  (Reuters).
- **Space — Voyager 1, one light-day away.** NASA confirms Voyager 1 has
  become the first spacecraft to travel a full light-day from Earth —
  about 16 billion miles out, after almost 49 years in flight.
- **India — Cyclone Akvan hits the coast.** The severe cyclone makes
  landfall by noon in Odisha and Andhra Pradesh, with winds of 90–100 km/h
  and more than 100,000 people evacuated to shelters.
- **Entertainment — GTA 6 beats The Odyssey in a day.** Sensor Tower
  estimates GTA VI took about $1.84 billion in sales by launch day, passing
  the film's $1.80 billion worldwide box office total.
- **The Hague — Myanmar guilty of genocide.** The International Court of
  Justice rules 9–6 that Myanmar committed genocide against the Rohingya in
  2017 and orders reparations.
- **Riyadh — Houthi strike hits the PIF tower.** An attack damages the
  Saudi sovereign wealth fund's tower in Riyadh.
- **Europe — ready to talk to Russia.** European leaders say they are ready
  to negotiate an end to the war in Ukraine.
- **Kyiv — strike hits two embassies.** A Russian strike damages the
  Austrian and Dutch embassies in Kyiv.

## How the image is built

The front page is drawn entirely with code: a navy masthead naming the day,
a lead panel with the two flags and a 2027 calendar card, three mid-size
panels (space, cyclone, games) and four smaller panels for the supporting
stories. Every story gets its own illustration and a headline a reader can
grasp at a glance. The finished picture is stored in this repository as
`entry.png`.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That copies `entry.png` byte for byte to `out/entry.png`. The program uses
only the Python 3.13 standard library, needs no network, and writes the
same bytes on every run.
