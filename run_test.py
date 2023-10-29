import os

weights = '2023-10-27 03_19_49.671230_train'
model = 'SFDet-ResNet'
mode = 'test'
batch = 32
score_threshold = 0.01
use_gpu = 'True'

start = 0
save_step = 5
num_epochs = 100

for i in range(start + save_step, num_epochs + save_step, save_step):
    pretrained_model = '"{}/{}"'.format(weights, i)
    args = ('--mode {} --pretrained_model {} --model {} --use_gpu {} '
            '--batch_size {} --score_threshold {}')
    args = args.format(mode,
                       pretrained_model,
                       model,
                       use_gpu,
                       batch,
                       score_threshold)
    command = 'python main.py {}'.format(args)
    os.system(command)
