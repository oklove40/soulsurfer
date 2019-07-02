# pip install pillow
# pip install pytesseract

# import Setting

# _config = Setting.Config("property.ini", debug=True)

# print('OriImgPath', _config.Path.OriImgPath)
# print('OcrTxtPath', _config.Path.OcrTxtPath)

from PIL import Image       # pip install pillow
from pytesseract import *   # pip install pytesseract
import configparser
import os

# config parser 초기화
config = configparser.ConfigParser()

# config File 읽기
config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')

# print('config : ', config)

# 이미지 -> 문자열 추출
def OcrToTxt(fullPath, outTxtPath, fileName, lang='eng'):
    # 기본은 영어로 추출
    # print('OcrToImg : ', fullPath, outTxtPath, fileName, lang)

    # 이미지 경로
    img = Image.open(fullPath)
    # 저장할 파일명
    txtName = os.path.join(outTxtPath, fileName.split('.')[0])

    # print('이미지 : ', img)
    # print(img.format)
    # print(img.format_description)
    # print(img.height)
    # print(img.width)
    # print(img.mode)
    # print(img.size)

    # 변환될 파일명 - txt
    # preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인한다
    # psm(페이지 세그먼트 모드 : 이미지 영역안에서 텍스트 추출 범위 모드)
    outText = image_to_string(img, lang=lang, config=' -c preserve_interword_spaces=1') # --psm 2

    print('+++ OCR Extract Result +++')
    print('Extract Filename ->> ', fileName, '<<-')
    print('\n\n')
    
    # 추출한 결과를 파일로 생성
    strToTxt(txtName, outText)


# 문자열 -> 텍스트파일 개별 저장
def strToTxt(txtName, outText):
    with open(txtName + '.txt', 'w', encoding='utf-8') as f:
        f.write(outText)

# 메인 시작
if __name__ == "__main__":
    print('main')

    imgType = "etc"

    # 텍스트파일 저장 경로
    outTxtPath = os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath'] + os.sep + imgType

    # print('OriImgPath : ', os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath'] + os.sep + imgType)
    # print('OcrTxtPath : ', os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath'] + os.sep + imgType)

    # OCR 추출 작업 메인
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath'] + os.sep + imgType):
        for fname in files:
            fullName = os.path.join(root, fname)
            OcrToTxt(fullName, outTxtPath, fname, 'kor')

