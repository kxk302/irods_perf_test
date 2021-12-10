import time
from functools import partial
from statistics import mean

import argparse

from irods.session import iRODSSession

def client(num_of_times, collection, cache_path, num_rows, num_cols):
  # Create an iRODSSession
  start = time.time()
  session = iRODSSession(host="gs-0.corral.tacc.utexas.edu", port="1247", 
                         user="gtest", password="ArgieB@rgie", 
                         zone="galaxy", refresh_time="300")
  end = time.time()
  print("Time to create an irods session: {}".format(end-start))

  collection_path = "/galaxy/home/gtest/" + collection 
  run_times = []
  CHUNK_SIZE = 2**20

  for idx in range(num_of_times):
    start = time.time()
    data_object_path = collection_path + "/" + num_rows + "_by_" + num_cols + "_" + str(idx) + ".txt"
    full_cache_path = cache_path + "/" + num_rows + "_by_" + num_cols + "_" + str(idx) + ".txt"
    data_obj = session.data_objects.get(data_object_path)
    with data_obj.open('r') as data_obj_fp, open(full_cache_path, "wb") as cache_fp:
      for chunk in iter(partial(data_obj_fp.read, CHUNK_SIZE), b''):
        cache_fp.write(chunk)
    end = time.time()
    run_time = end -start
    run_times.append(run_time)
    print(run_time)
  print("Average runetime after {} calls: {}".format(num_of_times,mean(run_times)))
  session.cleanup()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--num_of_times', help="Number of times to copy file to irods", required=True)
  parser.add_argument('-c', '--collection', help="irods collection to copy the files to", required=True)
  parser.add_argument('-p', '--cache_path', help="Path to which irods files will be saved", required=True)
  parser.add_argument('-r', '--num_rows', help="Number of rows in the input file", required=True)
  parser.add_argument('-l', '--num_cols', help="Number of columsn in the input file", required=True)
  args = vars(parser.parse_args())
  client(int(args['num_of_times']), args['collection'], args['cache_path'], args['num_rows'], args['num_cols'])
