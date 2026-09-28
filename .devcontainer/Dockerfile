FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install pixi system-wide (/usr/local/bin) so the vscode user can run it
ENV PIXI_HOME=/usr/local
RUN curl -fsSL https://pixi.sh/install.sh | bash \
    && echo 'eval "$(pixi completion --shell bash)"' >> /etc/bash.bashrc \
    && echo 'eval "$(pixi completion --shell zsh)"'  >> /etc/zsh/zshrc \
    && chsh -s /usr/bin/zsh vscode

# Install uv and uvx system-wide from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/
RUN echo 'eval "$(uv generate-shell-completion bash)"' >> /etc/bash.bashrc \
    && echo 'eval "$(uv generate-shell-completion zsh)"'  >> /etc/zsh/zshrc
