import re
if __name__ == '__main__':
    s = input()
    print(bool(re.search(".*[a-zA-Z0-9]+.*",s))) #alphanumeric
    print(bool(re.search(".*[a-zA-Z]+.*",s))) #alphabetical
    print(bool(re.search(".*[0-9]+.*",s))) #digits
    print(bool(re.search(".*[a-z]+.*",s))) #lowercase
    print(bool(re.search(".*[A-Z]+.*",s))) #uppercase
    
        
    