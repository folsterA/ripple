import json
from pathlib import Path

def main():
    data = {
        "user": {
            "id": 1,
            "name": "Test User"
        }
    }

    output_dir = Path("test-data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "user.json"
    output_file.write_text(json.dumps(data, indent=2))

    print(f"Wrote test data to {output_file}")

if __name__ == "__main__":
    main()