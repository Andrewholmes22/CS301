import time
import csv
import pandas as pd


def add_row_csv(n, elapsed_time, operation):
    df_temp = pd.DataFrame([[n, elapsed_time, operation]], columns=['Size of n', 'Time', 'Operation'])
    return df_temp
# def add_row_csv(n, elapsed_time, operation):
#     with open('./dict.csv', mode='a', newline='') as data_file:
#         csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    
#         with open('./dict.csv', mode='r') as csv_file:
#             csv_reader = csv.reader(csv_file)
#             has_content = any(csv_reader)

#             if not has_content:
#                 csv_writer.writerow(['Size of n', 'Time', 'Operation'])
            
#             csv_writer.writerow([n, elapsed_time, operation])

# Analysis of element insertion (2 points) -- determine big O notation for this
def insert_dict(n):
    runtime_dict = {}
    start_time = time.time()    
    
    # for i in range(n):
    #     runtime_dict[i] = i + 1
    runtime_dict[50] = 50
        
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    
    return elapsed_time

#Analysis of element deletion (2 points) -- determine big O notation for this
def delete_dict(n):
    runtime_dict = {}
    
    # print(runtime_dict)
    
    # for i in range(n):
    #     runtime_dict[i] = i + 1
    runtime_dict[50] = 50
    
    start_time = time.time()
    runtime_dict.clear()
    stop_time = time.time()
    elapsed_time = stop_time - start_time
        
    return elapsed_time

#Analysis of element access and search (3 points) -- determine big O notation for this
def access_dict(n):
    runtime_dict = {}
    for i in range(n):
        runtime_dict[i] = i*2
    # for i in range(n):
    #     print(runtime_dict[i])
    # return runtime_dict
    start_time = time.time()
    for i in range(n):
        runtime_dict.get(i)
    stop_time = time.time()
    elapsed_time = stop_time - start_time
        
    return elapsed_time

#Conclusion of possible dictionary data structure based on evidence (3 points)
main_df = pd.DataFrame([], columns=['Size of n', 'Time', 'Operation'])

num_runs = 10
size_of_dict = [i for i in range(0, 1000001, 1000)]

for _ in range(num_runs):
    for size in size_of_dict:
        elapsed_time = insert_dict(size)
        print(elapsed_time)
        insert_df = add_row_csv(size, elapsed_time, "insert")
        main_df = pd.concat([main_df, insert_df])
        elapsed_time = delete_dict(size)
        print(elapsed_time)
        delete_df = add_row_csv(size, elapsed_time, "delete")
        main_df = pd.concat([main_df, delete_df])
        elapsed_time = access_dict(size)
        print(elapsed_time)
        access_df = add_row_csv(size, elapsed_time, "access")
        main_df = pd.concat([main_df, access_df])

main_df.to_csv('./data_frame.csv', quotechar='"', index=False, quoting=1, float_format='%.015f')
