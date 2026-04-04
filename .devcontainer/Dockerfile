FROM mcr.microsoft.com/devcontainers/base:bookworm

# 1. Install PostgreSQL AND git-lfs
# We use noninteractive to avoid prompts during build
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql postgresql-contrib git-lfs asciinema 

# 2. SUDO : Ensure the 'vscode' user can use sudo without a password
# This prevents the "[sudo] password for vscode" error during startup
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# 3. AUTH : Configure Postgres to allow local connections ('trust' mode)
# This uses a wildcard (*) so it works for version 15, 16, etc. automatically.
# It replaces 'peer' (system user) auth with 'trust' (no password for local)
# or 'md5' (password allowed).
RUN sed -i 's/local\s*all\s*postgres\s*peer/local all postgres trust/g' /etc/postgresql/*/main/pg_hba.conf \
    && sed -i 's/local\s*all\s*all\s*peer/local all all trust/g' /etc/postgresql/*/main/pg_hba.conf \
    && sed -i 's/host\s*all\s*all\s*127.0.0.1\/32\s*scram-sha-256/host all all 127.0.0.1\/32 trust/g' /etc/postgresql/*/main/pg_hba.conf


RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        postgresql postgresql-contrib \
        git-lfs asciinema \
        python3 python3.11-venv python3-pip \
        python3-tk \
        xvfb x11vnc xterm

