# Log Management System

## System Architecture

The Log Management System consists of three main components: Log Ingestor, Query Interface, and Log Generator.

### Log Ingestor
- **Description:** The Log Ingestor is responsible for efficiently handling vast volumes of log data sent over HTTP. It ingests logs in a specific JSON format and stores them in Elasticsearch for later retrieval.
- **Technology Stack:**
  - Language: Python (Flask)
  - Database: Elasticsearch
- **How it works:**
  - The Log Ingestor exposes an HTTP server on port 3000 to receive log entries.
  - Upon receiving a log entry, it asynchronously indexes the log data into Elasticsearch to ensure scalability and performance.
  
### Query Interface
- **Description:** The Query Interface provides a user-friendly interface, either through a web UI or CLI, for searching and filtering logs stored in Elasticsearch. It supports full-text search and specific field filters.
- **Technology Stack:**
  - Language: Python (Flask)
  - Frontend: HTML, JavaScript (Web UI)
  - Database: Elasticsearch
- **How it works:**
  - Users can access the Query Interface via a web browser, providing search criteria such as level, message, timestamp, etc.
  - The Query Interface sends queries to Elasticsearch and displays the results, allowing users to efficiently retrieve logs.

### Log Generator
- **Description:** The Log Generator is a script written in Python that simulates log entries for testing and demonstration purposes. It sends sample log entries to the Log Ingestor over HTTP.
- **Technology Stack:**
  - Language: Python
- **How it works:**
  - The Log Generator script creates sample log entries with various attributes and sends them to the Log Ingestor at regular intervals.

## How to Run

### Log Ingestor
1. Navigate to the directory containing `log_ingestor.py`.
2. Install the required Python packages: `pip install flask elasticsearch requests flask-cors`.
3. Run the Log Ingestor: `python log_ingestor.py`.

### Query Interface
1. Navigate to the directory containing `query_interface.py`.
2. Install the required Python packages: `pip install flask elasticsearch requests flask-cors`.
3. Run the Query Interface: `python query_interface.py`.

### Log Generator
1. Navigate to the directory containing `log_generator.py`.
2. Install the required Python packages: `pip install requests`.
3. Run the Log Generator: `python log_generator.py`.
