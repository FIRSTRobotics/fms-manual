# Local development image for the FMS Manual.
#
# Builds the HTML site and serves it with live reload, so editing any .rst file
# automatically rebuilds the manual and refreshes your browser. See the
# "Local development with Docker" section of CONTRIBUTING.md for usage.

FROM python:3.12-slim

# git: used by the build; make: lets you run `make linkcheck`, `make html`, etc.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /docs

# Install Python dependencies first so this layer stays cached unless the
# requirements file changes. sphinx-autobuild provides the live-reload server
# and is only needed for local development (not in requirements.txt / CI).
COPY source/requirements.txt source/requirements.txt
RUN pip install --no-cache-dir -r source/requirements.txt sphinx-autobuild

EXPOSE 8000

# Watch source/ and live-rebuild to build/html, served on port 8000.
# Note: unlike `make html`, this does not use -W (warnings-as-errors), so a
# stray warning won't stop your live preview while you're editing.
CMD ["sphinx-autobuild", "source", "build/html", "--host", "0.0.0.0", "--port", "8000"]
