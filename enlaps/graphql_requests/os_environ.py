import os

# os.environ['KEY_1'] = 'super_key'

for key, value in dict(os.environ).items():
    print(key, value)

# print(os.environ['KEY_1'])