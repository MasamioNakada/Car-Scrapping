import sys

from get_links import get_links
from process_data import save_csv

if __name__ == "__main__":
    parametro = sys.argv[1]
    link_list = get_links(get_all=parametro)
    save_csv(link_list)
    #SaveData(link_list).save_db()