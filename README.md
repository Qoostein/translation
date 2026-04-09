# Retro Translations

I’ve been getting a lot of requests to translate Retro into other languages and I wanted to make this a community-effort.

Strings are **in-app** language (independent of the system locale).

[![Discord](https://badgen.net/discord/members/6v9TEhn)](https://discord.retromusic.co/)

## Layout

| Path | Purpose |
|------|---------|
| [`locales/en.json`](locales/en.json) | **Source of truth** for keys and English copy |
| `locales/<code>.json` | One file per language (`es`, `fr`, `de`, `zh`, `ja`, `ko`, …) |
| [`scripts/validate.py`](scripts/validate.py) | Ensures every locale has the same keys as English |

Keys are **flat** strings (e.g. `menu.music`, `status.loading`) and must stay stable so the app can look them up with `L.t("…")`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to open a pull request and what to change.

## Validation

From the repo root:

```bash
python3 scripts/validate.py
```

## Current Languages

- English (`en`)
- Spanish (`es`)
- German (`de`)
- French (`fr`)
- Japanese (`ja`)
- Korean (`ko`)
- Norwegian (`no`)
- Portuguese (`pt`)
- Russian (`ru`)
- Chinese (`zh`)
