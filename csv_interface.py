import csv

# return a dict containing all the entries from the given csv
def read(lor):
    with open(lor, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        words = {}
        print("reading rows:")
        for row in csv_reader:
            line_count += 1
            words[row["word"]] = row["frequency"]

        return words

# write the given words from the dict into the given CSV file
def write(words, lor):
    with open(lor, mode='w') as tweets:
        fieldnames = ['word', 'frequency']
        writer = csv.DictWriter(tweets, fieldnames=fieldnames)

        writer.writeheader()
        previous_words = read(lor)
        for word in words.keys():
            if word in previous_words:
                previous_words[word] += words[word]
            else:
                writer.writerow({'word': word, 'frequency': words[word]})
        for word in previous_words.keys():
            writer.writerow({'word': word, 'frequency': previous_words[word]})
