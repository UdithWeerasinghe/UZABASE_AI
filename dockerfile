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
COPY . .


# Install any Python dependencies specified in requirements.txt
RUN /uzb/bin/pip install --break-system-packages -r requirements.txt


# Define entrypoint for running the application
ENTRYPOINT ["/uzb/bin/python", "code/src/run.py"]
CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]
