from get_links import get_links
from process_data import save_csv,save_db

if __name__ == "__main__":
    link_list = get_links(get_all=True)
    save_csv(link_list)
    save_db(link_list)