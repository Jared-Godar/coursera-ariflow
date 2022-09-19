# Launch Kafka

## Download 

wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

## Extract

tar -xzf kafka_2.12-2.8.0.tgz

Navigate to `c:\kafka` in command prompt to launch zookeeper

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`
In a new terminal window, change directory to the kafka foolder and run the following command:

.\bin\windows\kafka-server-start.bat .\config\server.properties

## Create Topic in a new terminal

bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

## Start a producer


## Consumer - new terminal

cd kafka
bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092

## Kafka Directories

Kafka uses the directory /tmp/kakfa-logs to store the messages.

Explore the folder news-0 inside /tmp/kakfa-logs.

This is where all the messages are stored.

Explore the folder /home/project/kafka_2.12-2.8.0

This folder has the below 3 sub directories.

---

Create a new topic called `weather`

bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092

Post messages to the topic `weather`

bin/kafka-console-producer.sh --topic weather --bootstrap-server localhost:9092

Print test messages

bin/kafka-console-consumer.sh --topic weather --from-beginning --bootstrap-server localhost:9092

---

Start Zookeeper

bin/zookeeper-server-start.sh config/zookeeper.properties

Start Kafka Server

bin/kafka-server-start.sh config/server.properties

Create a topic and producer for processing bank ATM transactions
Next, we will be creating a bankbranch topic to process the messages that come from the ATM machines of bank branches.

Suppose the messages come from the ATM in the form of a simple JSON object, including an ATM id and a transaction id like the following example:

`{"atmid": 1, "transid": 100}`

Create a new topic using the `--topic` argument with the name `bankbranch`. In order to simplify the topic configuration and better explain how message key and consumer offset work, here we specify `--partitions` 2 argument to create two partitions for this topic. You may try other `partitions` settings for this topic if you are interested in comparing the difference.

bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic bankbranch  --partitions 2

Now let's list all the topics to see if `bankbranch` has been created successfully.

bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

We can also use the `--describe` command to check the details of the topic `bankbranch`

bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch

Next, we can create a producer to publish some ATM transaction messages.

bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch 

Paste the following messages

{"atmid": 1, "transid": 100}
{"atmid": 1, "transid": 101}
{"atmid": 2, "transid": 200}
{"atmid": 1, "transid": 102}
{"atmid": 2, "transid": 201}

hen, let's create a consumer in a new terminal window to consume these 5 new messages.

Start a new terminal and go to the extracted Kafka folder:

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning

Produce and consume with message keys
In this step, you will be using message keys to ensure that messages with the same key will be consumed in the same order as they were published. In the backend, messages with the same key will be published into the same partition and will always be consumed by the same consumer. As such, the original publication order is kept in the consumer side.

ASt this point, you should have the following four terminals open in Cloud IDE:

Zookeeper terminal
Kafka Server terminal
Producer terminal
Consumer terminal
In the next steps, you will be frequently switching among these terminals.

First, go to the consumer terminal and stop the consumer using Ctrl + C (Windows)
or Command + . (Mac).

Then, switch to the Producer terminal and stop the previous producer.

Ok, we can now start a new producer and consumer, this time using message keys. You can start a new producer with the following message key commands:

--property parse.key=true to make the producer parse message keys
--property key.separator=: define the key separator to be the : character,
so our message with key now looks like the following key-value pair example: - 1:{"atmid": 1, "transid": 102}. Here the message key is 1, which also corresponds to the ATM id, and the value is the transaction JSON object, {"atmid": 1, "transid": 102}.

Start a new producer with message key enabled:

bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch --property parse.key=true --property key.separator=:


1:{"atmid": 1, "transid": 102}
1:{"atmid": 1, "transid": 103}
2:{"atmid": 2, "transid": 202}
2:{"atmid": 2, "transid": 203}
1:{"atmid": 1, "transid": 104}


Next, switch to the consumer terminal again, and start a new consumer with
--property print.key=true --property key.separator=: arguments to print the keys

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning --property print.key=true --property key.separator=:

### Consumer Offset

Topic partitions keeps published messages in a sequence, like a list. Message offset indicates a message's position in the sequence. For example, the offset of an empty Partition 0 of bankbranch is 0, and if you publish the first message to the partition, its offset will be 1.

By using offsets in the consumer, you can specify the starting position for message consumption, such as from the beginning to retrieve all messages, or from some later point to retrieve only the latest messages.

### Consumer Group

In addition, we normally group related consumers together as a consumer group. For example, we may want to create a consumer for each ATM in the bank and manage all ATM related consumers together in a group.

So let's see how to create a consumer group, which is actually very easy with the --group argument.

In the consumer terminal, stop the previous consumer if it is still running.

In the consumer terminal, stop the previous consumer if it is still running.

Run the following command to create a new consumer within a consumer group called atm-app:

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

After the consumer within the atm-app consumer group is started, you should not expect any messages to be consumed. This is because the offsets for both partitions have already reached to the end. In other words, all messages have already been consumed, and therefore dequeued, by previous consumers.

You can verify that by checking consumer group details.

Stop the consumer.

Show the details of the consumer group atm-app:

bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group atm-app

Recall that we have published 10 messages in total, and we can see the CURRENT-OFFSET column of partition 1 is 6 and CURRENT-OFFSET of partition 0 is 4, and they add up to 10 messages.

The LOG-END-OFFSETcolumn indicates the last offset or the end of the sequence, which is 6 for partition 1 and 4 for partition 0. Thus, both partitions have reached the end of their queues and no more messages are available for consumption.

Meanwhile, you can check the LAG column which represents the count of unconsumed messages for each partition. Currently it is 0 for all partitions, as expected.

Now, let's produce more messages and see how the offsets change.

Switch to the previous producer terminal, and publish two more messages:

1:{"atmid": 1, "transid": 105}
2:{"atmid": 2, "transid": 204}

and let's switch back to the consumer terminal and check the consumer group details again:

bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group atm-app

Let's start the consumer again and see whether the two new messages will be consumed.

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

OK, now both partitions have reached the end once again. But what if you want to consume the messages again from the beginning?

We can do that via resetting offset in the next step.

Reset offset
We can reset the index with the --reset-offsets argument.

First let's try resetting the offset to the earliest position (beginning) using --reset-offsets --to-earliest.

Stop the previous consumer if it is still running, and run the following command to reset the offset:

bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --to-earliest --execute

Start the consumer again:

ou should see that all 12 messages are consumed and that all offsets have reached the partition ends again.

In fact, you can reset the offset to any position. For example, let's reset the offset so that we only consume the last two messages.

Stop the previous consumer

Shift the offset to left by 2 using --reset-offsets --shift-by -2:

bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --shift-by -2 --execute

If you run the consumer again, you should see that we consumed 4 messages, 2 for each partition:

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

### Summary
In this lab, you have learned how to include message keys in publication to keep their message states/order. You have also learned how to reset the offset to control the message consumption starting point.


