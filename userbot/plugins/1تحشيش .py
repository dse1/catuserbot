import random

from Jmthon.razan.resources.strings import *
from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

plugin_category = "utils"


@catub.cat_cmd(
    pattern="كت(?:\s|$)([\s\S]*)",
    command=("كت", plugin_category),
)
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@jmthon.ar_cmd(
    pattern="هينه(?:\s|$)([\s\S]*)",
    command=("هينه", plugin_category),
)
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1715051616:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@jmthon.ar_cmd(
    pattern="نسبة الحب(?:\s|$)([\s\S]*)",
    command=("نسبة الحب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@jmthon.ar_cmd(
    pattern="نسبة الانوثة(?:\s|$)([\s\S]*)",
    command=("نسبة الانوثة", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1715051616:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"⌯︙نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@jmthon.ar_cmd(
    pattern="نسبة الغباء(?:\s|$)([\s\S]*)",
    command=("نسبة الغباء", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1715051616:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@jmthon.ar_cmd(
    pattern="اوصف(?:\s|$)([\s\S]*)",
    command=("اوصف", plugin_category),
)
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1715051616:
        return await edit_or_reply(mention, f"**وفف هذا مطوري شكد احبه 🤍**")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"**وفف هذا مطوري شكد احبه 🤍**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**وفف هذا مطوري شكد احبه 🤍**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")
