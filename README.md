# Real-Time Crypto Anomaly Detection System

A high-throughput, distributed data pipeline designed to ingest live cryptocurrency trade data, process it via Kafka, and perform real-time machine learning inference within a Kubernetes-orchestrated environment.


## Project Overview

This project demonstrates the implementation of a modern, cloud-native data engineering stack. The system is engineered to handle high-velocity data streams from the Binance Public WebSocket, decoupling data ingestion from inference using an event-driven architecture. The final goal is a fully resilient, auto-scaling deployment capable of detecting market anomalies with minimal latency.

## Core Technical Stack

* **Languages:** Python 3.10+
* **Streaming & Messaging:** Apache Kafka, WebSockets
* **Containerization & Orchestration:** Docker, Kubernetes (Minikube)
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **API Framework:** FastAPI
* **Monitoring:** Prometheus, Grafana

## Development Roadmap & Status

### Phase 1: Infrastructure and Ingestion (Completed)
* **Environment Orchestration:** Established a containerized development environment using Docker and Kubernetes.
* **Live Stream Integration:** Developed a robust connection to the Binance WebSocket API to capture real-time BTC/USDT trade data.
* **Event Streaming:** Implemented a Kafka cluster via Docker Compose with a dedicated producer to handle trade message buffering.
* **Schema Definition:** Designed a lightweight JSON schema (timestamp, price, volume) for efficient downstream serialization.

### Phase 2: ML Modeling and Containerization (In Progress)
* **Feature Engineering:** Computing rolling statistical metrics and price returns for anomaly detection.
* **Model Training:** Implementing Isolation Forest and Z-Score thresholding for outlier identification.
* **Inference API:** Developing a FastAPI wrapper for the serialized ML model to provide real-time anomaly scores.

### Phase 3: Scaling and Observability (Planned)
* **K8s Deployment:** Orchestrating replicas with liveness/readiness probes and resource constraints.
* **Streaming Inference:** Integrating the Kafka consumer directly into the ML service for end-to-end processing.
* **Elasticity:** Implementing Horizontal Pod Autoscaling (HPA) based on CPU utilization and consumer lag.
* **Monitoring:** Deploying a Prometheus and Grafana stack to visualize request latency and anomaly rates.

## Architectural Features

* **Scalability:** Designed to scale horizontally via Kubernetes to handle volatile market spikes.
* **Resilience:** Decoupled architecture ensures that the ML inference engine can be updated or restarted without losing incoming stream data.
* **Efficiency:** Utilizing batch writes to Kafka and pinned requirements in Docker to ensure reproducible, high-performance execution.

## Local Setup

### Prerequisites
* Docker & Docker Compose
* Minikube / kubectl
* Python 3.10+

### Installation
1. Clone the repository:
 *  git clone [https://github.com/cookekieran/Bitcoin-Anomaly-Detection]

2. Initialize the Kafka Cluster:
* docker-compose up -d

3. Run the Producer:
* python src/producer.py

Current Focus: Transitioning the ML pipeline from historical training to the FastAPI containerization phase.