from bluevision.demo import video_demo

video_demo(
    weights="/mnt/c/Users/tokio/Downloads/yolov8n-coco.safetensors",
    video_path="/mnt/c/Users/tokio/Downloads/mot17.mp4",
    model_size="n",
    track=True,
    show=True,
    save_path="./output.mp4",
)