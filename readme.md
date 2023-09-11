# recursive-image-extension-converter

`source directory` 폴더의 파일을 탐색해 `destination directory`로 복사합니다

탐색중 `webp`, `jpg`, `jpeg` 등의 이미지 파일은 `png`로 변환해 복사합니다

## 변환 대상

`webp`, `jpg`, `jpeg`, `png` -> `png`

`mp4` -> `gif`

## dependency

check `dependency.sh`

## usage

```bash
python convert.py <source-directory> <dest-directory>
```