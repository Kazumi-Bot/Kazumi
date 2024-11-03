import sqlite3
import discord
from discord.ext import commands
from discord import ui
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

DatabaseFile = config['Database']['DBName']

# SQLite3 database connection
conn = sqlite3.connect(DatabaseFile)
cursor = conn.cursor()


class shipsApplication(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)  # Permission Settings
    async def ships(self, ctx):
        embed = discord.Embed(title="Place Holder",
                              description="Embed description")
        view = ShipButtons()
        message = await ctx.send(embed=embed, view=view)
        await ctx.message.delete()

    @ships.error
    async def d_error(self, ctx, error):
        await ctx.send(str(error), ephemeral=True)


async def handle_button_click(interaction, button_label, table_name):
    await interaction.response.send_message("Button Click", ephemeral=True)


class ShipButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Button CallBack

    @discord.ui.button(label="Click Me", custom_id="Basic", style=discord.ButtonStyle.blurple)
    async def battle_clipper_button(self, interaction, button):
        await handle_button_click(interaction, "battle_clipper")


async def setup(client):
    await client.add_cog(shipsApplication(client))
