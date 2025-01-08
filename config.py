# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21478717")

API_HASH = os.environ.get("API_HASH", "8f8629885b7fd647e3a5006fb27c38d6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8020786088:AAFNhL6vHJxEIar-RLR879Hb6NzlA6FoLII") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TsAll_channel") 

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://tosiksaini:
FsibH4HOJCN07N9t@cluster0.notst.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1807895968').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
