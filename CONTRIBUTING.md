# Contributing translations

Thank you for helping improve the Retro's localized strings.

## Which file to edit

- Edit **`locales/<language-code>.json`** for the language you know (e.g. `es.json` for Spanish).
- **Do not rename keys** (the left-hand strings in `"key": "value"`). Only change the **values** (the translated text).
- **`locales/en.json`** is the canonical list of keys. New keys are added in English first; other locales should then add the same keys.

## Pull requests

- One **language per PR** is easier to review (optional but appreciated).
- Run validation locally before opening a PR:

  ```bash
  python3 scripts/validate.py
  ```

- If a PR fails CI, fix **missing or extra keys** so every `locales/*.json` matches the key set in `en.json`.

## Adding a new language

1. Copy `locales/en.json` to `locales/<new-code>.json` (use a short code consistent with the app, e.g. `it` for Italian).
2. Translate all **values**; leave **keys** unchanged.
