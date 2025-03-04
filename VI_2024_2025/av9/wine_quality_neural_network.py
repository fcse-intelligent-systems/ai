from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


if __name__ == '__main__':
    dataset = read_dataset()
    dataset_bad = [row for row in dataset if row[-1] == 'bad']
    dataset_good = [row for row in dataset if row[-1] == 'good']

    train_set = dataset_bad[:int(0.7 * len(dataset_bad))] + \
                dataset_good[:int(0.7 * len(dataset_good))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_set = dataset_bad[int(0.7 * len(dataset_bad)):int(0.8 * len(dataset_bad))] + \
              dataset_good[int(0.7 * len(dataset_good)):int(0.8 * len(dataset_good))]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    test_set = dataset_bad[int(0.8 * len(dataset_bad)):] + \
               dataset_good[int(0.8 * len(dataset_good)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    clf_1 = MLPClassifier(5,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf_2 = MLPClassifier(10,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf_3 = MLPClassifier(100,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)

    clf_1.fit(train_x, train_y)
    clf_2.fit(train_x, train_y)
    clf_3.fit(train_x, train_y)

    pred_1 = clf_1.predict(val_x)
    pred_2 = clf_2.predict(val_x)
    pred_3 = clf_3.predict(val_x)

    acc_1 = accuracy_score(val_y, pred_1)
    print(f'Tochnost so 5 nevroni nad validacisko mnozestvo: {acc_1}')

    acc_2 = accuracy_score(val_y, pred_2)
    print(f'Tochnost so 10 nevroni nad validacisko mnozestvo: {acc_2}')

    acc_3 = accuracy_score(val_y, pred_3)
    print(f'Tochnost so 100 nevroni nad validacisko mnozestvo: {acc_3}')

    if acc_1 >= acc_2 and acc_1 >= acc_3:
        pred = clf_1.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')
    elif acc_2 >= acc_1 and acc_2 >= acc_3:
        pred = clf_2.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')
    else:
        pred = clf_3.predict(test_x)
        acc = accuracy_score(test_y, pred)
        print(f'Tochnost so testirachko mnozestvo: {acc}')
