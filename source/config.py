from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 1488114134
bot_user = "fza0bot"
api_id = 8897410
api_hash = "43cb89a7b70782868b77ace21c1341a9"
session = "1ApWapzMBu6eywcUeW2cRlqoeL08-cNfLt27FECbb7iUeyKFzsLLXDZX5z-A1AVaSZX_pq1G7q_CMN_vlWdk496MdgKxh4NfRGuwGsYwzy0HzWb9GSMB8Z-EXu9kUyU8XXbnWPqQnDcOAembo5CEJkocT82lVVXwIcNqJktjRyefAynbAFaY69kOK9pIQ4sHkr2v1UwxPSJss0XTNeTcuASH879ZZFPYzIX_uXbaUXxPQOcP66KChsg2ICz8qV6Hup8eywu9vyySkOfEiX3ty7BjRkiPBsYwVCib6FKTLTwj1yNjaG_9FzQXROOn3793Q0Br4c1O_lF5zu63a5N7rvDuHf5Z4ImY="
token = "6243993552:AAF2KXc1toaLD8fX0SrbsquQss6n4waVpwE"
sudo_command = [1488114134, 1488114134]
pm = "1488114134"
mention = "1488114134"
plugins = dict(root="plugins")
app = Client("user:fza0bot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("fza0bot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
