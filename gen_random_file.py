import argparse
import random
import string

def gen_random_file(num_rows, num_cols, file_name):
    print("Number of rows: {}".format(num_rows))
    print("Number of columns: {}".format(num_cols))
    print("File name: {}".format(file_name))

    with open(file_name, "w") as fp:
        for i in range(num_rows):
            # Write (num_cols-1) random characters and a new line, for a totla of num_cols characters
            line = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(num_cols-1))
            line += "\n" 
            fp.write(line)            
                              
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_rows", help="Number of rows in the generated file", type=int, required=True)
    parser.add_argument("--num_cols", help="Number of columns in the generated file", type=int, required=True)
    parser.add_argument("--file_name", help="Name of the generated file", type=str, required=True)
    args = parser.parse_args()
    gen_random_file(num_rows=args.num_rows, num_cols=args.num_cols, file_name=args.file_name)


