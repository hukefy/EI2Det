import argparse

import yaml

from wandb_utils import WandbLogger

WANDB_ARTIFACT_PREFIX = 'wandb-artifact://'


def create_dataset_artifact(opt):
    with open(opt.data) as f:
        data = yaml.safe_load(f)  # data dict
    logger = WandbLogger(opt, '', None, data, job_type='Dataset Creation')

