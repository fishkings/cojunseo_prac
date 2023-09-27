import pandas as pd

def save(location, cleaness, built_in):
    idx = len(pd.read_csv(r"cojunseo_prac\database.csv"))
    new_df = pd.DataFrame({"location":location,
                           "cleanedss":cleaness,
                           "built_in":built_in}, 
                         index = [idx])
    new_df.to_csv(r"cojunseo_prac\database.csv",mode = "a", header = False)
    return None

def load_list():
    house_list = []
    df = pd.read_csv(r"cojunseo_prac\database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    return house_list

def now_index():
    df = pd.read_csv(r"cojunseo_prac\database.csv")
    return len(df)-1

def load_house(idx):
    df = pd.read_csv(r"cojunseo_prac\database.csv")
    house_info = df.iloc[idx]
    return house_info

if __name__ =="__main__":
    load_list()