import re
if __name__ == '__main__':
    s = input()
    if re.search(".*[a-zA-Z]+.*",s):
        print('match')
        
    