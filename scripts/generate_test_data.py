from faker import Faker
import json
from pathlib import Path
import random

fake = Faker()

num_servers = 5
num_channels = 10
num_users = 10
pin_probability = 0.1

class User:
    id: str
    name: str
    profile_url: str

    def __init__(self):
        self.id = fake.uuid4()
        self.name = fake.user_name()
        self.profile_url = fake.image_url()


def generate_user_data():
    users = []
    for i in range(num_users):
        user = User()
        users.append(user.__dict__)
    return users

class Server:
    id: str
    name: str
    profile_url: str
    description: str

    def __init__(self):
        self.id = fake.uuid4()
        self.name = fake.company()
        self.profile_url = fake.image_url()
        self.description = fake.sentence()

def generate_server_data():
    servers = []
    for i in range(num_servers):
        server = Server()
        servers.append(server.__dict__)
    return servers

class Channel:
    id: str
    name: str
    pinned_messages: list[str]
    description: str

    def __init__(self):
        self.id = fake.uuid4()
        self.name = "-".join(fake.words(nb=random.randint(2, 5))).lower()
        self.description = fake.sentence()

def generate_channel_data(servers):
    channels = []
    for server in servers:
        count = random.randint(1, num_channels)
        for _ in range(count):
            channel = Channel()
            ch_dict = channel.__dict__.copy()
            ch_dict["server_id"] = server["id"]
            ch_dict["pinned_messages"] = []
            channels.append(ch_dict)
    return channels


class Message:
    channel_id: str
    contents: str
    id: str
    timestamp: int
    user_id: str

    def __init__(self, channel_id, contents, id, timestamp, user_id):
        self.channel_id = channel_id
        self.contents = contents
        self.id = id
        self.timestamp = timestamp
        self.user_id = user_id


def generate_message_data(channels, users):
    messages = []
    if not channels or not users:
        return messages

    for channel in channels:
        # ensure pinned_messages exists and is a list
        if "pinned_messages" not in channel or channel["pinned_messages"] is None:
            channel["pinned_messages"] = []

        # start somewhere in the last 5 days
        start_datetime = int(
            fake.date_time_between(start_date="-5d", end_date="now").timestamp()
        )
        timestamp = start_datetime

        # generate between 10 and 20 messages per channel
        for j in range(random.randint(10, 20)):
            user = random.choice(users)
            contents = fake.sentence(nb_words=random.randint(5, 20))
            # increment timestamp by between 30 seconds and 3 hours
            timestamp += random.randint(30, 3 * 60 * 60)
            msg_id = fake.uuid4()
            message = Message(
                channel["id"],
                contents,
                msg_id,
                timestamp,
                user["id"],
            )
            messages.append(message.__dict__)

            # decide whether to pin this message
            if random.random() < pin_probability:
                # keep pinned list small and unique
                if msg_id not in channel["pinned_messages"]:
                    channel["pinned_messages"].append(msg_id)

    return messages

def main():
    output_dir = Path(__file__).parent.parent / "src-tauri" / "test-data"
    output_dir.mkdir(parents=True, exist_ok=True)

    user_file = output_dir / "user.json"
    if user_file.exists():
        user_file.unlink()
    users = generate_user_data()

    server_file = output_dir / "servers.json"
    if server_file.exists():
        server_file.unlink()
    servers = generate_server_data()

    channel_file = output_dir / "channels.json"
    if channel_file.exists():
        channel_file.unlink()
    channels = generate_channel_data(servers)

    message_file = output_dir / "messages.json"
    if message_file.exists():
        message_file.unlink()
    messages = generate_message_data(channels, users)

    user_file.write_text(json.dumps(users, indent=2))
    server_file.write_text(json.dumps(servers, indent=2))
    channel_file.write_text(json.dumps(channels, indent=2))
    message_file.write_text(json.dumps(messages, indent=2))

    print(f"Wrote test data to {output_dir}")


if __name__ == "__main__":
    main()
