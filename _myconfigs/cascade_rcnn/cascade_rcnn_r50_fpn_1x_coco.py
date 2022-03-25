_base_ = [
    '../_base_/models/cascade_rcnn_r50_fpn.py',
    # '../_base_/datasets/cascade_rcnn/cascade_rcnn_r50_fpn_1x_coco.py',
    '../_base_/datasets/voc0712.py',
    # '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
