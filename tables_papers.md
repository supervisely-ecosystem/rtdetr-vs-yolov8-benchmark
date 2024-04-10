YOLOv6 v3.0 (2023)
https://github.com/meituan/YOLOv6, https://arxiv.org/pdf/2301.05586.pdf
FPS = T4 TRT fp16
Model       Size    mAP     FPS -   Params  FLOPs   T4(ms)
YOLOv6-S	640	    45.0	339	484	18.5	45.3    2.9
YOLOv6-M	640	    50.0	175	226	34.9	85.8    5.7
YOLOv6-L	640	    52.8	98	116	59.6	150.7   10.2

YOLOv8 from:
https://arxiv.org/pdf/2301.05586.pdf
T4 TRT fp16
Model       Size mAP    FPS T4(TRT) Params  FLOPs
YOLOv8-S    640  44.9   311 3.2 ms  11.2 M  28.6 G
YOLOv8-M    640  50.2   143 7.0 ms  25.9 M  78.9 G
YOLOv8-L    640  52.9   91  11.0 ms 43.7 M  165.2 G

YOLOv8 (2023)
https://github.com/ultralytics/ultralytics
            mAP     CPU ONNX,A100TRT,Params FLOPs 
YOLOv8s	640	44.9	128.4	1.20	11.2	28.6
YOLOv8m	640	50.2	234.7	1.83	25.9	78.9
YOLOv8l	640	52.9	375.2	2.39	43.7	165.2
YOLOv8x	640	53.9	479.1	3.53	68.2	257.8

YOLOv5 r6.1 (2022)
https://github.com/ultralytics/yolov5/releases/tag/v6.1
            mAP     CPU V100    Params  FLOPs
YOLOv5m	640	45.4	224	8.2	    21.2	49.0
YOLOv5l	640	49.0	430	10.1	46.5	109.1
YOLOv5x	640	50.7	766	12.1	86.7	205.7

YOLOv5 r5.0 (2021)
https://github.com/ultralytics/yolov5/releases/tag/v5.0
            mAP     V100    Params  FLOPs
YOLOv5m	640	44.5	2.7		21.4	51.3
YOLOv5l	640	48.2	3.8		47.0	115.4
YOLOv5x	640	50.4	6.1		87.7	218.8


RT-DETR
https://github.com/lyuwenyu/RT-DETR/tree/main/rtdetr_pytorch
pdf: https://arxiv.org/pdf/2304.08069.pdf
FPS = T4, TRT fp16
Model	            mAP	    Params  FPS ms      FLOPs
rtdetr_r18vd	640	46.4    20	    217 4.6     
rtdetr_r34vd	640	48.9    31	    161 6.2     
rtdetr_r50vd_m	640	51.3    36	    145 6.9     
rtdetr_r50vd	640	53.1    42	    108 9.3     136
rtdetr_r101vd	640	54.3    76	    74  13.5    259


v7: 51.2/9.0 (5.68)
v6_3.0: 52.8/10.3 (5.31) OR 50/5.7 (8.77)