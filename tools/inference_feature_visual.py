from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os

config_file = '../_myconfigs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712_all_layer_SE_with_ClassBalancedDataset_and_low_nms_score_config_and_data_augumentation.py'
# download the checkpoint from model zoo and put it in `checkpoints/`
# url: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
checkpoint_file = './work_dirs/faster_rcnn_r50_fpn_1x_voc0712_all_layer_SE_with_ClassBalancedDataset_and_low_nms_s' \
                  'core_config_and_data_augumentation/epoch_24.pth'
# checkpoint_file = './work_dirs/faster_rcnn_r50_fpn_1x_voc0712/epoch_12.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image
# change line48 of feature_visualization.py like the under line
img = '5309.jpg'
results = inference_detector(model, img)

# show the results
show_result_pyplot(model, img, results)

# save
