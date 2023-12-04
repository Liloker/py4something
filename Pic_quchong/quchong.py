from PIL import Image
import imagehash
import os
from collections import defaultdict
import shutil


def get_image_hash(image_path):
    try:
        image = Image.open(image_path)
        return imagehash.average_hash(image)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None


def find_duplicates(image_folder):
    hash_dict = defaultdict(list)

    for root, dirs, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(root, file)
                image_hash = get_image_hash(file_path)
                if image_hash is not None:
                    hash_dict[image_hash].append(file_path)

    duplicates = [files for files in hash_dict.values() if len(files) > 1]

    return duplicates


def move_truncated_files(image_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)

    for root, dirs, files in os.walk(image_folder):
        for file in files:
            file_path = os.path.join(root, file)
            image_hash = get_image_hash(file_path)
            if image_hash is None:
                # 图片无法处理，移动到目标文件夹
                destination_path = os.path.join(destination_folder, file)
                shutil.move(file_path, destination_path)
                print(f"Truncated file moved to: {destination_path}")


def main():
    image_folder = r"E:\url-save\Api_Pic"
    destination_folder = r"E:\url-save\truncated_images"

    # 移动无法处理的图片
    move_truncated_files(image_folder, destination_folder)

    # 查找并处理重复图片
    duplicates = find_duplicates(image_folder)

    if duplicates:
        print("Duplicate images found:")
        for group in duplicates:
            print(group)
            # 保留一张，删除其他
            for file in group[1:]:
                os.remove(file)
                print(f"Duplicate file removed: {file}")
        print("Duplicates removed.")
    else:
        print("No duplicate images found.")


if __name__ == "__main__":
    main()
