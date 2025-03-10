# FROM debian:latest

# # Set environment variables to avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Update package list and install required dependencies
# RUN apt update && apt upgrade -y && \
#     apt install -y \
#     wget \
#     curl \
#     unzip \
#     tar \
#     git \
#     build-essential \
#     software-properties-common \
#     openjdk-17-jdk

# # Set JAVA_HOME and update PATH for Java 17
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV PATH=$JAVA_HOME/bin:$PATH

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
#     bash /tmp/miniconda.sh -b -p /opt/miniconda && \
#     rm /tmp/miniconda.sh

# # Set Conda environment variables
# ENV PATH="/opt/miniconda/bin:$PATH"

# # Create Conda environment and install Python
# RUN conda create -n uzb_env python=3.11 -y

# # Install PySpark in the Conda environment
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install pyspark

# # Install Spark
# RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
#     tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
#     mv spark-3.5.5-bin-hadoop3 /opt/spark && \
#     rm spark-3.5.5-bin-hadoop3.tgz

# # Set Spark environment variables
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$SPARK_HOME/bin:$PATH
# ENV PYSPARK_PYTHON="/opt/miniconda/envs/uzb_env/bin/python"

# # Set working directory
# WORKDIR /app

# # Copy application files into the container
# COPY . .

# # Install project dependencies inside the Conda environment
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install --break-system-packages -r requirements.txt

# # Define entrypoint for running the application
# ENTRYPOINT ["/bin/bash", "-c", "/opt/miniconda/bin/conda run -n uzb_env python code/src/run.py"]
# CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]

# # Use Debian as base
# FROM debian:latest

# # Set environment variables to avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Update package list and install required dependencies
# RUN apt update && apt upgrade -y && \
#     apt install -y \
#     wget \
#     curl \
#     unzip \
#     tar \
#     git \
#     build-essential \
#     software-properties-common \
#     openjdk-17-jdk

# # Set JAVA_HOME and update PATH for Java 17
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV PATH=$JAVA_HOME/bin:$PATH

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
#     bash /tmp/miniconda.sh -b -p /opt/miniconda && \
#     rm /tmp/miniconda.sh

# # Set Conda environment variables
# ENV PATH="/opt/miniconda/bin:$PATH"

# # Create Conda environment and install Python
# RUN /opt/miniconda/bin/conda create -n uzb_env python=3.11 -y

# # Set Conda shell as default for next steps
# SHELL ["/opt/miniconda/bin/conda", "run", "-n", "uzb_env", "/bin/bash", "-c"]

# # Install PySpark and dependencies inside the Conda environment
# RUN pip install -r requirements.txt

# # Install Apache Spark
# RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
#     tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
#     mv spark-3.5.5-bin-hadoop3 /opt/spark && \
#     rm spark-3.5.5-bin-hadoop3.tgz

# # Set Spark environment variables
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$SPARK_HOME/bin:$PATH
# ENV PYSPARK_PYTHON="/opt/miniconda/envs/uzb_env/bin/python"

# # Set working directory
# WORKDIR /app

# # Copy application files into the container
# COPY . .

# # Run the application with the correct Conda environment activated
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/miniconda/bin/activate uzb_env && python code/src/run.py process_data --cfg code/config/cfg.yaml --dirout ztmp/data/"]

# FROM debian:latest

# # Set environment variables to avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Update package list and install required dependencies
# RUN apt update && apt upgrade -y && \
#     apt install -y \
#     wget \
#     curl \
#     unzip \
#     tar \
#     git \
#     build-essential \
#     software-properties-common \
#     openjdk-17-jdk \
#     bash

# # Set JAVA_HOME and update PATH for Java 17
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV PATH=$JAVA_HOME/bin:$PATH

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
#     bash /tmp/miniconda.sh -b -p /opt/miniconda && \
#     rm /tmp/miniconda.sh

# # Set Conda environment variables
# ENV PATH="/opt/miniconda/bin:$PATH"
# RUN conda init bash

# # Create Conda environment and install Python
# RUN conda create -n uzb_env python=3.11 -y

# # Set the shell to bash for correct Conda activation
# SHELL ["/bin/bash", "-c"]

# # Activate Conda environment and install PySpark
# RUN source /opt/miniconda/bin/activate uzb_env && pip install pyspark

# # Install Spark
# RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
#     tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
#     mv spark-3.5.5-bin-hadoop3 /opt/spark

# # Set Spark environment variables
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$SPARK_HOME/bin:$PATH
# ENV PYSPARK_PYTHON=/opt/miniconda/envs/uzb_env/bin/python

# # Set working directory
# WORKDIR /app

# # Copy application files into the container
# COPY . .

# # Install project dependencies inside the Conda environment
# RUN source /opt/miniconda/bin/activate uzb_env && pip install -r requirements.txt

# # Define entrypoint for running the application
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/miniconda/bin/activate uzb_env && exec python code/src/run.py"]
# CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]

# # Use Debian as the base image
# FROM debian:latest

# # Set environment variables to avoid interactive prompts during package installation
# ENV PATH="/opt/miniconda/bin:$PATH"

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
#     bash miniconda.sh -b -p /opt/miniconda && \
#     rm miniconda.sh

# # Initialize Conda
# RUN conda init bash

# # Create a Conda environment and install Python
# RUN conda create -n uzb_env python=3.11 -y

# # Set shell to use bash for Conda activation
# SHELL ["/bin/bash", "-c"]

# # Install PySpark in the Conda environment
# RUN source activate uzb_env && pip install pyspark
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install pyspark

# # Install Apache Spark
# RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
#     tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
#     mv spark-3.5.5-bin-hadoop3 /opt/spark && \
#     rm spark-3.5.5-bin-hadoop3.tgz

# # Set Spark environment variables
# ENV SPARK_HOME=/opt/spark

# # Set the working directory
# WORKDIR /app

# # Copy all project files into the container
# COPY . .

# # Install project dependencies inside the Conda environment
# RUN source activate uzb_env && pip install --break-system-packages -r requirements.txt
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install --break-system-packages -r requirements.txt

# # Define entrypoint for running the application
# ENTRYPOINT ["/bin/bash", "-c", "/opt/miniconda/bin/conda run -n uzb_env python code/src/run.py"]

# # Default command to execute when the container runs
# CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]

# FROM debian:latest

# # Set environment variables to avoid interactive prompts during package installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Update package list and install required dependencies
# RUN apt update && apt upgrade -y && \
#     apt install -y \
#     wget \
#     curl \
#     unzip \
#     tar \
#     git \
#     build-essential \
#     software-properties-common \
#     openjdk-17-jdk

# # Set JAVA_HOME and update PATH for Java 17
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV PATH=$JAVA_HOME/bin:$PATH

# # Install Miniconda
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
#     bash /tmp/miniconda.sh -b -p /opt/miniconda && \
#     rm /tmp/miniconda.sh

# # Set Conda environment variables
# ENV PATH="/opt/miniconda/bin:$PATH"

# # Create Conda environment and install Python
# RUN conda create -n uzb_env python=3.11 -y

# # Install PySpark in the Conda environment
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install pyspark

# # Install Spark
# RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
#     tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
#     mv spark-3.5.5-bin-hadoop3 /opt/spark && \
#     rm spark-3.5.5-bin-hadoop3.tgz

# # Set Spark environment variables
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$SPARK_HOME/bin:$PATH
# ENV PYSPARK_PYTHON="/opt/miniconda/envs/uzb_env/bin/python"

# # Set working directory
# WORKDIR /app

# # Copy application files into the container
# COPY . .

# # Install project dependencies inside the Conda environment
# RUN /opt/miniconda/bin/conda run -n uzb_env pip install --break-system-packages -r requirements.txt

# # Define entrypoint for running the application
# ENTRYPOINT ["/bin/bash", "-c", "/opt/miniconda/bin/conda run -n uzb_env python code/src/run.py"]
# CMD ["process_data", "--cfg", "code/config/cfg.yaml", "--dirout", "ztmp/data/"]


FROM debian:latest

# Set non-interactive mode for installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt update && apt upgrade -y && \
    apt install -y wget curl unzip tar git build-essential software-properties-common openjdk-17-jdk

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/miniconda && \
    rm miniconda.sh

# Set Conda environment variables
ENV PATH="/opt/miniconda/bin:$PATH"
SHELL ["/bin/bash", "-c"]  # Ensure all following commands use Bash

# Create Conda environment and install dependencies
RUN conda create -n uzb_env python=3.11 -y

# Install PySpark inside Conda environment
RUN conda run -n uzb_env pip install pyspark

# Download and set up Apache Spark
RUN wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.5-bin-hadoop3.tgz && \
    mv spark-3.5.5-bin-hadoop3 /opt/spark && \
    rm spark-3.5.5-bin-hadoop3.tgz

# Set Spark environment variables
ENV SPARK_HOME=/opt/spark
ENV PYSPARK_PYTHON=/opt/miniconda/envs/uzb_env/bin/python
ENV PATH="$SPARK_HOME/bin:$PATH"

# Clone the repository and install dependencies
RUN git clone https://github.com/UdithWeerasinghe/UZABASE_AI.git /app
WORKDIR /app
RUN /opt/conda/envs/uzb_env/bin/python -m pip install --break-system-packages -r requirements.txt


# Set the entrypoint to use Conda environment when running the application
#ENTRYPOINT ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c", "conda run -n uzb_env python code/src/run.py"]
CMD ["conda run -n uzb_env python code/src/run.py process_data -cfg code/config/cfg.yaml -dataset news -dirout 'ztmp/data/'"]
