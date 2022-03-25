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

# test a single image
root = '../../inference_data/beijing19/'
# location = ['fortaleza_Brazil','leipzig_Germany','lucknow_India','nagano_Japan','shantou_China','toronto_Canada','winnipeg_Canada']
# location = ['Antananarivo_Madagascar','Auckland_NewZealand','Ecatepec_Mexico','Latgale_Latvia','Mexicocity_Mexico','Riga_Latvia','Toamasina_Madagascar']
# location = ['lagos_Negeria2','moscow_Russia2','napier_NewZealand2','volgograd_Russia2']
# location = ['moscow_Russia2']
location = ['beijing']
# location = ['bojanala_SouthAfrica2','gaziantep_Turkey2','gulu_Uganda2','istanbul_Turkey2','johannesburg_SouthAfrica2','kampala_Uganda2','lagos_Negeria2','moscow_Russia2','napier_NewZealand2','volgograd_Russia2']
# time = ['16', '17', '18', '15']
time = ['21']
for loc in location:
    for t in time:
        count = 0
        root_path = os.path.join(root, loc, t)
        cutting_path = os.path.join(root_path,'cutting')
        for _, dirs, files in os.walk(cutting_path):
            for file in files:
                img_path = os.path.join(cutting_path, file)
                results = inference_detector(model, img_path)
                # 当检测到目标时
                if len(results[0]) != 0:
                    # 当目标置信度存在大于0.3时
                    for result in results:
                        if results[0][0][4] >= 0.3:
                            model.show_result(img_path, results, font_size=8,
                                              out_file=os.path.join(root, loc, t + '-inference', file))
                            break
                    # show_result_pyplot(model, img_path, results)

# img = 'demo.jpg'
# result = inference_detector(model, img)
#
# # show the results
# show_result_pyplot(model, img, results)


# save
