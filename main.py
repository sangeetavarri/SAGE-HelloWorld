#Hello World Program 
import numpy as np
from waggle.plugin import Plugin
import time

def main():
   with Plugin() as plugin:
      print("Hello World")
      t = time.time()
      plugin.publish("hello_world_printed", t)

if __name__ == "__main__":
    main()
