import os
from dotenv import load_dotenv

load_dotenv()
import sys

def main():
    print(os.getenv('key'))
    if len(sys.argv)>1:
        print(sys.argv[1])
if __name__ == "__main__":
    main()