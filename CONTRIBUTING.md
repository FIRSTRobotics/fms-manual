# Contributing to the FMS Manual

Thank you for helping improve the FMS Manual! This guide is written for the
people who know the Field Management System best: **FRC Field Technical
Advisors (FTAs), FTA Assistants (FTAAs), and Scorekeepers.** You do not need to
be a software developer to contribute — most useful changes are corrections,
clarifications, and updated screenshots.

This repository contains the source articles for the official
[FMS Manual](https://fms-manual.readthedocs.io/). The site is built from
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
(`.rst`) files using [Sphinx](https://www.sphinx-doc.org/) and published on
[Read the Docs](https://readthedocs.org/).

---

## Before you start

- **The Game Manual always wins.** If anything in this manual conflicts with the
  official FRC Game Manual, the Game Manual is the authoritative source. Please
  do not document anything that contradicts it.
- **Write from real field experience.** Document FMS as it actually behaves at
  events. If you're unsure whether a behavior is intended, note it in your pull
  request so a reviewer can confirm.
- **Follow the style guide.** This project uses the same style guide as
  [frc-docs](https://docs.wpilib.org/en/latest/docs/contributing/frc-docs/style-guide.html).
  When in doubt, match the tone and formatting of the article you're editing.
- **No private or sensitive information.** Do not include real team data,
  passwords, internal FIRST URLs, or anything that isn't appropriate for a
  public document.

---

## The easy way: edit in your web browser

For a quick fix — a typo, a wrong button name, an outdated step — you don't need
to install anything. You only need a free [GitHub](https://github.com) account.

1. Go to the article on the live site, scroll to the bottom, and click
   **"Edit on GitHub"** (or browse to the matching `.rst` file in the
   [`source/`](source/) folder on GitHub).
2. Click the **pencil ✏️ icon** to edit the file.
3. Make your change. The text is mostly plain English; see
   [Writing reStructuredText](#writing-restructuredtext) below for the few
   formatting rules you'll run into.
4. At the bottom, choose **"Create a new branch for this commit and start a pull
   request"**, then click **Propose changes**.
5. Fill in a short description of *what* you changed and *why*, then click
   **Create pull request**.

That's it. A Scorekeeper maintainer will review it. The build system will
automatically check your change (see [What happens after you submit](#what-happens-after-you-submit)).

> **Adding or replacing a screenshot in the browser?** You can drag-and-drop an
> image directly into a folder on GitHub, but it's easier to get image paths
> right when building locally. See [Working with screenshots](#working-with-screenshots).

---

## The recommended local setup: Docker

If you're making a larger change, adding pages, or just want to *see* your edits
as you make them, the easiest way to build the manual on your own computer is
with [Docker](https://www.docker.com/products/docker-desktop/). You don't need
to install Python or LaTeX — Docker handles everything.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and
   make sure it's running.
2. Clone this repository and open a terminal in the folder:
   ```bash
   git clone https://github.com/FIRSTRobotics/fms-manual.git
   cd fms-manual
   ```
3. Start the live preview:
   ```bash
   docker compose up docs
   ```
4. Open **http://localhost:8000** in your browser.

Now edit any `.rst` file under `source/` and save — the manual **rebuilds
automatically and your browser refreshes** so you can see the result instantly.
Press `Ctrl+C` in the terminal to stop.

Other useful commands:

| Command | What it does |
| ------- | ------------ |
| `docker compose up docs` | Live HTML preview at http://localhost:8000 |
| `docker compose run --rm linkcheck` | Run the same broken-link check CI runs |
| `docker compose --profile pdf run --rm pdf` | Build the PDF into `build/latex/` (downloads a large TeX Live image the first time) |

> The first `docker compose up` builds the image and takes a few minutes. After
> that it starts in seconds.

---

## The manual way: build without Docker

Use this if you'd rather not use Docker and want to install the tools directly.

### 1. Install the prerequisites

- **Python 3.12** (3.6+ will work, but CI uses 3.12)
- **Git** ([download](https://git-scm.com/downloads))
- **LaTeX** — only needed if you want to build the PDF. On Windows use
  [MiKTeX](https://miktex.org/); on macOS use [MacTeX](https://www.tug.org/mactex/);
  on Linux install `texlive`. You can skip this if you only build the HTML site.

### 2. Get the code

```bash
git clone https://github.com/FIRSTRobotics/fms-manual.git
cd fms-manual
```

### 3. Install the Python dependencies

```bash
pip install -r source/requirements.txt
```

### 4. Build the HTML site

```bash
make html        # macOS / Linux
make.bat html    # Windows
```

The generated site lands in `build/html/`. Open `build/html/index.html` in your
browser to preview your changes.

To build the PDF (requires LaTeX): `make latexpdf`.

> **Tip:** The build is run with warnings treated as errors (`-W`), exactly like
> the automated checks. If `make html` fails, the error message tells you the
> file and line to fix — usually a broken reference, a bad link, or a misaligned
> table.

### 5. Submit your change

```bash
git checkout -b my-correction
git add .
git commit -m "Fix battery voltage description in Field Monitor"
git push origin my-correction
```

Then open a pull request on GitHub against the `master` branch.

---

## How the manual is organized

Articles live under [`source/`](source/), grouped by FMS component. A few you'll
recognize:

| Folder | Covers |
| ------ | ------ |
| `event-manager/` | Event Manager (the main FMS application) |
| `field-monitor/`, `field-monitor-v3/` | Field Monitor live view and status indicators |
| `field-server-web/` | The 10.0.100.5 field server website |
| `pit-display/`, `audience-display/` | Pit and Audience displays |
| `fta-notepad/` | FTA Notepad |
| `scorekeeper-reference/` | Scorekeeper reference material |
| `wpa-kiosk/`, `event-manager/` | WPA Kiosk and related tooling |

[`source/index.rst`](source/index.rst) is the table of contents (the
`toctree`). **If you add a brand-new page, you must add it to the appropriate
`toctree`** — either in `index.rst` or in the local `index.rst` for that section
— or the build will warn that your page isn't included.

---

## Writing reStructuredText

reStructuredText is mostly plain text. The handful of rules you'll actually use:

**Headings** — underline the text with punctuation. The underline must be at
least as long as the text:

```rst
Page Title
==========

A Section
---------
```

**Images** — place the file in an `images/` folder next to the `.rst`, then:

```rst
.. image:: images/field-monitor-1.png
```

**Cross-references** — link to another page using its label:

```rst
:ref:`Status Indicators <field-monitor-status-indicators>`
```

**Tables** — use simple tables; keep the `=====` rules aligned with the columns:

```rst
======  ===========
Label   Description
======  ===========
DS      Driver Station connectivity.
======  ===========
```

When in doubt, copy the formatting from an existing article in the same folder.

---

## Working with screenshots

- Save screenshots in the **`images/` folder next to the article** that uses
  them (e.g. `source/field-monitor/live/images/`).
- Use descriptive, lowercase, hyphenated names: `prestart-complete.png`.
- **PNG** is preferred for FMS screenshots.
- Crop to the relevant area and blur or avoid any real team identifying
  information where it isn't needed.
- When you replace an existing screenshot because the UI changed, keep the same
  filename if possible so you don't have to update every reference.

The original editable assets (Photoshop files) live in
[`photoshop-files/`](photoshop-files/).

---

## What happens after you submit

Every pull request automatically runs three checks (you'll see them on the PR):

1. **Build HTML** — confirms the site builds with no warnings.
2. **Build PDF** — confirms the LaTeX/PDF version builds.
3. **Check Links** — confirms no links are broken.

If a check fails, click **"Details"** next to it to see why, then push another
commit to your branch to fix it. A Scorekeeper maintainer will review the
content and merge it once the checks pass. Once merged, Read the Docs rebuilds
and publishes the live site automatically.

---

## Questions

This project is managed by the **FRC Global Scorekeepers**. For questions about
contributing, open an [issue](https://github.com/FIRSTRobotics/fms-manual/issues)
on GitHub or ask in your usual Scorekeeper communication channels. For questions
about FMS itself or this content, contact FIRST HQ.

Thank you for contributing! 🤖
