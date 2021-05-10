import os
import json

if __name__ == "__main__":
    print(os.name)
    print([x for x in os.listdir('.') if os.path.isdir(x)])

    print(json.dumps({"aaa": 123, 'vvv': True}))
