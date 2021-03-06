# dataset settings
dataset_type = 'MyDataset'

data_root = '../data/garbage_dump_2022/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

# -------------augmentation operation set-------------
albu_train_transforms = [
    dict(
        type='RandomRotate90',
        p=0.5
    ),
    dict(
        type='ShiftScaleRotate',
        shift_limit=0.0625,
        scale_limit=0.5,
        rotate_limit=30,
        interpolation=1,
        p=0.5),
    dict(
        type='RandomBrightnessContrast',
        brightness_limit=[0.1, 0.3],
        contrast_limit=[0.1, 0.3],
        p=0.2),
    dict(
        type='OneOf',
        transforms=[
            dict(
                type='RGBShift',
                r_shift_limit=10,
                g_shift_limit=10,
                b_shift_limit=10,
                p=1.0),
            dict(
                type='HueSaturationValue',
                hue_shift_limit=20,
                sat_shift_limit=30,
                val_shift_limit=20,
                p=1.0)
        ],
        p=0.1),
    dict(type='JpegCompression', quality_lower=85, quality_upper=95, p=0.2),
    dict(type='ChannelShuffle', p=0.1),
    dict(
        type='OneOf',
        transforms=[
            dict(type='Blur', blur_limit=3, p=1.0),
            dict(type='MedianBlur', blur_limit=3, p=1.0)
        ],
        p=0.1),
]
# -------------augmentation operation set-------------

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1024, 1024), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    # -------------augmentation-------------
    dict(
            type='Albu',
            transforms=albu_train_transforms,
            bbox_params=dict(
                type='BboxParams',
                format='pascal_voc',
                label_fields=['gt_labels'],
                min_visibility=0.0,
                filter_lost_elements=True),
            keymap={
                'img': 'image',
                # 'gt_masks': 'masks',
                'gt_bboxes': 'bboxes'
            },
            update_pad_shape=False,
            skip_img_without_anno=True),
    # -------------augmentation-------------
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1024, 1024), #
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=0,
    train=dict(
        # # type=dataset_type,
        # type='RepeatDataset',
        # times=1,
        # # times=3,
        # dataset=dict(
        #     type=dataset_type,
        #     ann_file=[
        #         data_root + 'VOC2012/train/train.txt'
        #         # data_root + 'VOC2012/ImageSets/Main/trainval.txt'
        #     ],
        #     img_prefix=[data_root + 'VOC2012/train'],
        #     pipeline=train_pipeline)),
        type='ClassBalancedDataset',
        oversample_thr=0.3,
        dataset=dict(
            type=dataset_type,
            ann_file=data_root + 'VOC2012/train/train.txt',
            img_prefix=data_root + 'VOC2012/train',
            pipeline=train_pipeline)
    ),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'VOC2012/test/test.txt',
        img_prefix=data_root + 'VOC2012/test',
        # ann_file=data_root + 'VOC2012/train/train.txt',
        # img_prefix=data_root + 'VOC2012/train',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'VOC2012/test/test.txt',
        img_prefix=data_root + 'VOC2012/test',
        # ann_file=data_root + 'VOC2012/train/train.txt',
        # img_prefix=data_root + 'VOC2012/train',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='mAP')
