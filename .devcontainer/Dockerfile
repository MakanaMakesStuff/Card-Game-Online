# ---- Base: Dev Container with Python ----
# Note: If 3.14 fails to pull, downgrade to 3.12 (the current stable devcontainer tag)
FROM mcr.microsoft.com/devcontainers/python:3.14

# ---- Install Node.js 22 + common build deps ----
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get update && \
    apt-get install -y \
        nodejs \
        build-essential \
        git \
        curl \
        sqlite3 \
        jq \
        libssl-dev \
        openssh-client \
        ca-certificates \
        apt-transport-https \
        gnupg \
        lsb-release && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y \
        docker-ce-cli \
        docker-buildx-plugin && \
    rm -rf /var/lib/apt/lists/*

# ---- Add vscode user to docker group ----
RUN groupadd -f docker && usermod -aG docker vscode

# ---- Switch to vscode user for remaining setup ----
USER vscode

# ---- Install Poetry (Python package manager) ----
ENV POETRY_HOME="/home/vscode/.local/share/pypoetry"
ENV PATH="$POETRY_HOME/bin:/home/vscode/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

# (Optional) Tell Poetry not to create virtualenvs, since Docker 
# containers already isolate your environment.
RUN poetry config virtualenvs.create false

# ---- Install Starship prompt ----
RUN mkdir -p /home/vscode/.local/bin && \
    curl -sS https://starship.rs/install.sh | sh -s -- -b /home/vscode/.local/bin -y && \
    echo 'eval "$(starship init bash)"' >> /home/vscode/.bashrc
    
# ---- Load Bash Aliases ----
RUN echo "if [ -f /workspace/.devcontainer/.bash_aliases ]; then . /workspace/.devcontainer/.bash_aliases; fi" >> /home/vscode/.bashrc

# ---- Set workspace folder ----
WORKDIR /workspace

# ---- Default shell ----
CMD ["bash"]