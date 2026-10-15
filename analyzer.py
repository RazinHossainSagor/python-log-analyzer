from collections import Counter
from datetime import datetime

LOG_FILE = "sample.log"
REPORT_FILE = "report.txt"
ERROR_LIMIT = 2   # high limit ERROR then warning show


def read_logs(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{path}' file not found!")
        return None


def analyze(lines):
    levels = Counter()
    errors = Counter()

    for line in lines:
        parts = line.split(" ", 3)   # date, time, level, message
        if len(parts) < 4:
            continue
        level, message = parts[2], parts[3]
        levels[level] += 1
        if level == "ERROR":
            errors[message] += 1

    return levels, errors


def save_report(total, levels, errors):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_errors = levels.get("ERROR", 0)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("===== LOG REPORT =====\n")
        f.write(f"Generated: {now}\n")
        f.write(f"Total lines: {total}\n\n")

        f.write("Level count:\n")
        for level, count in levels.items():
            f.write(f"  {level}: {count}\n")

        f.write("\nTop errors:\n")
        for msg, count in errors.most_common():
            f.write(f"  {msg} -> {count} times\n")

        if total_errors > ERROR_LIMIT:
            f.write(f"\n!! WARNING: {total_errors} ERROR found !!\n")


def main():
    lines = read_logs(LOG_FILE)
    if lines is None:
        return

    levels, errors = analyze(lines)
    save_report(len(lines), levels, errors)

    print("Analysis Finish! report.txt Create Done!\n")
    print(open(REPORT_FILE, encoding="utf-8").read())


if __name__ == "__main__":
    main()