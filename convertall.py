import os, sys
import shutil, re
from PIL import Image
from moviepy.editor import VideoFileClip

class changewd:
    def __init__(self, path):
        self.wdprevious = os.getcwd()
        self.wdchanged = path
    def __enter__(self):
        os.chdir(self.wdchanged)
    def __exit__(self, type, value, traceback):
        os.chdir(self.wdprevious)

def mkdir_recursive(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

def get_relative_path(path:str, basepath:str):
    pathdir = path.replace("/","\\")
    length = len(basepath.replace("/","\\"))
    return pathdir[length+1:]

re_targetext_img = re.compile(R".*[.](webp|jpg|jpeg|png)$")
re_targetext_video = re.compile(R".*[.](mp4)$")
def convert(filename:str, srcdir:str, dstdir:str):
    if re_targetext_img.match(filename):
        renamed = re.sub(R"[.](webp|jpg|jpeg|png)$",".png",filename)
        src = f"{srcdir}\\{filename}"
        dst = f"{dstdir}\\{renamed}"
        
        img = Image.open(src)
        img.save(dst, 'png', save_all=True)
    elif re_targetext_video.match(filename):
        renamed = re.sub(R"[.](mp4)$",".gif",filename)
        dst = f"{dstdir}\\{renamed}"

        with changewd(srcdir):
            video = VideoFileClip(filename)
            video.write_gif(dst)
    else:
        src = f"{srcdir}\\{filename}"
        dst = f"{dstdir}\\{filename}"
        shutil.copy2(src, dst)

if __name__ == "__main__":
    try:
        beforedir = os.path.abspath(sys.argv[1])
        afterdir = os.path.abspath(sys.argv[2])

        if not os.path.exists(beforedir):
            print(f"Invalid path : '{beforedir}'")
            exit()
        elif not os.path.exists(afterdir):
            print(f"Invalid path : '{afterdir}'")
            exit()
    except IndexError:
        print("Invalid arguments")
        exit()

    for path, dirs, files in os.walk(beforedir):
        rpath = get_relative_path(path, beforedir)

        srcdir = f"{beforedir}\\{rpath}"
        dstdir = f"{afterdir}\\{rpath}"
        mkdir_recursive(dstdir)

        for filename in files:
            convert(filename, srcdir, dstdir)