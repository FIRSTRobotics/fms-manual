![CI](https://github.com/FIRSTRobotics/fms-manual/workflows/CI/badge.svg)
![docs](https://readthedocs.org/projects/fms-manual/badge/?version=latest)

# fms-manual

Welcome to fms-manual! This repository contains the underlying articles for the official User Manual and guide for
Scorekeepers working FIRST Robotics Competition events. This project is licensed under Creative Commons, with assets
such as the FIRST logo under trademark and copyright of [FIRST](https://www.firstinspires.org/). This project is managed
by the FRC Global Scorekeepers. For questions or comments, please contact FIRST HQ.

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

The website is available under the following domains:

- https://fms-manual.readthedocs.io/
- https://fms-manual.rtfd.io/
- https://bit.ly/fmsmanual

## Building

The quickest way to build and preview the manual locally is with
[Docker](https://www.docker.com/products/docker-desktop/) — no need to install
Python or LaTeX:

```bash
docker compose up docs
```

Then open http://localhost:8000. Editing any file under ``source/`` rebuilds the
site and refreshes your browser automatically. See
[CONTRIBUTING.md](CONTRIBUTING.md) for more, including the link check and PDF builds.

To build without Docker, install:

- Python 3.12
- LaTeX, only if building the PDF (see MiKTeX for Windows)
- Python dependencies in ``source/requirements.txt``

Then build by running ``make html``.

## Styleguide

Styleguide is duplicate of [frc-docs](https://docs.wpilib.org/en/latest/docs/contributing/frc-docs/style-guide.html)

In case of conflict with the official FRC Game Manual- the Game Manual is the official source.
