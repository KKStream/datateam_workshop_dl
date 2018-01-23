"""
"""
import csv
import numpy as np
import os
import sklearn.metrics


def auc(guess, truth):
    """
    """
    guess = guess.flatten()
    truth = truth.flatten()
    
    fprs, tprs, _ = sklearn.metrics.roc_curve(truth, guess)

    return sklearn.metrics.auc(fprs, tprs)


def mini_batches(eigens, labels, batch_size, once):
    """
    """
    indices = np.arange(eigens.shape[0])

    # NOTE: if is_training is True, drop remain samples in each epoch
    #       if is_training is False, yield all samples in one epoch
    epoch_size = indices.size - indices.size % batch_size

    step = 0

    while True:
        if not once:
            np.random.shuffle(indices)

        for i in range(0, epoch_size, batch_size):
            temp_eigens = eigens[indices[i:i+batch_size]]
            temp_labels = labels[indices[i:i+batch_size]]

            yield step, temp_eigens, temp_labels

            step += 1

        if once:
            temp_eigens = eigens[indices[epoch_size:]]
            temp_labels = labels[indices[epoch_size:]]

            yield step, temp_eigens, temp_labels

            break


def write_result(name, predictions):
    """
    """
    if predictions is None:
        raise Exception('need predictions')

    predictions = predictions.flatten()

    if not os.path.exists('./results/'):
        os.makedirs('./results/')

    path = os.path.join('./results/', name)

    with open(path, 'wb') as csv_target_file:
        target_writer = csv.writer(csv_target_file, delimiter=',')

        header = [
            'user_id',
            'time_slot_0', 'time_slot_1', 'time_slot_2', 'time_slot_3',
            'time_slot_4', 'time_slot_5', 'time_slot_6', 'time_slot_7',
            'time_slot_8', 'time_slot_9', 'time_slot_10', 'time_slot_11',
            'time_slot_12', 'time_slot_13', 'time_slot_14', 'time_slot_15',
            'time_slot_16', 'time_slot_17', 'time_slot_18', 'time_slot_19',
            'time_slot_20', 'time_slot_21', 'time_slot_22', 'time_slot_23',
            'time_slot_24', 'time_slot_25', 'time_slot_26', 'time_slot_27',
        ]

        target_writer.writerow(header)

        for i in range(0, len(predictions), 28):
            userid = [57159 + i / 28]
            labels = predictions[i:i+28].tolist()

            target_writer.writerow(userid + labels)
