import os


def load_data(data_path):
    train_path = os.path.join(data_path, 'train')
    dev_path = os.path.join(data_path, 'dev')
    test_path = os.path.join(data_path, 'test')

    train_data = load_data_workhorse(train_path)
    dev_data = load_data_workhorse(dev_path)
    test_data = load_data_workhorse(test_path)

    return [train_data, dev_data, test_data]


def load_data_workhorse(type_path):
    data = {}
    for each_file in os.listdir(type_path):
        data[each_file] = {}
        data[each_file]['sentences'] = []
        data[each_file]['question'] = []
        data[each_file]['options'] = []
        data[each_file]['answer'] = []
        with open(os.path.join(type_path, each_file), 'r') as f:
            for each_line in f:
                parsed = each_line.strip().split()
                if parsed[0] == 'SENTENCE':
                    data[each_file]['sentences'].append(parsed[1:])
                elif parsed[0] == 'QUESTION':
                    data[each_file]['question'] = parsed[1:]
                else:
                    data[each_file]['options'].append(parsed[1:-1])
                    if parsed[-1] == '1':
                        data[each_file]['answer'] = parsed[1:-1]
    return data


if __name__ == '__main__':
    data_path = 'Path/to/data/directory'
    train_data, dev_data, test_data = load_data(data_path)
