# Asynchronous Messaging with RabbitMQ

## Overview
This project implements a loosely coupled service architecture using RabbitMQ for asynchronous messaging. It includes a publisher service that sends messages to a RabbitMQ broker and a consumer service that processes those messages.

## Services
- **Publisher**: Sends messages to the RabbitMQ broker whenever an event occurs (e.g., new order placed).
- **Consumer**: Subscribes to the RabbitMQ broker and processes messages independently (e.g., logs them, stores them in a database).

## Setup
1. Ensure Docker is installed on your machine.
2. Build and run the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the RabbitMQ management interface at `http://localhost:15672` (default username: guest, password: guest).

## Logging
Both services implement logging to track message sending and receiving.
