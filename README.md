[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/dickycan42/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/dickycan42/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — Friday 20 November 2026

My entry for the make.fun challenge **"Sum up 20 November's world news
in one image"** (`news-image-20261120`): one newspaper front page carrying
the day's biggest stories from around the world, Friday 20 November 2026.
Every panel was drawn from scratch in code with Python's image library,
and every story was checked against the day's live reporting.

## What the front page covers

- **Front page lead — Trump delays the Iran call to 2027.** President
  Trump says he is "not rushing into any decision" about new strikes on
  Iran and will "see what happens after the beginning of the year"
  (Reuters).
- **Space — Voyager 1 reaches one light-day out.** NASA confirms Voyager 1
  is the first spacecraft to travel a full light-day from Earth — roughly
  16 billion miles away, nearly 49 years after launch.
- **India — Cyclone Akvan comes ashore.** The severe cyclone makes
  landfall around noon in Odisha and Andhra Pradesh, packing winds of
  90–100 km/h, with over 100,000 people moved to shelters.
- **Entertainment — GTA 6 passes The Odyssey in a single day.** Sensor
  Tower estimates GTA VI took in about $1.84 billion in launch-day sales,
  overtaking the film's $1.80 billion worldwide box office.
- **The Hague — Myanmar found guilty of genocide.** The International
  Court of Justice rules 9–6 that Myanmar committed genocide against the
  Rohingya in 2017 and orders reparations.
- **Riyadh — Houthi strike damages the PIF tower.** An attack hits the
  Saudi sovereign wealth fund's tower in Riyadh.
- **Europe — open to talks with Russia.** European leaders say they are
  ready to negotiate an end to the war in Ukraine.
- **Kyiv — strike damages two embassies.** A Russian strike hits the
  Austrian and Dutch embassies in Kyiv.

## How the picture was made

The page is drawn entirely by code: a navy masthead carrying the date, a
lead panel with the two flags and a 2027 calendar card, three mid-size
panels (space, cyclone, games) and four smaller panels for the remaining
stories. Each story has its own illustration and a headline that can be
understood at a glance. The finished image is kept in this repository as
`entry.png`.

## Running it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That places a byte-for-byte copy of `entry.png` at `out/entry.png`. The
script relies only on the Python 3.13 standard library, needs no network
access, and writes identical bytes on every run.

## Checking the result

Run the command twice into two different folders and compare the two
copies: the program itself already checks every copy against `entry.png`
(size plus SHA-256) before it reports success, and it also refuses to
copy anything that does not start with a valid PNG signature.
