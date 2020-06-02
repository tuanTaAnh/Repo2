import struct
from PIL import Image
import glob
from gen_csv.gen_csv import add_row, write_csv
import shutil, os


def read_record_ETL8B2(f):
    s = f.read(512)
    r = struct.unpack('>2H4s504s', s)
    i1 = Image.frombytes('1', (64, 63), r[3], 'raw')
    return r + (i1,)


def read_file(row_list, label_images, filepath,save_path):
    id_record = 0

    print(filepath)

    while (True):
        try:
            id_record += 1
            with open(filepath, 'rb') as f:
                f.seek((id_record + 1) * 512)
                r = read_record_ETL8B2(f)

            filename = filepath.split("/")[-1]

            iI = Image.eval(r[-1], lambda x: not x)
            fn = '{:s}_{:d}.png'.format(filename, id_record)
            iI.save(save_path + fn, 'PNG')
            print(fn)
            label_images[r[2]] = fn

            row_list = add_row(row_list, (save_path + fn).split("Desktop/")[-1], r[2])
        except Exception as e:
            print(e)
            break


def read_folder(save_path,folderpath,csv_path,save_label_path,csv_label_path):
    row_list = []
    row_label_list = []
    label_images = {}

    for filepath in glob.glob(folderpath):
        if "INFO" not in filepath:
            read_file(row_list, label_images,filepath, save_path)

    write_csv(csv_path,row_list)

    for key in label_images.keys():
        print(key," ", label_images[key])
        row_label_list = add_row(row_label_list,label_images[key],key)
        shutil.copy(save_path + label_images[key], save_label_path)

    write_csv(csv_label_path, row_label_list)

