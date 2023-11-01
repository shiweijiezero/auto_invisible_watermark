from PIL import Image, ImageDraw, ImageFont, ImageChops
import os
from tqdm import tqdm

# 创建Font对象,设定字体大小
font = ImageFont.truetype('arial.ttf', 36)

def get_img_paths(input_folder):
    img_paths = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, file)
            img_paths.append([str(img_path),str(file)])
    return img_paths

def add_waterMark(img_paths,output_folder,wm,password):
    text = wm

    for i in tqdm(range(len(img_paths))):
        # -
        abs_path, file_name = img_paths[i]
        out_file_name = ".".join(file_name.split(".")[:-1])+".png"
        print(out_file_name)
        out_path = str(os.path.join(output_folder, out_file_name))

        # try:
        original_img = Image.open(abs_path).convert('RGBA')

        font = ImageFont.truetype('arial.ttf', 36)
        watermark = Image.new('RGBA', original_img.size, (0, 0, 0,0))
        draw = ImageDraw.Draw(watermark)
        draw.text((10, 10), text, font=font)
        # watermarked_img = Image.alpha_composite(original_img,watermark)
        watermarked_img = Image.blend(original_img,watermark,alpha=0.01)
        # watermarked_img = watermarked_img.convert('RGB')

        watermarked_img.save(out_path)
        # except Exception as e:
        #     print(f"{file_name} 文件注入失败！")
        #     print(e)

    print("已全部完成盲水印注入！")

def main():
    input_folder = './input'
    output_folder = './output_PIL'
    wm = 'Hade Hade Hade Hade Hade Hade'
    password = 1
    img_paths = get_img_paths(input_folder)
    add_waterMark(img_paths, output_folder, wm, password)

if __name__=="__main__":
    main()