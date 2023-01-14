from get_links import get_links
from process_data import SaveData

if __name__ == "__main__":
    link_list = get_links(get_all=False)
    SaveData(link_list).save_csv()
    #SaveData(link_list).save_db()