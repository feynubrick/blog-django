FROM debian:buster-slim

# for setting locale to en_US.UTF-8
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# install packages needed for building python
RUN apt-get update \
    && apt-get install -y wget build-essential libreadline-gplv2-dev libncursesw5-dev \
     libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

# install Python 3.9.2
RUN wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
RUN tar xzf Python-3.9.2.tgz
RUN cd Python-3.9.2 && ./configure --enable-optimizations && make install

# install Python packages
RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
RUN cd /app && python3 -m pip install -r requirements.txt

# Copy project
COPY . /app
WORKDIR /app
# Entry command
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]