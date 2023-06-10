import discord,json,os,random
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MemberConverter
from discord import DMChannel






with open("config.json") as file: 
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]
    genchannel = info["Gen_channel"]
    dropchannel = info["drop_channel"]
    
   

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())








@bot.event
async def on_ready():
    print("Tym razem bez błędu, ale fart :)")
    



@bot.event
async def on_command_error(ctx, error):
       if isinstance(error, CommandNotFound):
                nocommand = discord.Embed(title="Error!",description="Taka komenda nie istnieje", color=discord.Color.red())
                await ctx.send(embed=nocommand)

@bot.event
async def on_message(message):
    
    if message.author.bot:  
        return

    if message.channel.id == twoje id kanalu legit check:  
        custom_emoji = discord.PartialEmoji(name='nazwa emoji', id='id emoji')
        await message.add_reaction(custom_emoji)  

    await bot.process_commands(message)               



class SupremeHelpCommand(commands.HelpCommand):
    async def send_error_message(self, error, message, ctx):
        

        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        channel = self.get_destination()
        
        await channel.send(embed=embed)
        


    

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=discord.Color.green())
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            if command_signatures := [
                self.get_command_signature(c) for c in filtered
            ]:
                cog_name = getattr(cog, "qualified_name", "Komendy")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command) , color=discord.Color.green())
        if command.help:
            embed.description = command.help
        if alias := command.aliases:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_help_embed(self, title, description, commands): 
        embed = discord.Embed(title=title, description=description or "Nie znalazłem nic")

        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                embed.add_field(name=self.get_command_signature(command), value=command.help or "Nie znalazłem nic")

        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        title = self.get_command_signature(group)
        await self.send_help_embed(title, group.help, group.commands)

    async def send_cog_help(self, cog):
        title = cog.qualified_name or "No"
        await self.send_help_embed(f'{title} Kategoria', cog.description, cog.get_commands())
        
bot.help_command = SupremeHelpCommand()
            
            

    

    
@bot.command() 
async def stock(ctx):
    stockmenu = discord.Embed(title="Dostępne konta",description="", color=discord.Color.green()) 
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: 
            ammount = len(f.read().splitlines()) 
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") #
            stockmenu.description += f"*{name}* - {ammount}\n" 
    await ctx.send(embed=stockmenu) 



@bot.command() 
async def gen(ctx,name=None):
    if str(ctx.channel.id) != genchannel:
        chann=discord.Embed(title="Error!", description="Możesz generować jedynie na kanale <#id kanalu>", color=discord.Color.red())
        await ctx.send(embed=chann)
        return
    else:
    
        if name == None:
            non=discord.Embed(title="Error!", description="Podaj, co chcesz wygenerować", color=discord.Color.red())
        
            await ctx.send(embed=non) 
            return
        else:
            name = name.lower()+".txt" 
        if name not in os.listdir("Accounts"): 
            no=discord.Embed(title="Error!", description="Niestety te konta narazie nie są dostępne. `Użyj !stock, aby zobaczyć dostępne konta`", color=discord.Color.red())
            await ctx.send(embed=no)
            return
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() 
            if len(lines) == 0: 
                kon=discord.Embed(title="Error!", description="Nie ma tych kont aktualnie.", color=discord.Color.red())
                await ctx.send(embed=kon)
        
                return
            else:
                
            
              with open("Accounts\\"+name) as file:
                        account = random.choice(lines) 
            try: 
                    await ctx.author.send(f"`{str(account)}`\n\nTa wiadomość zostanie usunięta za {str(delete)} sekund!",delete_after=delete)
            except: 
                    priv=discord.Embed(title="Error!", description="Masz zablokowany priv, nie mogę wysłać wiadomości.", color=discord.Color.red())
                    await ctx.send(embed=priv)
            else: 
                    suc=discord.Embed(title="Sukces!", description="Konto zostało wysłane w wiadomości prywatnej.", color=discord.Color.green())
                    await ctx.send(embed=suc)
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") 
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: 
                            if line != account: 
                                file.write(line+"\n") 






@bot.command() 
async def drop(ctx):
    if str(ctx.channel.id) != dropchannel:
        await ctx.message.delete()
        chann=discord.Embed(title="Error!", description="Możesz użyć tej komendy jedynie na kanale <#id kanalu drop>", color=discord.Color.red())
        await ctx.send(embed=chann)
        return
    
    else:
            gen_number = random.randint(0, 5)
            if gen_number == 1:
                prizelist = ["zniżka 5% na boosty", "zniżka 10% na boosty","zniżka 5% na członków discord", "zniżka 10% na członków discord", "zniżka 15% na członków discord", "zniżka 20% na członków discord", "zniżka 25% na członków discord", "zniżka 30% na członków discord", "zniżka 5% na social boost", "zniżka 10% na social boost"]
                member = ctx.author
                emb=discord.Embed(title = "G0 N1TR0 - Drop", description = f"Gratulacje {member} wygrałeś: `{random.choice(prizelist)}`!\nBon ma ważność `3 dni`. Gratulujemy!", color=discord.Color.green())
                await ctx.send(embed=emb)
                return
            else:
                 await ctx.message.delete()
                 embb = discord.Embed(title = "G0 N1TR0 - Drop", description = "Niestety nie udało Ci się wylosować żadnej z nagród.\nSpróbuj ponownie za 2h!", color=discord.Color.red())
                 await ctx.send(embed=embb, delete_after= 5)



@bot.command()
async def pp(ctx):
    if ctx.message.author.id == id ownera:
        await ctx.send("email: twoj email paypal xd \n\n**Wyślij Znajomi i rodzina**")
    else:
            await ctx.send("Tylko felek może użyć tą komendę")
            return

@bot.command()
async def blik(ctx):
    if ctx.message.author.id == id ownera:
        await ctx.send("twoj numer blik xd")
    else:
            await ctx.send("Tylko felek może użyć tą komendę")
            return     

                                                
            
            
                
            
           
         
           

    

    

         
                    
                

           
            
                
                
            
                    
   


            
                    




         


     
     
     
     
    

bot.run(token)
