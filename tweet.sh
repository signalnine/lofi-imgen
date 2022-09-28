#!/bin/bash

CONTAINER=$(/snap/bin/docker ps | grep miniconda | awk '{print $1}')
/snap/bin/docker exec -i $CONTAINER /sd/run.sh
IMAGE="$(ls /home/gabe/stable-diffusion/outputs/*.png -t | head -n1)"
/home/gabe/realesrgan/realesrgan-ncnn-vulkan -i "$IMAGE" -o /tmp/upscaled.png
python3 /home/gabe/lofi-imgen/tweet.py /tmp/upscaled.png
