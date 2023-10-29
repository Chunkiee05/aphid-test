import os.path as osp

weights = 'SSD.2023-04-05 15_06_29.598914_train'
mode = 'test'
start = 140
save_step = 5
num_epochs = 220

for i in range(start + save_step, num_epochs + save_step, save_step):
    text_file = '{}_{}_{}.txt'.format(weights, mode, i)
    file_path = osp.join('tests', weights, text_file)
    with open(file_path, 'r') as f:
        last_line = f.readlines()[-4]
        print(i, last_line)
