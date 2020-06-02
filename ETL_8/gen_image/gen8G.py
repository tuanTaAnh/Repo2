import struct
from PIL import Image
import glob
from gen_csv.gen_csv import add_row, write_csv
import shutil, os


def read_record_ETL8G(f,sz_record):
    s = f.read(8199)
    r = struct.unpack('>2H8sI4B4H2B30x8128s11x', s)
    iF = Image.frombytes('F', (128, 127), r[14], 'bit', 4)
    iL = iF.convert('RGB')
    return r + (iL,)


def read_file(row_list, label_images, filepath,save_path,save_label_path):
    id_record = 0

    print(filepath)

    while(True):
        try:
            id_record += 1
            with open(filepath, 'rb') as f:
                f.seek(id_record * 8199)
                r = read_record_ETL8G(f, 8199)

            filename = filepath.split("/")[-1]

            iE = Image.eval(r[-1], lambda x: 255 - x * 16)
            fn = '{:s}_{:d}.png'.format(filename, id_record)
            iE.save(save_path + fn, 'PNG')
            print(save_path + fn)
            label_images[r[2]] = fn

            row_list = add_row(row_list, (save_path + fn).split("Desktop/")[-1], r[2])
        except Exception as e:
            print(e)
            break

    print("end")


def read_folder(save_path,folderpath,csv_path,save_label_path,csv_label_path):
    row_list = []
    row_label_list = []
    label_images = {}

    for filepath in glob.glob(folderpath):
        if "INFO" not in filepath:
            read_file(row_list, label_images, filepath, save_path,save_label_path)

    write_csv(csv_path,row_list)

    for key in label_images.keys():
        print(key, " ", label_images[key])
        row_label_list = add_row(row_label_list, label_images[key], key)
        shutil.copy(save_path + label_images[key], save_label_path)


    write_csv(csv_label_path, row_label_list)



