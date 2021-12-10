# Compare icommands with Python client for put/get

## Configure your environment

Create a virtual environment via ```python3 -m venv venv```

Activate the virtual environment via ```. ./venv/bin/activate```

Configure the virtual environment via ```pip3 install -r requirements.txt```

## Generate files with random content

Create folders for each file size via ```mkdir 100B 10KB 1MB 4MB 6.25MB 25MB 50MB 100MB 1GB``` 

For each file size, select the appropriate number of rows and columns, such that their product equals the desired file size 

Generate a random file of size 100 bytes (10 rows X 10 columns) via \
```python3 gen_random_file.py --num_rows 10 --num_cols 10 --file_name 100B/10_by_10_1.txt```

Generate a random file of size 100MB (10,000 rows X 10,000 columns) via \
```python3 gen_random_file.py --num_rows 10000 --num_cols 10000 --file_name 100MB/10000_by_10000_1.txt```

For each file size, run these commands, say 50 times, to create 50 files of that size (Can write a simple loop that calls gen_random_file.py for this). For example, in 100B folder, you will create files named 10_by_10_1.txt through 10_by_10_50.txt.

## Run put scripts

Run Python client's put script for a specific file size, e.g. 100 bytes, via \
```put_client.py -f 100B -n 50 -c 100B -r 10 -l 10```

This runs Python client's put command 50 times, once for each file in 100B folder. Files are added to 100B collection.

Run icommand's put script for a specific file size, e.g. 100MB bytes, via \
```put_icmd.py -f 100MB -n 50 -c 100MB -r 10000 -l 10000```

This runs icommand's put command 50 times, once for each file in 100MB folder. Files are added to 100MB collection.

## Run get scripts

Create get folders for each file size via ```mkdir 100B_get 10KB_get 1MB_get 4MB_get 6.25MB_get 25MB_get 50MB_get 100MB_get 1GB_get```

Run Python client's get script for a specific file size, e.g. 100 bytes, via \
```get_client.py -p 100B_get -n 50 -c 100B -r 10 -l 10```

This runs Python client's get command 50 times, once for each file in 100B collection. Files are added to 100B_get folder.

Run icommand's gett script for a specific file size, e.g. 100MB bytes, via \
```get_icmd.py -p 100MB_get -n 50 -c 100MB -r 10000 -l 10000```

This runs icommand's get command 50 times, once for each file in 100MB collection. Files are added to 100MB_get folder.

