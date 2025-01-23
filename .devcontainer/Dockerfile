FROM python:3.11-bookworm

ENV USER_GID=1000
ENV USER_UID=1000
ENV DOCKER_GID=965
ENV USERNAME=worker
ENV HOME=/home/${USERNAME}

# Setup container user, groups and home
RUN groupadd -g ${USER_GID} ${USERNAME} && \
    useradd -m -u ${USER_UID} -g ${USER_GID} ${USERNAME} && \
    mkdir /workspace && \
    chown ${USERNAME}:${USERNAME} /workspace

# Install advanced python dependencies
RUN apt-get update && apt-get install -y \
    build-essential libssl-dev libffi-dev python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install opencv display dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx libx11-dev libwayland-client0 x11-utils qtwayland5

# Install ADB
RUN groupadd -r adbusers && usermod -aG adbusers ${USERNAME}
RUN apt-get update && apt-get install -y \
    adb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# <- DEVCONTAINER ->
# Enable sudo permissions for container user
RUN apt-get update && apt-get install -y sudo&& \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# Make sure locals are set
RUN apt-get update && apt-get install -y locales locales-all \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
# Install zsh and other useful packages
RUN apt-get update && apt-get install -y \
    git wget curl unzip rsync zsh htop vim neofetch \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
# Install Docker
RUN groupadd -g ${DOCKER_GID} docker
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
# Set up the environment for the container user
RUN chsh -s /bin/zsh ${USERNAME} && \
    usermod -aG docker ${USERNAME} && \
    mkdir /workspace/dev && chown ${USERNAME}:${USERNAME} /workspace/dev
# Switch to container user and set home directory
USER ${USERNAME}
# Install oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" "" --unattended
# Enable command completion and git support in zsh
RUN git clone https://github.com/zsh-users/zsh-completions ${HOME}/.oh-my-zsh/custom/plugins/zsh-completions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${HOME}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${HOME}/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN sed -i 's/plugins=(git)/plugins=(git zsh-completions zsh-syntax-highlighting zsh-autosuggestions)/' ${HOME}/.zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' ${HOME}/.zshrc
RUN echo 'prompt_context() {}' >> ${HOME}/.zshrc
# Command alias
RUN echo 'alias ll="ls -lah --color=auto"' >> ${HOME}/.zshrc
RUN echo 'alias cp="rsync -avh --progress"' >> ${HOME}/.zshrc
# Switch back to root user
USER root
# <- DEVCONTAINER ->

# Install poetry
RUN pip install poetry
ENV PATH="${HOME}/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_VIRTUALENVS_OPTIONS_ALWAYS_COPY=true

# Entrypoint
USER ${USERNAME}
WORKDIR /workspace/dev
CMD ["/bin/zsh"]
