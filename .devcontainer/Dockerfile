FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install pixi system-wide (/usr/local/bin) so the vscode user can run it
ENV PIXI_HOME=/usr/local
RUN curl -fsSL https://pixi.sh/install.sh | bash \
    && echo 'eval "$(pixi completion --shell bash)"' >> /etc/bash.bashrc \
    && echo 'eval "$(pixi completion --shell zsh)"'  >> /etc/zsh/zshrc \
    && chsh -s /usr/bin/zsh vscode
