# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install required Python packages
RUN python -m venv /py
RUN apt update -y && apt install awscli -y
RUN /py/bin/pip install --upgrade pip
RUN python -m pip install --upgrade pip
ENV PATH="/py/bin:$PATH"
RUN pip install -r requirements.txt --default-timeout=100 future

# Copy the rest of the application files to the container's working directory
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501
EXPOSE 8000
EXPOSE 8080
EXPOSE 5432

# Command to run your Streamlit application
CMD ["streamlit", "run", "app.py"]