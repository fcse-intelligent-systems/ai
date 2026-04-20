import csv
from sklearn.model_selection import train_test_split


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset


if __name__ == '__main__':
    dataset = read_file('car.csv')

    dataset_x = [row[:-1] for row in dataset]
    dataset_y = [row[-1] for row in dataset]

    train_x, test_x, train_y, test_y = train_test_split(dataset_x, dataset_y,
                                                        test_size=0.1, stratify=dataset_y)
