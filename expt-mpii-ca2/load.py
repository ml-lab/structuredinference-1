"""Load MPII CA2 poses and associated actions."""

import numpy as np

from p2d_loader import load_p2d_data


def loadDataset():
    seq_length = 32
    seq_skip = 3
    data = load_p2d_data('./mpii_ca2.h5', seq_length, seq_skip,
                         gap=3, val_frac=0.2, add_noise=None,
                         load_actions=False)

    dim_observations = data.train_poses.shape[2]

    dataset = {}

    dataset['train'] = data.train_poses
    dataset['mask_train'] = np.ones(data.train_poses.shape[:2])

    dataset['valid'] = data.val_poses
    dataset['mask_valid'] = np.ones(data.val_poses.shape[:2])

    dataset['test'] = dataset['valid']
    dataset['mask_test'] = dataset['mask_valid']

    dataset['dim_observations'] = dim_observations
    dataset['data_type'] = 'real'

    dataset['p2d_mean'] = data.mean
    dataset['p2d_std'] = data.std

    # dataset['train_cond_vals'] = data.train_actions
    # dataset['val_cond_vals'] = data.val_actions
    # dataset['test_cond_vals'] = data.val_actions
    # dataset['p2d_action_names'] = data.action_names

    dataset['p2d_parents'] = data.parents

    # for action prediction
    # dataset['train_aclass_ds'] = data.train_aclass_ds
    # dataset['val_aclass_ds'] = data.val_aclass_ds

    print('Shapes of various things:')
    to_check = [
        'train', 'valid', 'test',
        # 'train_cond_vals', 'val_cond_vals', 'test_cond_vals'
    ]
    for to_shape in to_check:
        print('%s: %s' % (to_shape, dataset[to_shape].shape))
    # for name in ['train_aclass_ds', 'val_aclass_ds']:
    #     print('%s: %d (list)' % (name, len(dataset[name])))

    return dataset
