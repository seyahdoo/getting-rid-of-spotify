

import ZODB, ZODB.FileStorage
import os
import multiprocessing.dummy as mp


storage = ZODB.FileStorage.FileStorage('data.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root


input_path = "C:\\Users\\seyahdoo\\Music\\Other"
output_path = "C:\\CODE_SEGMANT\\GettingRidOfSpotify\\flaccer\\o2"


def process_filename(filename):
    input_file_path = os.path.join(input_path, filename)
    print(input_file_path)
    output_file_path = os.path.join(output_path, filename.replace(".mp4", ".mp3"))

    if os.path.exists(output_file_path):
        return

    cmd = "ffmpeg -i \"{}\" -vn \"{}\"".format(input_file_path, output_file_path)
    print(cmd)
    os.system(cmd)


p=mp.Pool(7)
p.map(process_filename, os.listdir(input_path))
p.close()
p.join()


