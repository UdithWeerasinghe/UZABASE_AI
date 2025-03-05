# Use Debian as base
FROM debian:latest

# Install Java, wget, and procps (for ps command)
RUN apt-get update && apt-get install -y wget openjdk-17-jdk-headless procps

# Set Java environment variables for PySpark
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

# Set up Conda environment with Python 3.11
ENV PATH="/opt/conda/bin:$PATH"
RUN conda create -n myenv python=3.11 -y

# Activate Conda environment
RUN /opt/conda/bin/conda init bash

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies inside Conda
RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 -r /app/requirements.txt

# Install PySpark explicitly inside Conda
RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 pyspark==3.5.5

# Copy application code
COPY code /app/code

# Set working directory
WORKDIR /app/code

# Set Java in PySpark explicitly
ENV PYSPARK_SUBMIT_ARGS="--conf spark.driver.extraJavaOptions=-Djava.library.path=$JAVA_HOME"

# Activate Conda environment and run script
CMD ["/bin/bash", "-c", "source /opt/conda/bin/activate myenv && bash /app/code/script/run.sh"]







