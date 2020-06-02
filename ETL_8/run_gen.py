from gen_image import gen8B, gen8G

folderpathB = r'/Users/taanhtuan/Desktop/ETL8/Data/compressed_data/ETL8B/*'
folderpathG = r'/Users/taanhtuan/Desktop/ETL8/Data/compressed_data/ETL8G/*'
save_path = r"/Users/taanhtuan/Desktop/ETL8/Data/data_gen/"
csv_path = r"/Users/taanhtuan/Desktop/ETL8/Data/csv_folder/ETL8_label.csv"
save_label_path = r"/Users/taanhtuan/Desktop/ETL8/Data/label_image"
csv_label_path = r"/Users/taanhtuan/Desktop/ETL8/Data/csv_folder/ETL8_label_map.csv"

if __name__ == "__main__":
    gen8G.read_folder(save_path,folderpathG,csv_path,save_label_path,csv_label_path)
    gen8B.read_folder(save_path,folderpathB,csv_path,save_label_path,csv_label_path)

