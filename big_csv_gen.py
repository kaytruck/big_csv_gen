import csv


def main():
    with open("bigdat.csv", "w", newline="", encoding="UTF-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in range(1_000):
            row = ["a", "b", "c"]
            for i in range(10):
                row.append(f"D{i}")
            writer.writerow(row)


if __name__ == "__main__":
    main()
