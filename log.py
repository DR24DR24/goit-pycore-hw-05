import re
import collections
import sys

messange_dict=collections.defaultdict(list)


def parse_log_line(line: str):# -> dict:
    element_Match =re.search(r"([\-0-9]+)\s([0-9:]+)\s(\w+)\s(.*)",line)
    if not (element_Match==None):
        try:
            messange_dict[element_Match.group(3)].append(\
                {"date":element_Match.group(1),\
                      "time":element_Match.group(2),\
                      "message":element_Match.group(4)\
                      }\
                )
        except:
            messange_dict["CORRUPTED"].append(\
                     {"date":"",\
                      "time":"",\
                      "message":line\
                      }\
            )
     

def load_logs(file_path: str):
    try:
        with open(file_path, "r",encoding='utf-8')  as file:
            for line in file:
                parse_log_line(line)
    except:
        print("error, please check the file")


def filter_logs_by_level(level: str) -> list:
    try:
        return messange_dict[level]
    except:
        print(f"no '{level}' ib log")


def display_logs_by_level(level: str):
    filter_list=filter_logs_by_level("INFO")
    print(f"\nДеталі логів для рівня {level}")
    for item in filter_list:
        print(f"{item["date"]} {item["time"]} - {item["message"]}")
    

def display_log_counts():
    print("Рівень логування | Кількість")
    print("----------------------------")
    for key in messange_dict:
        a=f"{key}                            "
        b=a[:16]+" | "+f"{len(messange_dict[key])}"
        print(b) 




def main():    
    try:
        if len(sys.argv) >1:
            #load_logs("log.txt")
            load_logs(sys.argv[1])
            display_log_counts()
            if len(sys.argv) >2:
                # display_logs_by_level("INFO")
                display_logs_by_level(sys.argv[2].upper())
        else:
            print("please add the file name in command prompt")        
    except:
        print("unknown error")
    print("\n")    

if __name__=="__main__":
    main()

