# # Use Debian as base
# FROM debian:latest

# # Install Java, wget, and procps (for ps command)
# RUN apt-get update && apt-get install -y wget openjdk-17-jdk-headless procps

# # Set Java environment variables for PySpark
# ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
# ENV PATH="$JAVA_HOME/bin:$PATH"

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
#     bash miniconda.sh -b -p /opt/conda && \
#     rm miniconda.sh

# # Set up Conda environment with Python 3.11
# ENV PATH="/opt/conda/bin:$PATH"
# RUN conda create -n myenv python=3.11 -y

# # Activate Conda environment
# RUN /opt/conda/bin/conda init bash

# # Set working directory
# WORKDIR /app

# # Copy requirements file
# COPY requirements.txt /app/requirements.txt

# # Install dependencies inside Conda
# RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 -r /app/requirements.txt

# # Install PySpark explicitly inside Conda
# RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 pyspark==3.5.5

# # Copy application code
# COPY code /app/code

# # Set working directory
# WORKDIR /app/code

# # Set Java in PySpark explicitly
# ENV PYSPARK_SUBMIT_ARGS="--conf spark.driver.extraJavaOptions=-Djava.library.path=$JAVA_HOME"

# # Activate Conda environment and run script
# CMD ["/bin/bash", "-c", "source /opt/conda/bin/activate myenv && bash /app/code/script/run.sh"]

# # Use Debian as base
# FROM debian:latest

# # Install Java, wget, and procps (for ps command)
# RUN apt-get update && apt-get install -y wget openjdk-11-jdk-headless procps

# # Set Java environment variables for PySpark
# ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
# ENV PATH="$JAVA_HOME/bin:$PATH"

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
#     bash miniconda.sh -b -p /opt/conda && \
#     rm miniconda.sh

# # Set up Conda environment with Python 3.11
# ENV PATH="/opt/conda/bin:$PATH"
# RUN conda create -n myenv python=3.11 -y

# # Activate Conda environment
# RUN /opt/conda/bin/conda init bash

# # Set working directory
# WORKDIR /app

# # Copy requirements file
# COPY requirements.txt /app/requirements.txt

# # Install dependencies inside Conda
# RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 -r /app/requirements.txt

# # Install PySpark explicitly inside Conda
# RUN /opt/conda/bin/conda run -n myenv pip install --default-timeout=1000 pyspark==3.5.5

# # Copy application code
# COPY code /app/code

# # Set working directory
# WORKDIR /app/code

# # Set Java in PySpark explicitly
# ENV PYSPARK_SUBMIT_ARGS="--conf spark.driver.extraJavaOptions=-Djava.library.path=$JAVA_HOME"

# # Activate Conda environment and run script
# # Use `conda run` to ensure the environment is activated and the script is executed properly
# CMD ["/opt/conda/bin/conda", "run", "-n", "myenv", "bash", "/app/code/script/run.sh"]

# Use Debian as the base image
# Use Debian as the base image
# Use Debian as the base image
FROM debian:bullseye-slim

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
    openjdk-17-jdk \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    python3-pip \
    python3-venv

# Set JAVA_HOME and PATH for Java 17
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Spark dependencies
RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
    mv spark-3.5.5-bin-hadoop3 /opt/spark

# Set SPARK_HOME and PYSPARK_PYTHON
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON=python3.11

# Create and activate a virtual environment
RUN python3.11 -m venv /uzb

# Install Python dependencies inside the virtual environment
RUN /uzb/bin/pip install pyspark

# Set working directory
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/UdithWeerasinghe/UZABASE_AI.git

# Set the working directory inside the cloned repository
WORKDIR /app/UZABASE_AI

# Install any Python dependencies specified in requirements.txt
RUN /uzb/bin/pip install --break-system-packages -r requirements.txt

# Expose ports (if needed, adjust as per your project needs)
EXPOSE 8080

# Define entrypoint for running the application
ENTRYPOINT ["/uzb/bin/python", "code/src/run.py"]
CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]





