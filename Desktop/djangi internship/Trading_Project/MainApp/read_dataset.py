# importing module
import pandas as pd
import json
def generate_json(file_name,rang):
    start = 0
    ran = rang
    main_lst = []
    # reading CSV file
    data = pd.read_csv(file_name,low_memory=False)
    # print(data.head())
    data = data[['OPEN','HIGH','LOW','CLOSE','DATE']]
    # print(data.head())
    total_rows = len(data)
    # total_rows = 23
    for i in range(0,total_rows,ran):
        t_lst=[]
        if(i==0):
            continue
        # print(data[:][start:i])
        # print(data["CLOSE"][i])
        # print(f"{start} {i}")
        t_lst.append(i)
        t_lst.append(data["OPEN"][start])
        t_lst.append(data["HIGH"][start:i-1].max())
        t_lst.append(data["LOW"][start:i-1].min())
        t_lst.append(data["CLOSE"][i-1])
        t_lst.append(int(data["DATE"][start]))
        main_lst.append(t_lst)
        # print(t_lst)
        start = i

    json_obj = json.dumps(main_lst)
    with open("temp.json",'w') as f:
        f.write(json_obj)


