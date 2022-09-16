# Building Streaming Pipelined Using Kafka

## Distributed Event Streaming Platform Components

- Event
  - Something worth noticing is happening
  - Type of data
  - Describes an entity's observable state updates over time
    - GPS location of a car
    - Temperature of a room
    - Blood Pressure of a Patient
    - RAM usage of an application
- Event Format
  - Primitive
    - Plain text number or date
  - Key - value
  - Complex
    - list
    - tuple
    - JSON
    - XML
    - bytes
  - Often associated with a timestamp
- Event Streaming
  - One source
    - Sensor
    - Device
    - Database
    - Application
  - Event Destinaton
    - File system
    - Database
    - Application
  - Event source to event destination = event streaming
    - Can be complex with multiple sources and destinations
    - Destination can be a source as well to an additional destination
- ESP - Event Stream Platform
  - Acts as middle layer between event source and event destination
  - All sources send events to ESP
  - Destinations subscribe to events from ESP
  - Event Broker
    - Consume events from event sources
    - Ingestor
      - Receive events
    - Processor
      - Operations
        - Serialization
        - Encryption
    - Consumption
  - Event Storage
    - Store events
  - Analytic and Query Engine
- Popular ESPs
  - Amazon Kinesis
  - Apache Kafka
    - Most popular ESP
  - Apache Spark
  - Apache Flink
  - Apache Storm
  - Unique features and applications

---

## Apache Kafka Overview

- Many open source and commercial ESPs available
- Kafka - comprehensive, open-source, most common
- Originally used to track user activity on a website
  - Sensor, GPS, hardware, software
- Collect and integrate huge numbers of logs
  - Fintech - payments and transactions
- High throughput from multiple sources
- Real-time processing and analytics
- Notifications
- Governance and auditing
- Distributed Clients
  - Cluster with many servers (brokers)
  - Receive, store, and manage events
  - Zookeeper
    - Distributed coordination service
    - Keeps track of brokers
    - Keeps track of topics
    - Keeps track of partitions
    - Keeps track of consumers
  - TCP connection
    - Client to broker
    - Broker to broker
  - Kafka CLI
    - Rest api
- Main Features
  - Distribution System
    - Scalable
    - High throughput and concurrency
    - Events streaming in parallell
    - Fast
    - Multiple partitions and replications
      - Fault tolerant
      - Reliable
    - Permanent persistency
    - Open-source
    - Well documented
    - Challenging to configure and deploy
    - Extensive tuning and configuration, especially enterprise
- On-demand ESP as a service
  - Confluent Clout
  - IBM Event Streams
  - Amazon Manages Streaming for Kafka (MSK)

---

## Building Event Streaming Pipelines Using Kafka

- Kafka cluster has one or many brokers
  - Synchronized and managed by Zookeeper
  - Server for ingesting events
  - Saved to topics
  - Pushed to consumers
  - Partitions
  - Replication
  - Increase fault tolerance and throughput
  - Consumption and distribution occurs in parallel
- Kafka CLI
  - Powerful scripts for building pipelines
  - Create a topic
  - List topic
  - get topic details
  - Delete topic
- Kafka producer
  - Client applications that publish events to topic partitions
  - Can be associated with a key
  - Key is used to determine which partition to send the event to
  - Producer CLI
- Kafka Consumers
  - Client applications that subscribe to topics
  - Read from topic partitions in order published
  - Store an offset record for each partition
  - Offset can be reset to zero to read all events from the beginning again

### Example - weather pipeline

- IBM Weather Company Data
  - Weather data
  - Historical data
  - Real-time data
  - Weather API
- Twitter topics
  - JSON
- Create Producer, Topic, and Consumer to each
  - Can use a DB writer to write to a database from the consumer
  - RDBMS
  - Dashboard

## Review

- Core components of Kafka
  - Brokers
    - Dedicated servers
    - Receive
    - Store
    - Process
    - Distribute
  - Topics
    - Containers of DB of events
  - Partitions
    - Divide topics into different brokers
  - Replications
    - Duplicate partitions to brokers
  - Producers
    - Client applications to publish events into topics
  - Consumers
    - Client applications subscribe to topics to read events
  - CLIs
    - Kafka-topics
    - Kafka-console-producer
    - Kafka-console-consumer

---

## Kafka Streaming Process

- Stream processing applications
  - Filter
  - Aggregate
  - Ad hoc
    - read from a topic
    - process (filter, aggregate, etc)
    - publish to another topic
    - raw_weather_topic -> processed_weather_topic
- Kafka Streams API
  - Simple client library to facilitate data processing in event streaming pipelines
  - Processes and analyzes data stored in Kafka topics
  - Process each record only once
  - One record at a time
  - Stream processing topology
    - Each node - stream processor
    - Performs transformation
    - Produces output stream
    - edges - IO streams
    - Source processor - nothing upstream
    - Synch processor - nothing downstream
    - Source processor - reads from a topic
    - Stream processor - filters
    - Synch processor - writes to a topic
    - 