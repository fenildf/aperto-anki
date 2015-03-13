import os

TOKEN=os.getenv("TOKEN")

if TOKEN is None:
    raise Exception("Please set the environment variable TOKEN.")

DEVICE_ID="0f637589-6fea-47b8-867f-bbab4aafcf79"
TRANSMITTER_ID="a1bacf67-52eb-492c-b485-1856932504c5"


