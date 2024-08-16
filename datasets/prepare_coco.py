import wget
import zipfile


def download_file(url, destination):
    wget.download(url, destination)
    print(f'\nDownload completed: {destination}')


def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f'Extraction completed: {extract_path}')


# Settings (COCO Dataset)
# 'http://images.cocodataset.org/zips/train2017.zip' - done

urls = ['http://images.cocodataset.org/zips/val2017.zip',
        'http://images.cocodataset.org/zips/test2017.zip',
        'http://images.cocodataset.org/annotations/annotations_trainval2017.zip']

destinations = ['datasets/coco/zip/val2017.zip',
                'datasets/coco/zip/test2017.zip',
                'datasets/coco/zip/annot2017.zip']

zip_paths = ['datasets/coco/zip/val2017.zip',
             'datasets/coco/zip/test2017.zip',
             'datasets/coco/zip/annot2017.zip'
             ]

extract_paths = ['datasets/coco/',
                 'datasets/coco/',
                 'datasets/coco/']

for i in range(3):
    download_file(urls[i], destinations[i])
    extract_zip(zip_paths[i], extract_paths[i])
