import argparse


def parse_csv():
    parser = argparse.ArgumentParser(description="Process CSV file.")
    parser.add_argument(
        "csv_file", type=argparse.FileType("r"), help="CSV file to be parsed"
    )
    parser.add_argument(
        "-c",
        "--column",
        action="append",
        type=int,
        help="columns to select from CSV file",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="print logging messages"
    )

    args = parser.parse_args()

    for line in args.csv_file:
        seperated_line = line.strip().split(",")
        new_line = [
            seperated_line[c] for c in (args.column or range(len(seperated_line)))
        ]
        print(", ".join(new_line))


if __name__ == "__main__":
    parse_csv()
