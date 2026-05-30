# Canopic Jars Project Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a mobile-first, single-page scaffold website for Amilia's school project on Canopic Jars — placeholder content slots, a one-line theme switch (3 styles), and a GitHub Pages deploy path.

**Architecture:** Plain static files — `index.html` + `styles.css` + `images/` + `README.md`. No build step, no framework, no JavaScript. Three visual themes are defined as CSS-variable sets selected by a `data-theme` attribute on `<body>`. Hosted on GitHub Pages from the repo root.

**Tech Stack:** HTML5, CSS3 (custom properties, flexbox), git, GitHub Pages. Python 3 `http.server` is used only for local verification.

---

## File Structure

| File | Responsibility |
|------|---------|
| `index.html` | Page structure: hero, intro, gallery, video, references, footer — all placeholder content with `<!-- Amilia: ... -->` comments |
| `styles.css` | Mobile-first layout reading from CSS variables, plus three `[data-theme]` blocks (faience default, papyrus, dark-gold) |
| `images/.gitkeep` | Keeps the (initially empty) images folder in git for Amilia to drop files into |
| `README.md` | Non-technical editing + deploy guide |
| `.gitignore` | Excludes `.superpowers/` (already created) |
| `mockups/` | Style-reference mockups — kept, NOT deployed (harmless extra file on Pages; documented in README) |

Repo already initialised at `/home/eag/canopic-jars` with `.gitignore` and the design doc committed.

---

### Task 1: Create the images folder placeholder

**Files:**
- Create: `images/.gitkeep`

- [ ] **Step 1: Create the empty images folder marker**

```bash
cd /home/eag/canopic-jars
mkdir -p images
touch images/.gitkeep
```

- [ ] **Step 2: Verify it exists**

Run: `ls -la /home/eag/canopic-jars/images/`
Expected: shows `.gitkeep`

- [ ] **Step 3: Commit**

```bash
cd /home/eag/canopic-jars
git add images/.gitkeep
git commit -m "Add images folder for Amilia's pictures"
```

---

### Task 2: Build index.html

**Files:**
- Create: `index.html`

- [ ] **Step 1: Write the full page**

Write `/home/eag/canopic-jars/index.html` with exactly this content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Canopic Jars — A Project by Amilia</title>
  <link rel="stylesheet" href="styles.css">
</head>
<!-- Amilia: change data-theme to "papyrus", "dark-gold", or "faience" to switch the whole look -->
<body data-theme="faience">

  <!-- ============ HERO ============ -->
  <header class="hero">
    <p class="kicker">Ancient Egypt</p>
    <!-- Amilia: this is the main title -->
    <h1>Canopic Jars</h1>
    <p class="subtitle">A school project by Amilia</p>
    <!-- Amilia: put a hero image in images/ and set its filename below, then delete the placeholder div -->
    <!-- <img class="hero-img" src="images/hero.jpg" alt="Canopic jars"> -->
    <div class="hero-img placeholder">📷 HERO IMAGE — replace me</div>
  </header>

  <main class="container">

    <!-- ============ INTRO ============ -->
    <section class="intro">
      <h2>Introduction</h2>
      <!-- Amilia: write a short paragraph introducing Canopic Jars here -->
      <p>Write a short introduction here — what Canopic Jars are and why they
      mattered in ancient Egyptian burials. Replace this whole paragraph.</p>
    </section>

    <!-- ============ GALLERY ============ -->
    <section class="gallery">
      <h2>Gallery</h2>

      <!-- Amilia: copy one whole "figure" block below to add more images.
           Put the image file in images/ and change the src filename and the caption text. -->

      <figure class="image-card">
        <!-- <img src="images/jar1.jpg" alt="Describe the image"> -->
        <div class="img placeholder">📷 IMAGE 1 — replace me</div>
        <figcaption>Caption: what this image shows and where it is from.</figcaption>
      </figure>

      <figure class="image-card">
        <!-- <img src="images/jar2.jpg" alt="Describe the image"> -->
        <div class="img placeholder">📷 IMAGE 2 — replace me</div>
        <figcaption>Caption: what this image shows and where it is from.</figcaption>
      </figure>

      <figure class="image-card">
        <!-- <img src="images/jar3.jpg" alt="Describe the image"> -->
        <div class="img placeholder">📷 IMAGE 3 — replace me</div>
        <figcaption>Caption: what this image shows and where it is from.</figcaption>
      </figure>

      <figure class="image-card">
        <!-- <img src="images/jar4.jpg" alt="Describe the image"> -->
        <div class="img placeholder">📷 IMAGE 4 — replace me</div>
        <figcaption>Caption: what this image shows and where it is from.</figcaption>
      </figure>
    </section>

    <!-- ============ VIDEO (optional — delete this whole section if not used) ============ -->
    <section class="video">
      <h2>Video</h2>
      <!-- Amilia (YouTube): copy the share link, replace VIDEO_ID below, then delete the placeholder div.
           <div class="video-frame">
             <iframe src="https://www.youtube.com/embed/VIDEO_ID"
                     title="Project video" allowfullscreen></iframe>
           </div>
      -->
      <!-- Amilia (your own video file): put it in images/ and use:
           <video class="video-frame" controls src="images/myvideo.mp4"></video>
      -->
      <div class="video-frame placeholder">🎬 VIDEO — replace me (or delete this section)</div>
    </section>

    <!-- ============ REFERENCES ============ -->
    <section class="references">
      <h2>References</h2>
      <!-- Amilia: replace each list item with a real source. Add or remove <li> lines as needed. -->
      <ol>
        <li>Source one — author, title, year.</li>
        <li>Source two — author, title, year.</li>
        <li>Source three — author, title, year.</li>
      </ol>
    </section>

  </main>

  <!-- ============ FOOTER ============ -->
  <footer class="site-footer">
    <p>A school project by Amilia · 2026</p>
  </footer>

</body>
</html>
```

- [ ] **Step 2: Verify the file contains every required section**

Run:
```bash
cd /home/eag/canopic-jars
grep -c -E 'class="hero"|class="intro"|class="gallery"|class="video"|class="references"|class="site-footer"' index.html
```
Expected: `6`

- [ ] **Step 3: Verify the theme attribute is present**

Run: `grep -o 'data-theme="faience"' /home/eag/canopic-jars/index.html`
Expected: `data-theme="faience"`

- [ ] **Step 4: Commit**

```bash
cd /home/eag/canopic-jars
git add index.html
git commit -m "Add page structure with placeholder content slots"
```

---

### Task 3: Build styles.css — base layout (mobile-first) + variables

**Files:**
- Create: `styles.css`

- [ ] **Step 1: Write the base stylesheet (variables + layout, no themes yet)**

Write `/home/eag/canopic-jars/styles.css` with exactly this content:

```css
/* ===== Variables (overridden per-theme lower in this file) ===== */
:root {
  --bg: #ffffff;
  --text: #1f2d3d;
  --muted: #5a6b7b;
  --accent: #0d7a8c;
  --accent-contrast: #ffffff;
  --panel: #f7fafb;
  --border: #e2e8ec;
  --font-head: 'Segoe UI', system-ui, sans-serif;
  --font-body: 'Segoe UI', system-ui, sans-serif;
}

/* ===== Reset / base (mobile-first) ===== */
* { box-sizing: border-box; margin: 0; padding: 0; }

html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 17px;
  line-height: 1.6;
}

img { max-width: 100%; display: block; }

h1, h2 { font-family: var(--font-head); line-height: 1.2; }

/* ===== Layout container ===== */
.container { width: 100%; max-width: 760px; margin: 0 auto; padding: 0 18px; }

section { padding: 32px 0; border-bottom: 1px solid var(--border); }
section:last-child { border-bottom: none; }
section h2 {
  font-size: 14px; letter-spacing: .14em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 16px;
}

/* ===== Hero ===== */
.hero { background: var(--accent); color: var(--accent-contrast); text-align: center; padding: 40px 18px 0; }
.hero .kicker { font-size: 12px; letter-spacing: .22em; text-transform: uppercase; opacity: .85; }
.hero h1 { font-size: 40px; margin: 10px 0 6px; }
.hero .subtitle { font-size: 16px; opacity: .9; margin-bottom: 28px; }
.hero-img { height: 200px; border-radius: 10px 10px 0 0; object-fit: cover; width: 100%; }

/* ===== Intro ===== */
.intro p { color: var(--text); }

/* ===== Gallery ===== */
.image-card {
  margin-bottom: 22px; border-radius: 10px; overflow: hidden;
  border: 1px solid var(--border); background: var(--panel);
}
.image-card img, .image-card .img { width: 100%; }
.image-card .img { height: 220px; }
.image-card figcaption { padding: 12px 14px; font-size: 15px; color: var(--muted); }

/* ===== Video ===== */
.video-frame {
  width: 100%; aspect-ratio: 16 / 9; border: none; border-radius: 10px;
  background: var(--panel);
}
.video-frame iframe { width: 100%; height: 100%; border: none; }

/* ===== References ===== */
.references ol { padding-left: 22px; }
.references li { margin-bottom: 10px; color: var(--muted); }

/* ===== Footer ===== */
.site-footer { background: var(--accent); color: var(--accent-contrast); text-align: center; padding: 20px; font-size: 14px; }

/* ===== Placeholder boxes (visible until Amilia replaces them) ===== */
.placeholder {
  display: flex; align-items: center; justify-content: center;
  text-align: center; color: var(--muted); font-size: 14px; letter-spacing: .04em;
  background: repeating-linear-gradient(45deg, var(--panel), var(--panel) 12px, var(--border) 12px, var(--border) 24px);
}

/* ===== Wider screens (scale up gracefully) ===== */
@media (min-width: 720px) {
  .hero h1 { font-size: 52px; }
  .hero-img { height: 300px; }
  .image-card .img { height: 320px; }
}
```

- [ ] **Step 2: Verify CSS references all the classes used in index.html**

Run:
```bash
cd /home/eag/canopic-jars
for c in hero kicker subtitle hero-img container image-card video-frame references site-footer placeholder; do
  grep -q "\.$c" styles.css && echo "OK $c" || echo "MISSING $c"
done
```
Expected: every line says `OK`

- [ ] **Step 3: Commit**

```bash
cd /home/eag/canopic-jars
git add styles.css
git commit -m "Add mobile-first base styles and layout"
```

---

### Task 4: Add the three themes to styles.css

**Files:**
- Modify: `styles.css` (append theme blocks at the end)

- [ ] **Step 1: Append the three theme blocks**

Append the following to the END of `/home/eag/canopic-jars/styles.css`:

```css

/* ===================================================================
   THEMES — set <body data-theme="..."> in index.html to switch.
   faience (default) is already defined in :root above.
   =================================================================== */

/* --- Papyrus: warm, classic, serif (museum-label feel) --- */
[data-theme="papyrus"] {
  --bg: #f3e9d2;
  --text: #3a2e1f;
  --muted: #6b5a32;
  --accent: #8a6d2e;
  --accent-contrast: #fdf7e6;
  --panel: #ece0c2;
  --border: #cdb985;
  --font-head: Georgia, 'Times New Roman', serif;
  --font-body: Georgia, 'Times New Roman', serif;
}
[data-theme="papyrus"] .hero { background: #e3d3aa; color: #6b4f1d; }
[data-theme="papyrus"] .site-footer { background: #e3d3aa; color: #6b5a32; }

/* --- Dark & Gold: dramatic, museum-at-night --- */
[data-theme="dark-gold"] {
  --bg: #14110c;
  --text: #e8e0cf;
  --muted: #b3a578;
  --accent: #d4af37;
  --accent-contrast: #14110c;
  --panel: #1f190f;
  --border: #3a2f1a;
  --font-head: 'Segoe UI', system-ui, sans-serif;
  --font-body: 'Segoe UI', system-ui, sans-serif;
}
[data-theme="dark-gold"] .hero { background: linear-gradient(#1d1810, #14110c); color: #f0d77a; }
[data-theme="dark-gold"] .site-footer { background: #1b160e; color: #b3a578; }

/* --- Faience: clean & bright (DEFAULT, lives in :root). Listed here for clarity. --- */
[data-theme="faience"] {
  --bg: #ffffff;
  --text: #1f2d3d;
  --muted: #5a6b7b;
  --accent: #0d7a8c;
  --accent-contrast: #ffffff;
  --panel: #f7fafb;
  --border: #e2e8ec;
  --font-head: 'Segoe UI', system-ui, sans-serif;
  --font-body: 'Segoe UI', system-ui, sans-serif;
}
```

- [ ] **Step 2: Verify all three themes are defined**

Run:
```bash
cd /home/eag/canopic-jars
for t in papyrus dark-gold faience; do
  grep -q "\[data-theme=\"$t\"\]" styles.css && echo "OK $t" || echo "MISSING $t"
done
```
Expected: `OK papyrus`, `OK dark-gold`, `OK faience`

- [ ] **Step 3: Commit**

```bash
cd /home/eag/canopic-jars
git add styles.css
git commit -m "Add three switchable themes (faience default, papyrus, dark-gold)"
```

---

### Task 5: Local rendering verification

**Files:** none (verification only)

- [ ] **Step 1: Serve the site locally in the background**

Run (use the Bash tool's `run_in_background: true`):
```bash
cd /home/eag/canopic-jars && python3 -m http.server 8078 --bind 0.0.0.0
```

- [ ] **Step 2: Confirm the page is served**

Run:
```bash
python3 -c "import urllib.request as u; print(u.urlopen('http://127.0.0.1:8078/', timeout=3).status)"
```
Expected: `200`

- [ ] **Step 3: Confirm the served HTML links the stylesheet and all sections render**

Run:
```bash
python3 - <<'PY'
import urllib.request as u
html = u.urlopen('http://127.0.0.1:8078/', timeout=3).read().decode()
for needle in ['styles.css','class="hero"','class="gallery"','class="references"','data-theme="faience"']:
    print('OK' if needle in html else 'MISSING', needle)
css = u.urlopen('http://127.0.0.1:8078/styles.css', timeout=3).read().decode()
for needle in ['[data-theme="papyrus"]','[data-theme="dark-gold"]','--accent']:
    print('OK' if needle in css else 'MISSING', needle)
PY
```
Expected: every line says `OK`

- [ ] **Step 4: Visual check (human-in-the-loop)**

Tell the user to open `http://192.168.88.14:8078/` (open firewall port 8078 with `sudo ufw allow 8078/tcp` if needed) and confirm on a phone-width window:
- Hero, intro, four gallery placeholders with captions, video placeholder, references list, footer all appear top-to-bottom.
- Then ask them to temporarily edit `index.html` `data-theme` to `papyrus` and `dark-gold`, reload, and confirm each theme changes colours/fonts with no broken layout. Reset to `faience` after.

- [ ] **Step 5: Stop the local server**

Stop the background server task once the visual check passes.

---

### Task 6: Write README.md editing + deploy guide

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the guide**

Write `/home/eag/canopic-jars/README.md` with exactly this content:

```markdown
# Canopic Jars — Amilia's Project Site

A single-page website for the Canopic Jars project. Everything is plain HTML and CSS —
no special software needed to edit it.

## The files

- `index.html` — the page text and images go here
- `styles.css` — colours and fonts (you normally don't need to touch this)
- `images/` — put your picture and video files in this folder
- `mockups/` — style previews only; ignore it

## How to edit (open `index.html` in any text editor)

Look for green `<!-- Amilia: ... -->` notes — they tell you exactly what to change.

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
```

- [ ] **Step 2: Verify the README mentions the key tasks**

Run:
```bash
cd /home/eag/canopic-jars
for k in data-theme images/ "GitHub Pages" References; do
  grep -q "$k" README.md && echo "OK $k" || echo "MISSING $k"
done
```
Expected: every line says `OK`

- [ ] **Step 3: Commit**

```bash
cd /home/eag/canopic-jars
git add README.md
git commit -m "Add editing and deploy guide for Amilia"
```

---

### Task 7: Deploy to GitHub Pages (human-in-the-loop)

**Files:** none (deploy only)

- [ ] **Step 1: User creates GitHub account + empty public repo**

Ask the user to:
1. Sign up / sign in at https://github.com.
2. Create a new **public** repository named e.g. `canopic-jars` — do NOT add a README/.gitignore (the repo already has them).
3. Copy the repo URL (e.g. `https://github.com/USERNAME/canopic-jars.git`).

- [ ] **Step 2: Connect the local repo to GitHub and push**

With the URL from Step 1 (substitute it for `<REPO_URL>`):
```bash
cd /home/eag/canopic-jars
git branch -M main
git remote add origin <REPO_URL>
git push -u origin main
```
Note: GitHub will prompt for credentials. If a password is rejected, the user must create a
Personal Access Token (GitHub → Settings → Developer settings → Tokens) and use it as the password.

- [ ] **Step 3: Enable Pages**

Ask the user, in the repo on github.com: **Settings → Pages → Source: Deploy from a branch →
Branch: `main`, folder `/ (root)` → Save.**

- [ ] **Step 4: Verify the live site**

Wait ~1–2 minutes, then:
```bash
python3 -c "import urllib.request as u; print(u.urlopen('https://USERNAME.github.io/canopic-jars/', timeout=10).status)"
```
Expected: `200` (substitute the real username). Also open the URL in a browser to confirm the page renders.

---

## Notes for the implementer

- No automated test framework — this is a static site. Verification = serving locally and
  checking the served HTML/CSS contains the required markers, plus a human visual check.
- Keep all content as placeholders. Do NOT invent real Canopic Jars text/images — Amilia
  supplies the real content later.
- `mockups/` is committed and will also deploy to Pages; that's harmless. Leave it.
