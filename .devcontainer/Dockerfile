FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install pixi and uv system-wide (/usr/local/bin) so the vscode user can run them
ENV PIXI_HOME=/usr/local
ENV UV_INSTALL_DIR=/usr/local/bin
RUN curl -fsSL https://pixi.sh/install.sh | bash \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && echo 'eval "$(pixi completion --shell bash)"' >> /etc/bash.bashrc \
    && echo 'eval "$(pixi completion --shell zsh)"'  >> /etc/zsh/zshrc \
    && echo 'eval "$(uv generate-shell-completion bash)"' >> /etc/bash.bashrc \
    && echo 'eval "$(uv generate-shell-completion zsh)"'  >> /etc/zsh/zshrc \
    && chsh -s /usr/bin/zsh vscode
