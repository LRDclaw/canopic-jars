# Canopic Jars — Amila Galvao's Project Site

A single-page website for the Canopic Jars project. Everything is plain HTML and CSS —
no special software needed to edit it.

## The files

- `index.html` — the page text and images go here
- `styles.css` — colours and fonts (you normally don't need to touch this)
- `images/` — put your picture and video files in this folder
- `mockups/` — style previews only; ignore it

## How to edit (open `index.html` in any text editor)

Look for green `<!-- Amila: ... -->` notes — they tell you exactly what to change.

### Change the look (3 styles)
At the top of `index.html` find:
`<body data-theme="faience">`
Change `faience` to `papyrus` or `dark-gold` and save. That switches the whole style.

### Add a picture with a caption
1. Put your image file in the `images/` folder (e.g. `images/jar5.jpg`).
2. In `index.html`, copy one whole `<figure class="image-card"> ... </figure>` block.
3. Delete the grey placeholder `<div class="img placeholder">...</div>` line.
4. Uncomment the `<img ...>` line above it and change the filename to your file.
5. Change the caption text.

### Write the introduction
Find the `Introduction` section and replace the paragraph text.

### Add a video
In the `Video` section, follow the green notes: paste a YouTube embed link, or point to
a video file in `images/`. If you don't want a video, delete the whole `<section class="video">` block.

### Add references
In the `References` section, edit the list items. Add or remove `<li>...</li>` lines.

## Preview your changes BEFORE publishing

You can see your edits locally without committing anything. They're just files, so
there's nothing to build.

**Easiest:** open `index.html` directly in a web browser (double-click it, or right-click →
Open With → your browser). Refresh after each save to see changes.

**Live preview server** (lets you view from another device on the same WiFi):
1. In a terminal, from this folder, run:
   ```bash
   python3 -m http.server 8077
   ```
2. On this machine open `http://localhost:8077/`, or from another device on the same
   network open `http://192.168.88.14:8077/`.
3. Edit a file, **save**, then **refresh** the browser — your change shows up immediately.
4. Press `Ctrl+C` in the terminal to stop the preview server when done.

Nothing is published until you commit and push (next section).

## How to put it online (GitHub Pages)

First time:
1. Create a free account at https://github.com and a new **public** repository.
2. In this folder, run the commands GitHub shows you (your helper set the first ones up):
   ```bash
   git add .
   git commit -m "My project content"
   git push
   ```
3. In the repo on GitHub: **Settings → Pages → Build from branch → `main` / root → Save**.
4. After ~1 minute your site is live at `https://YOUR-USERNAME.github.io/REPO-NAME/`.

To update later (after editing):
```bash
git add .
git commit -m "Updated content"
git push
```
The live site updates in about a minute.
