import random
import string
import os
from os import getenv
import time
import pymongo
from telethon import TelegramClient, events, Button
from pyrogram import Client, filters
from thumbnails import *
from fonts import *

# Use getenv for all sensitive/configurable values
API_ID = os.getenv("API_ID","10284859")
API_HASH = os.getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
STRING_SESSION = os.getenv("STRING_SESSION", "BQGJMTYAnMTEDXmgXzuptSLaeffcIr5AWGiw6J9jtZg94qowD2Y9tHBUaiWAIXtJr9PE2zDRaa5NWFPET5LXfEfxF8bOOdutrPcelB0sVdbQAThRjmyU_k1IhykbZI6vUlaQrFRqtD_p0uMPIXZqQoz8shZIIHkcbaMwN6Ee-x3xhYdTPEWFmSQGNoUEPFBSVPC0H4pN1Gc4XQaG1mApyMFhspCfs8txWLGaATqjskiVVSaH_Udc4-qTd6vT3h6UTdQcvrh76-j0RenbD5CttYWDlZe4uq9fT8SWMCQEMQKnMXD3LBROBq9GgDg8iuwPeGHd6jUriKFbWsaOiI0EZAMA3lu1GQAAAAHSHPeVAA")
GROUP = os.getenv("GROUP", "HeartBeat_Fam")
CHANNEL = os.getenv("CHANNEL", "HeartBeat_Offi")
BOT_TOKEN = os.getenv("BOT_TOKEN", "2096983652:AAHz41orhz9RrWscwg_WwSCp0_OhP-zLmDY")
OWNER_ID = int(os.getenv("OWNER_ID", 1281282633))
LOGGER_ID = os.getenv("LOGGER_ID", "-1001735663878")
mongodb = os.getenv("MONGODB_URI", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
# Working directory
ggg = os.getcwd()

# Initialize data structures
# Track start time
StartTime = time.time()

# Set up MongoDB connection
mongo_client = pymongo.MongoClient(mongodb)
db = mongo_client['voice']
user_sessions = db['user_sessions']
collection = db["users"]

