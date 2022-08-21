#!/usr/bin/python3

import asyncio
from xml.dom.minidom import parseString
import cv2
import easyocr
import os
import pyautogui
import sys
import subprocess
import time

before_message = ""

class GraReader:
    """
    GraReader は Gravity の音声ルームに表示される文字列を読み上げるクラスです
    __worker メソッドがコアメソッドです
    """

    def __init__(self,
                 interval_sec: float = 0.5,
                 lang_list: list[str] = ['ja', 'en'],
                 # screenshot_range=(left, top, width, height)
                 screenshot_range=(130, 1400, 630, 200)):
        self.interval_sec = interval_sec
        self.lang_list = lang_list
        self.reader = easyocr.Reader(lang_list)
        self.screenshot_range = screenshot_range
        self.target_path = "./assets/test.png"
        self.updated_path = "./assets/test_reverse.png"
        if not os.path.isdir("./assets/"):
            os.mkdir("./assets/")
        print('終了したいときはCtrl-Cを押してください')

    async def run(self):
        while True:
            # fix this(async)
            self.__worker()
            time.sleep(self.interval_sec)

    def __extract_text_from_image(self, target_image_path: str):
        result = self.reader.readtext(target_image_path)
        # return only a text
        try:
            return result[0][1]
        except Exception:
            print("Gravityの音声ルームが正しく開かれていない可能性があります", file=sys.stderr)
            return None

    def __state_is_changed(self, target_path: str, updated_path: str) -> bool:
        img = cv2.imread(target_path)
        reversed_img = cv2.bitwise_not(img)

        # check if the past image is changed
        past_img = cv2.imread(updated_path)
        if past_img is not None:
            diff = reversed_img.astype(int) - past_img.astype(int)
            if diff.max() - diff.min() < 500:
                return False

        cv2.imwrite(updated_path, reversed_img)
        return True
    
    def say(self, text : str):
        global before_message
        try:
            idx = text.index("が音")
            text = text[:idx] + "さん、こんにちは！"
        except:
            # ただのメッセージのはずなので、そのまま読み上げる
            pass

        if before_message == text:
            print('duplicated message', file=sys.stderr)
            return
        
        print(f'read text: {text}')
        before_message = text
        command = ['voicevox-cli', '-speaker=4', '-style=0', text]
        cp = subprocess.run(command)
        return cp

    def __worker(self):
        # take a screenshot to recognize a text
        pyautogui.screenshot(self.target_path, region=self.screenshot_range)

        extracted_text = self.__extract_text_from_image(self.updated_path)
        if extracted_text is None:
            return
        print(f'expected: {extracted_text}')

        # read the text
        self.say(extracted_text)

if __name__ == "__main__":
    GraReader().run()
