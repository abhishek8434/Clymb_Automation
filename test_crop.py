#!/usr/bin/env python3
"""
Simple test harness for crop_browser_ui() using a dummy driver and image.
"""
import os
from PIL import Image
from tests.shopify import crop_browser_ui

class DummyDriver:
    def __init__(self, platform):
        self.capabilities = {'platformName': platform}

    def execute_script(self, script):
        if 'getBoundingClientRect' in script:
            return 50
        if 'window.innerHeight' in script:
            return 700
        if 'querySelector' in script:
            return 100
        return 0

def make_dummy_image(path, size=(400, 800), color=(100, 150, 200)):
    img = Image.new('RGB', size, color=color)
    img.save(path)

def test_crop(platform_label, platform_key):
    img_path = f"dummy_{platform_label}.png"
    make_dummy_image(img_path)
    driver = DummyDriver(platform_key)
    crop_browser_ui(img_path, driver)
    cropped = Image.open(img_path)
    print(f"Platform={platform_label}: original=(400,800) cropped={cropped.size}")
    os.remove(img_path)

if __name__ == '__main__':
    test_crop('iOS', 'iOS')
    test_crop('Android', 'Android')