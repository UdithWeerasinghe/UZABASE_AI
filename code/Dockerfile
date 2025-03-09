FROM debian:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install required dependencies
RUN apt update && apt upgrade -y && \
    apt install -y \
    wget \
    curl \
    unzip \
    tar \
    git \
    build-essential \
    software-properties-common \
    openjdk-17-jdk

# Set JAVA_HOME and update PATH for Java 17
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/miniconda && \
    rm /tmp/miniconda.sh

# Set Conda environment variables
ENV PATH="/opt/miniconda/bin:$PATH"
RUN conda init bash

# Create Conda environment and install Python
RUN conda create -n uzb_env python=3.11 -y

# Activate Conda environment for the rest of the setup
SHELL ["/bin/bash", "-c"]

# Install PySpark in the Conda environment
RUN source activate uzb_env && pip install pyspark

# Install Spark
RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
    mv spark-3.5.5-bin-hadoop3 /opt/spark

# Set Spark environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON="/opt/miniconda/envs/uzb_env/bin/python"

# Set working directory
WORKDIR /app

# Copy application files into the container
COPY . .

# Install project dependencies inside the Conda environment
RUN source activate uzb_env && pip install --break-system-packages -r requirements.txt

# Define entrypoint for running the application
ENTRYPOINT ["/bin/bash", "-c", "source activate uzb_env && python code/src/run.py"]
CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]

