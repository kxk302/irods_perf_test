import subprocess
import time
from statistics import mean

import argparse

def iget(num_of_times, collection, cache_path, num_rows, num_cols):

  run_times = []
  data_object_path = "/galaxy/home/gtest/" + collection + "/"
  for idx in range(num_of_times):
    start = time.time()
    subprocess.call(['/usr/bin/iget', data_object_path + num_rows + "_by_" + num_cols + "_" + str(idx) + ".txt", cache_path])
    end = time.time()
    run_time = end -start
    run_times.append(run_time)
    print(run_time)
  print("Average runtime after {} calls: {}".format(num_of_times,mean(run_times)))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--num_of_times', help="Number of times to copy file to irods", required=True)
  parser.add_argument('-c', '--collection', help="irods collection to copy the files to", required=True)
  parser.add_argument('-p', '--cache_path', help="Path to which irods files will be saved", required=True)
  parser.add_argument('-r', '--num_rows', help="Number of rows in the input file", required=True)
  parser.add_argument('-l', '--num_cols', help="Number of columsn in the input file", required=True)
  args = vars(parser.parse_args())
  iget(int(args['num_of_times']), args['collection'], args['cache_path'], args['num_rows'], args['num_cols']) 
