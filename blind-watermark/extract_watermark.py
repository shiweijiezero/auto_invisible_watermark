from blind_watermark import WaterMark, blind_watermark
import os
from tqdm import tqdm
from pprint import pprint

def get_img_paths(input_folder):
    img_paths = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, file)
            img_paths.append([str(img_path),str(file)])
    return img_paths

def detect_waterMark(img_paths,wm,password,len_wm):
    res = []
    for i in tqdm(range(len(img_paths))):
        abs_path, file_name = img_paths[i]
        try:
            bwm1 = WaterMark(password_wm=password, password_img=password)
            # notice that wm_shape is necessary
            wm_extract = bwm1.extract(abs_path, wm_shape=len_wm, mode='str')
            print(f"{file_name}的水印抽取结果为:{wm_extract}")
            if(wm_extract==wm):
                res.append(file_name)
            del bwm1
        except Exception as e:
            print(f"{file_name} 水印抽取失败！")
            print(e)

    print("已全部完成盲水印抽取！")
    print("其中具有盲水印的图片为")
    pprint(res)


def main():
    blind_watermark.bw_notes.close()
    input_folder = './test_picture_director'
    wm = 'Hade'
    len_wm = 31
    password = 1
    img_paths = get_img_paths(input_folder)
    detect_waterMark(img_paths, wm, password,len_wm)

if __name__=="__main__":
    main()