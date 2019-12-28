import os
back = os.path.dirname
BASE_DIR = back(back(back(os.path.abspath(__file__))))
print(BASE_DIR)
