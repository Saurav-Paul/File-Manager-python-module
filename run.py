from commands.file_arranger import file_arranger
import argparse

arrange_keys = ['ar' , 'arrange']
def start():
    pass
    
    parser = argparse.ArgumentParser(description='Manage your files.')
    parser.add_argument('action',help='Enter you action')
    arg = parser.parse_args()
    print(arg.action)
    action = arg.action

    if action in arrange_keys:
        file_arranger()

if __name__ == "__main__":
    start()