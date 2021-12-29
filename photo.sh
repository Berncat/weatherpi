#!/bin/bash
fswebcam -r 640x360 --no-banner image.jpg
python3 tcp_client.py