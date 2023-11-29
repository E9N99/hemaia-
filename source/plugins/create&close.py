from random import randint
from typing import Optional
from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
import asyncio
from pyrogram.types import Message
#سورس القرش بيمسي - @T_3_A

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"{err_msg}")
    return False

@Client.on_message(filters.command("فتح محادثة مرئية$", prefixes=f".") & filters.me)
async def opengc(c, msg):
    await msg.edit("⎉ جـاري فتـح المحادثة المرئيـة ...")
    if (
        group_call := (
            await get_group_call(c, msg, err_msg="المحادثة المرئية مفتوحة")
        )
    ):
        await msg.edit("المحادثة المرئية مفتوحة")
        return
    try:
            await c.invoke(
                CreateGroupCall(
                    peer=(await c.resolve_peer(msg.chat.id)),
                    random_id=randint(10000, 999999999),
                )
            )
            await msg.edit("⎉ تـم .. فتـح المحادثـة المرئيـة .")
    except Exception as e:
        await msg.edit("⎉ عـذرًا .. أنت لسـت أدمـن")
@Client.on_message(filters.command("قفل المحادثة المرئية$", prefixes=f".") & filters.me)
async def end_vc(c, msg):
    chat_id = msg.chat.id
    if not (
        group_call := (
            await get_group_call(c, msg, err_msg="المحادثة المرئية مغلفة أصلًا")
        )
    ):
        await msg.edit("⎉ المحادثـة المرئية مغلقـة أصلًا .")
        return
    try:
      await c.invoke(DiscardGroupCall(call=group_call))
      await msg.edit("⎉ تم قفـل المحادثة المرئيـة")
    except:
        await msg.edit("⎉ أنـت لسـت أدمن ..")