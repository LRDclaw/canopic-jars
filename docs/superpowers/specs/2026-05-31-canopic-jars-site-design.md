# Canopic Jars Project Site — Design

**Date:** 2026-05-31
**Status:** Approved

## Summary

A scaffolded, mobile-first single-page website to host the information for Amilia's
school project on Canopic Jars. The scaffold is built now; Amilia fills in the body
content (images, captions, intro text, references, video) later and chooses the visual
style with a one-line change. The finished site is hosted publicly on GitHub Pages.

## Goals

- Mobile-first single scrolling page, viewable by a teacher and classmates.
- Built as a **placeholder scaffold** so Amilia can drop in content without touching layout.
- Visual style switchable by changing one word (three styles shipped).
- Permanent public URL via GitHub Pages.
- Editable by a non-technical student, guided by a plain-English README.

## Non-Goals (YAGNI)

- No CMS, no JavaScript framework, no build step.
- No contact form, no analytics, no comments.
- It is a static information page — nothing dynamic.

## Audience & Content

- **Audience:** school/academic — teacher and classmates.
- **Content (placeholders for now):** images with per-image captions, an optional embedded
  video, and a references/bibliography list. A short intro paragraph slot is included.
- Amilia already-has-or-will-supply the actual images and video; the scaffold ships with
  clearly labelled placeholder boxes and example blocks.

## Architecture

Plain static files, no build step:

| File | Purpose |
|------|---------|
| `index.html` | Page structure with clearly-marked, commented placeholder slots |
| `styles.css` | Mobile-first styling + three themes defined as CSS-variable sets |
| `images/` | Folder for Amilia to drop image files into |
| `README.md` | Plain-English editing + deploy guide for Amilia |
| `mockups/` | Style-reference mockups (kept for reference, **not** deployed) |

The site is fully usable by opening `index.html` directly or serving the folder; GitHub
Pages serves the repository root.

## Page Structure (single scrolling page, top → bottom)

1. **Header / hero** — project title ("Canopic Jars"), Amilia's name, one-line subtitle,
   hero image placeholder.
2. **Intro** — short introductory paragraph placeholder.
3. **Gallery** — captioned images, single column on mobile; each image full-width with its
   caption directly below. Ships with ~4 copy/paste example image+caption blocks.
4. **Video** — placeholder for an embedded video (YouTube embed or local file). Easy to
   remove if unused.
5. **References** — numbered bibliography list with placeholder entries.
6. **Footer** — small credit line ("A school project by Amilia · 2026").

Mobile-first: single column, full-width images, phone-sized tap targets, graceful scale-up
to laptop width via a max-width container and minimal breakpoints.

## Styling System

Three styles are pre-built as sets of CSS custom properties (variables):

- **`papyrus`** — warm sandstone / aged-papyrus tones, classic serif type (museum-label feel).
- **`dark-gold`** — near-black background with gold accents and cream text (dramatic).
- **`faience`** — white background with Egyptian faience-blue accents, sans-serif, very
  readable. **This is the default.**

The active style is selected by a single attribute on the `<body>` tag:

```html
<body data-theme="faience">   <!-- change to "papyrus" or "dark-gold" -->
```

Each theme is a `[data-theme="..."]` block in `styles.css` that overrides the colour/font
variables. Switching the whole look is a one-word edit. All layout rules read from the
variables so themes never touch structure.

## Placeholders & Editing Experience

- Every content slot is a visible, labelled placeholder box (e.g. "📷 IMAGE — replace me").
- An HTML comment sits directly above each slot telling Amilia exactly what to do, e.g.
  `<!-- Amilia: put your image file in images/ and change the filename below -->`.
- The gallery ships with ~4 example `image + caption` blocks she can duplicate to add more.
- `README.md` covers, in non-technical steps: add an image + caption, write the intro,
  add a reference, embed the video, switch the theme, and re-deploy.

## Hosting & Deploy (GitHub Pages)

1. User creates a free GitHub account and an empty public repository via github.com.
2. We initialise the local git repo in `/home/eag/canopic-jars`, commit, add the remote,
   and push (plain `git` — no `gh` CLI required; git 2.43 is installed, GitHub reachable).
3. User enables Pages in the repo settings (Deploy from branch → `main` → `/root`).
4. Result: a permanent public URL (e.g. `https://<user>.github.io/<repo>/`).
5. Update loop (documented in README): drop new images into `images/`, edit `index.html`,
   then `git add . && git commit -m "..." && git push` → live in ~1 minute.

`.gitignore` excludes `.superpowers/` (brainstorm session files).

## Testing / Verification

- Open `index.html` locally and serve the folder; confirm the page renders top-to-bottom
  with all sections and placeholder boxes visible.
- Switch `data-theme` between all three values; confirm each theme applies cleanly with no
  layout shift.
- Check rendering at a narrow (phone ~390px) width and a wide (laptop) width.
- After deploy: confirm the public GitHub Pages URL loads the same page.

## Open Items for Amilia (later, not part of scaffold)

- Final style choice (`data-theme` value).
- Actual images, captions, intro text, references, and video.
