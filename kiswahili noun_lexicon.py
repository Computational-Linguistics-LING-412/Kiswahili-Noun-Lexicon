
# KISWAHILI NOUN LEXICON
# Python implementation for reading and analyzing a CSV file

import csv

# STEP 1: Open and read the CSV file

filename = "kiswahili noun_lexicon.csv"

try:
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        # Check required columns
        required_columns = [
            "Stem",
            "Class_pair",
            "Sg-prefix",
            "Pl-prefix",
            "Sg-form",
            "Pl-form",
            "Gloss",
            "Data source"
        ]

        if not all(column in reader.fieldnames for column in required_columns):
            raise ValueError("The CSV file is missing required columns.")

        lexicon = []

        # STEP 2: Store entries in a Python list
        for row in reader:

            # Remove unnecessary spaces
            entry = {
                key: (value or "").strip()
                for key, value in row.items()
            }

            # Standardize noun-class pair spacing
            entry["Class_pair"] = entry["Class_pair"].replace(" ", "")

            lexicon.append(entry)

    # STEP 3: Display the complete lexicon

    print("\n===================================")
    print("       KISWAHILI NOUN LEXICON")
    print("===================================\n")

    for number, noun in enumerate(lexicon, start=1):

        print(f"Entry {number}")
        print("Stem:", noun["Stem"])
        print("Class pair:", noun["Class_pair"])
        print("Singular prefix:", noun["Sg-prefix"])
        print("Plural prefix:", noun["Pl-prefix"])
        print("Singular form:", noun["Sg-form"])
        print("Plural form:", noun["Pl-form"])
        print("English meaning:", noun["Gloss"])
        print("Data source:", noun["Data source"])
        print("-----------------------------------")

    # STEP 4: Count total nouns

    print("\nTOTAL NUMBER OF NOUNS:", len(lexicon))

    # STEP 5: Identify noun-class pairs

    class_pairs = set(
        noun["Class_pair"] for noun in lexicon
    )

    print("\nNOUN-CLASS PAIRS:")
    for pair in sorted(class_pairs):
        print(pair)

    print("TOTAL CLASS PAIRS:", len(class_pairs))

    # STEP 6: Count nouns in each class pair

    print("\nDISTRIBUTION OF NOUNS BY CLASS PAIR:")

    for pair in sorted(class_pairs):

        count = sum(
            1 for noun in lexicon
            if noun["Class_pair"] == pair
        )

        print(f"Class {pair}: {count} nouns")

    # STEP 7: Display data sources

    print("\nDATA SOURCES:")

    sources = {}

    for noun in lexicon:

        source = noun["Data source"]

        sources[source] = sources.get(source, 0) + 1

    for source, count in sources.items():

        print(f"{source}: {count} entries")

    # STEP 8: Check for missing information

    print("\nDATA QUALITY CHECK:")

    missing = 0

    for number, noun in enumerate(lexicon, start=1):

        for column in required_columns:

            if not noun[column]:
                print(f"Entry {number}: Missing {column}")
                missing += 1

    if missing == 0:
        print("No missing fields detected.")

    # STEP 9: Check the minimum assignment requirements

    print("\nASSIGNMENT REQUIREMENTS:")

    if len(lexicon) >= 20:
        print("PASS: At least 20 nouns collected.")
    else:
        print("FAIL: Fewer than 20 nouns collected.")

    if len(class_pairs) >= 4:
        print("PASS: At least four noun-class pairs covered.")
    else:
        print("FAIL: Fewer than four noun-class pairs covered.")

except FileNotFoundError:
    print("ERROR: CSV file not found.")
    print("Make sure the CSV and Python files are in the same folder.")

except Exception as error:
    print("An error occurred:", error)
