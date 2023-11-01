from blind_watermark import WaterMark, blind_watermark
import os
from tqdm import tqdm

def get_img_paths(input_folder):
    img_paths = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, file)
            img_paths.append([str(img_path),str(file)])
    return img_paths

def add_waterMark(img_paths,output_folder,wm,password):
    len_wm = -1
    for i in tqdm(range(len(img_paths))):
        abs_path, file_name = img_paths[i]
        out_path = str(os.path.join(output_folder, file_name))
        try:
            bwm1 = WaterMark(password_wm=password, password_img=password)
            # read original image
            bwm1.read_img(abs_path)
            # read watermark
            bwm1.read_wm(wm, mode='str')
            # embed
            bwm1.embed(f'{out_path}')
            len_wm = len(bwm1.wm_bit)
            del bwm1
        except Exception as e:
            print(f"{file_name} 文件注入失败！")
            print(e)

    if(len_wm!=-1):
        print('wm_bit 长度为: {len_wm}'.format(len_wm=len_wm))
    print("已全部完成盲水印注入！")

def main():
    blind_watermark.bw_notes.close()
    input_folder = './input'
    output_folder = './output'
    wm = 'Hade'
    password = 1
    img_paths = get_img_paths(input_folder)
    add_waterMark(img_paths, output_folder, wm, password)

if __name__=="__main__":
    main()