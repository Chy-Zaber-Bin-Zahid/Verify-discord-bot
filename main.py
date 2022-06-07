import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix="$")
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#######################-Cse 101-#######################
@client.command(pass_context=True)
async def cse101(ctx):
  if str(ctx.channel) not in ( "verify","join-jaal-family"):
    return

  # name = str(member)
  # new1 = str(member.nick)
  # print(member,type(member))
  # print(name,type(name))
  # print(new1)
  # if new1 == 'None':
  #   await member.edit(nick="JaaL"+name[0:len(name)-5])
  #   new = name[0:len(name)-5]
  #   await ctx.send(f"Welcome to family {new}!",file = discord.File('welcome.png'))
  # elif new1[0:4] == "JaaL":
  #   await ctx.send(f"You're already in 'JaaL' family {new1[4:]}!",file = discord.File('already.png'))
  # else:
  #   await member.edit(nick="JaaL"+new1)
  #   new = new1
  #   await ctx.send(f"Welcome to family {new}!",file = discord.File('welcome.png'))
  user = ctx.author
  role = discord.utils.get(user.guild.roles, name="CSE101")
  store = ctx.author.nick
  member = ctx.author
  memberstr = str(member)
  if str(store) == "None":
    store = memberstr[0:len(memberstr)-5]
  if store[0:6] != "CSE101" and memberstr[0:6] != "CSE101":
    if store[0:3] == "CSE" or memberstr[0:3] == "CSE":
      await ctx.send("Contract admin in order to change course! {}".format(ctx.author.mention))
      return
  # print(member,type(member))
  # print(store,type(store))
  # print(memberstr)
  if str(store) == 'None':
    await member.edit(nick="CSE101_" + memberstr[0:len(memberstr)-5])
    await user.add_roles(role)
    new = memberstr[0:len(memberstr)-5]
    await ctx.send(f"You are given access to the CSE101 channel {new}!",file = discord.File('Tom.gif'))
  else:
    if store[0:6] == "CSE101":
      await ctx.send(f"You're already in 'CSE101' {store[7:]}!",file = discord.File('already.png'))
    elif len(store)<6 or len(store)>6:
      await member.edit(nick="CSE101_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE101 channel {store}!",file = discord.File('Tom.gif'))
    elif len(store) == 6 and store != "CSE101":
      await member.edit(nick="CSE101_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE101 channel {store}!",file = discord.File('Tom.gif'))

#######################-Cse 110-#######################
@client.command(pass_context=True)
async def cse110(ctx): #member: discord.Member 
  if str(ctx.channel) not in ( "verify","join-jaal-family"):
    return

  user = ctx.author
  role = discord.utils.get(user.guild.roles, name="CSE110")
  store = ctx.author.nick
  member = ctx.author
  memberstr = str(member)
  if str(store) == "None":
    store = memberstr[0:len(memberstr)-5]
  if store[0:6] != "CSE110" and memberstr[0:6] != "CSE110":
    if store[0:3] == "CSE" or memberstr[0:3] == "CSE":
      await ctx.send("Contract admin in order to change course! {}".format(ctx.author.mention))
      return

  if str(store) == 'None':
    await member.edit(nick="CSE110_" + memberstr[0:len(memberstr)-5])
    await user.add_roles(role)
    new = memberstr[0:len(memberstr)-5]
    await ctx.send(f"You are given access to the CSE110 channel {new}!",file = discord.File('Tom.gif'))
  else:
    if store[0:6] == "CSE110":
      await ctx.send(f"You're already in 'CSE110' {store[7:]}!",file = discord.File('already.png'))
    elif len(store)<6 or len(store)>6:
      await member.edit(nick="CSE110_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE110 channel {store}!",file = discord.File('Tom.gif'))
    elif len(store) == 6 and store != "CSE110":
      await member.edit(nick="CSE110_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE110 channel {store}!",file = discord.File('Tom.gif'))

#######################-Cse 111-#######################
@client.command(pass_context=True)
async def cse111(ctx): #member: discord.Member 
  if str(ctx.channel) not in ( "verify","join-jaal-family"):
    return

  user = ctx.author
  role = discord.utils.get(user.guild.roles, name="CSE111")
  store = ctx.author.nick
  member = ctx.author
  memberstr = str(member)
  if str(store) == "None":
    store = memberstr[0:len(memberstr)-5]
  if store[0:6] != "CSE111" and memberstr[0:6] != "CSE111":
    if store[0:3] == "CSE" or memberstr[0:3] == "CSE":
      await ctx.send("Contract admin in order to change course! {}".format(ctx.author.mention))
      return

  if str(store) == 'None':
    await member.edit(nick="CSE111_" + memberstr[0:len(memberstr)-5])
    await user.add_roles(role)
    new = memberstr[0:len(memberstr)-5]
    await ctx.send(f"You are given access to the CSE111 channel {new}!",file = discord.File('Tom.gif'))
  else:
    if store[0:6] == "CSE111":
      await ctx.send(f"You're already in 'CSE111' {store[7:]}!",file = discord.File('already.png'))
    elif len(store)<6 or len(store)>6:
      await member.edit(nick="CSE111_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE111 channel {store}!",file = discord.File('Tom.gif'))
    elif len(store) == 6 and store != "CSE111":
      await member.edit(nick="CSE111_"+store)
      await user.add_roles(role)
      await ctx.send(f"You are given access to the CSE111 channel {store}!",file = discord.File('Tom.gif'))




###VejaaL verify code###
  # if str(store) == 'None':
  #   await member.edit(nick="JaaL"+memberstr[0:len(memberstr)-5])
  #   new = memberstr[0:len(memberstr)-5]
  #   await ctx.send(f"Welcome to family {new}!",file = discord.File('welcome.png'))
  # else:
  #   if store[0:4] == "JaaL":
  #     await ctx.send(f"You're already in 'JaaL' family {store[4:]}!",file = discord.File('already.png'))
  #   elif len(store)<4 or len(store)>4:
  #     await member.edit(nick="JaaL"+store)
  #     await ctx.send(f"Welcome to family {store}!",file = discord.File('welcome.png'))
  #   elif len(store) == 4 and store != "JaaL":
  #     await member.edit(nick="JaaL"+store)
  #     await ctx.send(f"Welcome to family {store}!",file = discord.File('welcome.png'))


          
keep_alive()
client.run(os.getenv('Verify'))
