# Airflow monitoring and logging

- Monitor status and diagnose problems with DAG runs
- By default, Airflow logs are saved to local file systems as log files
- Can be sent to Azure / AWS
- Can be searched / dashboarded
- Recommends Elastisearch and Splunk to index, search, and analyze logs
- By default, log files are organized by DAG IDs and Task IDs path convention: `logs/dag_id/task_id/execution_date/try_number.log`

## Metrics

- Counters
  - Always increasing
  - Successful/failed tasks
- Gauges
  - Fluctuate
  - Number or running tasks
- Timers
  - Time to finish task
- StatsD
  - Network daemon that listens for metrics
- Prometheus
  - Aggregate and dashboard metrics