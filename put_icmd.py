import random
import string
import subprocess
import time
from statistics import mean

import argparse

def iput(folder_name, num_of_times, collection, num_rows, num_cols):
  # First, create the collection (folder) 
  subprocess.call(['/usr/bin/imkdir', collection])

  # Next, generate a random file and add it to the collection number_of_times
  # And measure the runtime
  run_times = []
  data_object_path = "/galaxy/home/gtest/" + collection + "/"
  for idx in range(num_of_times):
    file_name = num_rows + "_by_" + num_cols + "_" + str(idx) + ".txt"
    file_path = folder_name + "/" + file_name
    # gen_random_file(int(num_rows), int(num_cols), file_path)
    start = time.time()
    subprocess.call(['/usr/bin/iput', file_path, data_object_path + file_name])
    end = time.time()
    run_time = end -start
    run_times.append(run_time)
    print(run_time)
  print("Average runtime after {} calls: {}".format(num_of_times,mean(run_times)))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--folder_name', help="Name of the folder to generate the random files in", required=True)
  parser.add_argument('-n', '--num_of_times', help="Number of times to copy file to irods", required=True)
  parser.add_argument('-c', '--collection', help="irods collection to copy the files to", required=True)
  parser.add_argument('-r', '--num_rows', help="Number of rows in the input file", required=True)
  parser.add_argument('-l', '--num_cols', help="Number of columsn in the input file", required=True)
  args = vars(parser.parse_args())
  iput(args['folder_name'], int(args['num_of_times']), args['collection'], args['num_rows'], args['num_cols'])
