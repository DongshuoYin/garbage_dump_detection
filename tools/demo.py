
from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os

# This demo is for single image inference
config_file = '../_myconfigs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712_all_layer_SE_with_ClassBalancedDataset_and_low_nms_score_config_and_data_augumentation.py'
checkpoint_file = '../checkpoint_backup/epoch_48.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image
img = 'demo.jpg'
result = inference_detector(model, img)

# show the results
show_result_pyplot(model, img, result)

# save
model.show_result(img, result, font_size=16, out_file='demo_visualization.jpg')
