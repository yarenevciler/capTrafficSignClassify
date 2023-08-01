# -*- coding: utf-8 -*-
"""Model configs in json format"""

CFG = {
    "data": {
        "path": "oxford_iiit_pet:3.2.0",
        "image_size": 30,
        "load_with_info": True
    },
    "train": {
        "batch_size": 64,
        "buffer_size": 1000,
        "epoches": 20,
        "val_subsplits": 5,
        "optimizer": {
            "type": "adam"
        },
        "metrics": ["accuracy"]
    },
    "model": {
        "input": [30, 30, 3],
        "up_stack": {
            "layer_1": 512,
            "layer_2": 256,
            "layer_3": 128,
            "layer_4": 64,
            "kernels": 3
        },
        "output": 3
    },
    "project": {
        "path": "/opt/project"
    }
}