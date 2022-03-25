_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py', '../_base_/mydatasets/voc0712.py',
    '../_base_/mydefault_runtime.py'
]
model = dict(roi_head=dict(bbox_head=dict(num_classes=1)))
# optimizer
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
# batchsize=16,lr=0.02
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
# runtime settings
runner = dict(
    type='EpochBasedRunner', max_epochs=12)  # actual epoch = 4 * 3 = 12

# actual epoch explanation: In file configs/_base_/datasets/voc0712.py line 34 & 35,
# voc uses RepeatDataset ( time=3 ) as default,
# which means 1 epoch equals to 3 epochs
