import random
import string
import subprocess
import time
from statistics import mean

import argparse

from irods.session import iRODSSession

def client(folder_name, num_of_times, collection, num_rows, num_cols):
  # Create an iRODSSession
  start = time.time()
  session = iRODSSession(host="gs-0.corral.tacc.utexas.edu", port="1247", 
                         user="gtest", password="ArgieB@rgie", 
                         zone="galaxy", refresh_time="300")
  end = time.time()
  print("Time to create an irods session: {}".format(end-start))

  # Create the collection
  start = time.time()
  collection_path = "/galaxy/home/gtest/" + collection 
  session.collections.create(collection_path, recurse=True)
  end = time.time()
  print("Time to create a collection: {}".format(end-start))

  run_times = []
  options = {'forceFlag':''}
  for idx in range(num_of_times):
    file_name = num_rows + "_by_" + num_cols + "_" + str(idx) + ".txt"
    file_path = folder_name + "/" + file_name
    # gen_random_file(int(num_rows), int(num_cols), file_path)
    start = time.time()
    data_object_path = collection_path + "/" + file_name
    #session.data_objects.create(data_object_path, "corralResc", **options)
    session.data_objects.put(file_path, data_object_path, **options)
    end = time.time()
    run_time = end - start
    run_times.append(run_time)
    print(run_time)
  print("Average runetime after {} calls: {}".format(num_of_times,mean(run_times)))
  session.cleanup()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--folder_name', help="Name of the folder to generate the random files in", required=True)
  parser.add_argument('-n', '--num_of_times', help="Number of times to copy file to irods", required=True)
  parser.add_argument('-c', '--collection', help="irods collection to copy the files to", required=True)
  parser.add_argument('-r', '--num_rows', help="Number of rows in the input file", required=True)
  parser.add_argument('-l', '--num_cols', help="Number of columsn in the input file", required=True)
  args = vars(parser.parse_args())
  client(args['folder_name'], int(args['num_of_times']), args['collection'], args['num_rows'], args['num_cols'])
