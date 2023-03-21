import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
sys.path.append(os.path.join(current_path, "lib"))
print('\n')
print(__path__)