from pathlib import Path

counter_file = Path("counter.txt")

if counter_file.exists():
    counter = int(counter_file.read_text().strip())
else:
    counter = 0

counter += 1

counter_file.write_text(str(counter))

print(f"Counter wurde auf {counter} erhöht.")