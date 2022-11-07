import torch



if __name__ == '__main__':

    # 模型
    model = torch.hub.load(r'.', 'yolov5s',source="local")  # or yolov5n - yolov5x6, custom

    # 图像
    img = './data/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

    # 推理
    results = model(img)

    # 结果
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
    results.show()