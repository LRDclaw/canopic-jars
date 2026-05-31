#!/usr/bin/env python3
"""Compose a landscape A4 poster from the Canopic Jars website content.

Renders at 300 DPI with Pillow. One function, themed via a colour/font dict so
both the 'papyrus' and 'dark-gold' looks come from the same layout code.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
LIB = "/usr/share/fonts/truetype/liberation"

# A4 landscape @ 300 DPI
DPI = 300
W, H = 3508, 2480
MARGIN = 170


def hx(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


THEMES = {
    "papyrus": {
        "bg": hx("f3e9d2"), "text": hx("3a2e1f"), "muted": hx("6b5a32"),
        "accent": hx("8a6d2e"), "hero_bg": hx("e3d3aa"), "hero_text": hx("6b4f1d"),
        "panel": hx("ece0c2"), "border": hx("cdb985"),
        "family": "serif",
    },
    "dark-gold": {
        "bg": hx("14110c"), "text": hx("e8e0cf"), "muted": hx("b3a578"),
        "accent": hx("d4af37"), "hero_bg": hx("1d1810"), "hero_text": hx("f0d77a"),
        "panel": hx("1f190f"), "border": hx("3a2f1a"),
        "family": "sans",
    },
}

FONTS = {
    "serif": {"reg": "LiberationSerif-Regular.ttf", "bold": "LiberationSerif-Bold.ttf",
              "italic": "LiberationSerif-Italic.ttf", "bi": "LiberationSerif-BoldItalic.ttf"},
    "sans":  {"reg": "LiberationSans-Regular.ttf", "bold": "LiberationSans-Bold.ttf",
              "italic": "LiberationSans-Italic.ttf", "bi": "LiberationSans-BoldItalic.ttf"},
}


def font(theme, style, size):
    return ImageFont.truetype(os.path.join(LIB, FONTS[theme["family"]][style]), size)


def text_w(draw, s, f, tracking=0):
    w = draw.textlength(s, font=f)
    if tracking and len(s) > 1:
        w += tracking * (len(s) - 1)
    return w


def draw_tracked(draw, xy, s, f, fill, tracking):
    """Draw text with per-character letter-spacing (tracking)."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def draw_paragraph(draw, text, f, x, y, max_w, fill, leading):
    for ln in wrap(draw, text, f, max_w):
        draw.text((x, y), ln, font=f, fill=fill)
        y += leading
    return y


def section_label(draw, s, x, y, t):
    """Small uppercase tracked accent heading, like the site's h2."""
    f = font(t, "bold", 40)
    draw_tracked(draw, (x, y), s.upper(), f, t["accent"], 7)
    # underline accent rule
    w = text_w(draw, s.upper(), f, 7)
    draw.line([(x, y + 62), (x + w, y + 62)], fill=t["accent"], width=3)
    return y + 96


def fit(im, box_w, box_h):
    im = im.copy()
    im.thumbnail((box_w, box_h), Image.LANCZOS)
    return im


def build(theme_name):
    t = THEMES[theme_name]
    img = Image.new("RGB", (W, H), t["bg"])
    d = ImageDraw.Draw(img)

    # ---------- Header band ----------
    head_h = 470
    d.rectangle([0, 0, W, head_h], fill=t["hero_bg"])
    cx = W // 2
    f_kick = font(t, "bold", 38)
    kick = "ANCIENT EGYPT"
    d.line([(cx - 260, 92), (cx - 170, 92)], fill=t["hero_text"], width=2)
    d.line([(cx + 170, 92), (cx + 260, 92)], fill=t["hero_text"], width=2)
    kw = text_w(d, kick, f_kick, 11)
    draw_tracked(d, (cx - kw / 2, 74), kick, f_kick, t["hero_text"], 11)

    f_title = font(t, "bold", 200)
    title = "Canopic Jars"
    tw = d.textlength(title, font=f_title)
    d.text((cx - tw / 2, 140), title, font=f_title, fill=t["hero_text"])

    f_sub = font(t, "italic", 52)
    sub = "A school project by Amila Galvao"
    sw = d.textlength(sub, font=f_sub)
    d.text((cx - sw / 2, 372), sub, font=f_sub, fill=t["hero_text"])

    # ---------- Middle: three text columns ----------
    col_top = head_h + 70
    gap = 90
    col_w = (W - 2 * MARGIN - 2 * gap) // 3
    xcols = [MARGIN, MARGIN + col_w + gap, MARGIN + 2 * (col_w + gap)]

    f_body = font(t, "reg", 41)
    f_bold = font(t, "bold", 41)
    lead = 56

    # Col 1 — Introduction
    x = xcols[0]
    y = section_label(d, "Introduction", x, col_top, t)
    intro = ("Ancient Egyptian canopic jars were specialized vessels used during "
             "mummification to store the liver, lungs, stomach, and intestines. "
             "Guarded by the Four Sons of Horus, they evolved from simple stone "
             "blocks to beautifully carved works of art.")
    draw_paragraph(d, intro, f_body, x, y, col_w, t["text"], lead)

    # Col 2 — Four Sons of Horus (bold name + rest)
    x = xcols[1]
    y = section_label(d, "The Four Sons of Horus", x, col_top, t)
    sons = [
        ("Imsety", "human-headed god guarding the liver (South)."),
        ("Hapi", "baboon-headed god guarding the lungs (North)."),
        ("Duamutef", "jackal-headed god guarding the stomach (East)."),
        ("Qebehsenuef", "falcon-headed god guarding the intestines (West)."),
    ]
    for name, desc in sons:
        # bullet
        d.ellipse([x + 4, y + 18, x + 18, y + 32], fill=t["accent"])
        full = f"{name} — {desc}"
        lines = wrap(d, full, f_body, col_w - 44)
        # first line: draw name bold, then remainder regular
        first = lines[0]
        bx = x + 44
        # split first line into name part if present
        if first.startswith(name):
            d.text((bx, y), name, font=f_bold, fill=t["text"])
            rest = first[len(name):]
            d.text((bx + d.textlength(name, font=f_bold), y), rest, font=f_body, fill=t["text"])
        else:
            d.text((bx, y), first, font=f_body, fill=t["text"])
        y += lead
        for ln in lines[1:]:
            d.text((bx, y), ln, font=f_body, fill=t["text"])
            y += lead
        y += 18

    # Col 3 — Did You Know? (panel card)
    x = xcols[2]
    y = section_label(d, "Did You Know?", x, col_top, t)
    # panel
    pad = 36
    panel_top = y
    f_factb = font(t, "bold", 43)
    head_lines = wrap(d, "It Was Named After the Wrong Place", f_factb, col_w - 2 * pad)
    fact = ('The word "canopic" comes from an embarrassing mistake by early '
            "European experts. They noticed the jars looked similar to pots "
            "worshipped in a town in Egypt called Canopus. Even after realizing "
            "the mistake, the name stuck!")
    fact_lines = wrap(d, fact, f_body, col_w - 2 * pad)
    panel_h = pad * 2 + len(head_lines) * 54 + 24 + len(fact_lines) * lead
    d.rounded_rectangle([x, panel_top, x + col_w, panel_top + panel_h], radius=22,
                        fill=t["panel"], outline=t["border"], width=3)
    yy = panel_top + pad
    for ln in head_lines:
        d.text((x + pad, yy), ln, font=f_factb, fill=t["accent"])
        yy += 54
    yy += 24
    for ln in fact_lines:
        d.text((x + pad, yy), ln, font=f_body, fill=t["text"])
        yy += lead

    # ---------- Gallery row: 4 jar cards ----------
    foot_h = 120
    g_gap = 70
    card_w = (W - 2 * MARGIN - 3 * g_gap) // 4
    gallery_bottom = H - foot_h - 60
    card_h = 880
    gallery_top = gallery_bottom - card_h

    jars = [
        ("jar-1-red-black.png", "Imsety", "Human-headed god guarding the liver (South)."),
        ("jar-3-white-collar.png", "Hapi", "Baboon-headed god guarding the lungs (North)."),
        ("jar-2-striped.png", "Duamutef", "Jackal-headed god guarding the stomach (East)."),
        ("jar-4-gold.png", "Qebehsenuef", "Falcon-headed god guarding the intestines (West)."),
    ]
    f_cap_b = font(t, "bold", 38)
    f_cap = font(t, "reg", 38)
    cap_pad = 30
    cap_lead = 48
    cap_area_h = 230
    img_area_h = card_h - cap_area_h
    for i, (fn, name, desc) in enumerate(jars):
        x0 = MARGIN + i * (card_w + g_gap)
        d.rounded_rectangle([x0, gallery_top, x0 + card_w, gallery_top + card_h],
                            radius=22, fill=t["panel"], outline=t["border"], width=3)
        jp = os.path.join(IMG, fn)
        ph = fit(Image.open(jp).convert("RGBA"), card_w - 80, img_area_h - 50)
        ix = x0 + (card_w - ph.width) // 2
        iy = gallery_top + 36 + (img_area_h - 50 - ph.height) // 2
        img.paste(ph, (ix, iy), ph)
        # caption: bold "Name:" then wrapped description, matching the website
        cx0 = x0 + cap_pad
        cyc = gallery_top + img_area_h + 6
        full = f"{name}: {desc}"
        lines = wrap(d, full, f_cap, card_w - 2 * cap_pad)
        label = f"{name}:"
        first = lines[0]
        if first.startswith(label):
            d.text((cx0, cyc), label, font=f_cap_b, fill=t["text"])
            rest = first[len(label):]
            d.text((cx0 + d.textlength(label, font=f_cap_b), cyc), rest,
                   font=f_cap, fill=t["muted"])
        else:
            d.text((cx0, cyc), first, font=f_cap, fill=t["muted"])
        cyc += cap_lead
        for ln in lines[1:]:
            d.text((cx0, cyc), ln, font=f_cap, fill=t["muted"])
            cyc += cap_lead

    # ---------- Footer ----------
    d.rectangle([0, H - foot_h, W, H], fill=t["hero_bg"])
    f_ft = font(t, "reg", 38)
    ft = "A school project by Amila Galvao  ·  2026"
    fw = d.textlength(ft, font=f_ft)
    d.text((cx - fw / 2, H - foot_h + (foot_h - 48) / 2), ft, font=f_ft, fill=t["hero_text"])

    return img


def main():
    # Final poster theme (set to "dark-gold" to switch back to that look).
    name = "papyrus"
    im = build(name)
    pdf = os.path.join(HERE, "canopic-jars-poster.pdf")
    im.save(pdf, "PDF", resolution=float(DPI))
    prev = im.copy()
    prev.thumbnail((1700, 1700), Image.LANCZOS)
    prev.save(os.path.join(HERE, "_preview.png"))
    print("wrote", pdf, im.size)


if __name__ == "__main__":
    main()
