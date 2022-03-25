from .darknet import Darknet
from .detectors_resnet import DetectoRS_ResNet
from .detectors_resnext import DetectoRS_ResNeXt
from .hourglass import HourglassNet
from .hrnet import HRNet
from .regnet import RegNet
from .res2net import Res2Net
from .resnest import ResNeSt
from .resnet import ResNet, ResNetV1d
from .resnext import ResNeXt
from .ssd_vgg import SSDVGG
from .trident_resnet import TridentResNet
from .resnet_with_attention import ResNet_CBAM
from .resnet_SE import ResNet_SE
from .resnet_resSE import ResNet_resSE
from .res2net_SE import Res2Net_SE
from .resnet_SE_add_RGB_channel import ResNet_SE_add_RGB_channel
from .resnet_SE_enhanced import ResNet_SE_enhanced
from .resnet_all_layer_SE import ResNet_all_layer_SE

# __all__ = [
#     'RegNet', 'ResNet', 'ResNetV1d', 'ResNeXt', 'SSDVGG', 'HRNet', 'Res2Net',
#     'HourglassNet', 'DetectoRS_ResNet', 'DetectoRS_ResNeXt', 'Darknet',
#     'ResNeSt', 'TridentResNet'
# ]
__all__ = [
    'RegNet', 'ResNet', 'ResNetV1d', 'ResNeXt', 'SSDVGG', 'HRNet', 'Res2Net',
    'HourglassNet', 'DetectoRS_ResNet', 'DetectoRS_ResNeXt', 'Darknet',
    'ResNeSt', 'TridentResNet', 'ResNet_CBAM', 'ResNet_SE', 'ResNet_resSE', 'Res2Net_SE',
    'ResNet_SE_add_RGB_channel', 'ResNet_SE_enhanced', 'ResNet_all_layer_SE'
]
