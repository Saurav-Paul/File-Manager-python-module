from commands.file_arranger import file_arranger, r_e_f
import argparse , os

arrange_keys = ['ar' , 'arrange']
remove_empty_folder_keys = ['remove_empty_folder','ref']
def start():
    
    parser = argparse.ArgumentParser(description='Manage your files.')
    parser.add_argument('action',help='Enter you action')
    arg = parser.parse_args()
    action = arg.action

    if action in arrange_keys:
        file_arranger()
    if action in remove_empty_folder_keys:
        r_e_f(os.getcwd())
    else:
        print("wrong")

if __name__ == "__main__":
    start()