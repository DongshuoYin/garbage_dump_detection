from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os

# config_file = '../_myconfigs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712_SE.py'
config_file = '../_myconfigs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712_all_layer_SE_with_ClassBalancedDataset_and_low_nms_score_config_and_data_augumentation.py'
# download the checkpoint from model zoo and put it in `checkpoints/`
# url: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
checkpoint_file = '../checkpoint_backup/epoch_48.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

root = './batch_inference_data/'

count = 0
root_path = root
for _, dirs, files in os.walk(root_path):
    for file in files:
        img_path = os.path.join(root_path, file)
        results = inference_detector(model, img_path)
        # when detection result is not empty
        if len(results[0]) != 0:
            # when confidence > 0.3
            for result in results:
                if results[0][0][4] >= 0.3:
                    model.show_result(img_path, results, font_size=8,
                                      out_file=os.path.join(root, 'inference_visualization', file))
                    break
            # show_result_pyplot(model, img_path, results)
