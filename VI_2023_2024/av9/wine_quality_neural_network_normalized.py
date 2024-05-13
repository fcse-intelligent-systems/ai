from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score


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

    clf_1 = MLPClassifier(10,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf_1.fit(train_x, train_y)
    pred_1 = clf_1.predict(val_x)
    acc_1 = accuracy_score(val_y, pred_1)
    print(f'Tochnost so originalno mnozestvo: {acc_1}')

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_x)

    clf_2 = MLPClassifier(10,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf_2.fit(standard_scaler.transform(train_x), train_y)
    pred_2 = clf_2.predict(standard_scaler.transform(val_x))
    acc_2 = accuracy_score(val_y, pred_2)
    print(f'Tochnost so normalizacija so StandardScaler: {acc_2}')

    min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
    min_max_scaler.fit(train_x)

    clf_3 = MLPClassifier(10,
                          activation='relu',
                          learning_rate_init=0.001,
                          max_iter=500,
                          random_state=0)
    clf_3.fit(min_max_scaler.transform(train_x), train_y)
    pred_3 = clf_3.predict(min_max_scaler.transform(val_x))
    acc_3 = accuracy_score(val_y, pred_3)
    print(f'Tochnost so normalizacija so MinMaxScaler (-1, 1): {acc_3}')

    if acc_1 >= acc_2 and acc_1 >= acc_3:
        pred = clf_1.predict(test_x)
    elif acc_2 >= acc_1 and acc_2 >= acc_3:
        pred = clf_2.predict(standard_scaler.transform(test_x))
    else:
        pred = clf_3.predict(min_max_scaler.transform(test_x))

    tp, tn, fp, fn = 0, 0, 0, 0
    for y_true, y_pred in zip(test_y, pred):
        if y_true == 'good':
            if y_pred == 'good':
                tp += 1
            else:
                fn += 1
        else:
            if y_pred == 'bad':
                tn += 1
            else:
                fp += 1

    acc = (tp + tn) / (tp + tn + fp + fn)
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)

    # acc = accuracy_score(test_y, pred)
    # precision = precision_score(test_y, pred)
    # recall = recall_score(test_y, pred)

    print(f'Tochnost so testirachko mnozestvo: {acc}')
    print(f'Preciznost so testirachko mnozestvo: {precision}')
    print(f'Odziv so testirachko mnozestvo: {recall}')
