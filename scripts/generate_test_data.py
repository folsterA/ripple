from faker import Faker
import json
from pathlib import Path
import random

fake = Faker()


class User:
    id: str
    name: str
    profile_url: str

    def __init__(self, id, name, profile_url):
        self.id = id
        self.name = name
        self.profile_url = profile_url


def generate_user_data():
    users = []
    for i in range(5):
        user = User(i, fake.user_name(), fake.image_url())
        users.append(user.__dict__)
    return users


class Message:
    chat_id: str
    contents: str
    id: str
    timestamp: int
    user_id: str

    def __init__(self, chat_id, contents, id, timestamp, user_id):
        self.chat_id = chat_id
        self.contents = contents
        self.id = id
        self.timestamp = timestamp
        self.user_id = user_id


def generate_message_data(users):
    messages = []
    for i in range(5):
        chat_id = i
        start_datetime = int(
            fake.date_time_between(start_date="-5d", end_date="now").timestamp()
        )
        timestamp = start_datetime
        for j in range(random.randint(10, 20)):
            user_id = random.randint(0, 4)
            contents = fake.text()
            timestamp += random.randint(30, 3 * 60 * 60)
            message = Message(chat_id, contents, i * 5 + j, timestamp, user_id)
            messages.append(message.__dict__)
    return messages


def main():
    output_dir = Path(__file__).parent.parent / "src-tauri" / "test-data"
    output_dir.mkdir(parents=True, exist_ok=True)

    user_file = output_dir / "user.json"
    if user_file.exists():
        user_file.unlink()

    users = generate_user_data()
    user_file.write_text(json.dumps(users, indent=2))

    message_file = output_dir / "messages.json"
    if message_file.exists():
        message_file.unlink()

    messages = generate_message_data(users)
    message_file.write_text(json.dumps(messages, indent=2))

    print(f"Wrote test data to {user_file} and {message_file}")


if __name__ == "__main__":
    main()
