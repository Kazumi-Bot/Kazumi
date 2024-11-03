import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View


class SelectMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    options = [
        discord.SelectOption(label="Red", value="1", description="Red Color"),
        discord.SelectOption(label="Green", value="2", description="Green Color")
    ]

    @discord.ui.select(placeholder="Select Class", options=options, custom_id="Select_Role")
    async def menu_callback(self, interaction: discord.Interaction, select):
        select.disabled = True
        user = interaction.user
        guild = interaction.guild
        selected_value = select.values[0]

        # Define your role IDs corresponding to the options
        role_ids = {
            '1': 1301948122930352239,  # Replace with your role ID
            '2': 1301948155641860096
        }

        role_id = role_ids.get(selected_value)

        if role_id:
            role = guild.get_role(role_id)

            if role:
                # Check if the user already has the role
                for existing_role_id in role_ids.values():
                    existing_role = guild.get_role(existing_role_id)
                    if existing_role in user.roles:
                        await user.remove_roles(existing_role)

                # Add the role to the user
                await user.add_roles(role)
                await interaction.response.send_message(content=f"Class role <@&{role.id}> added.", ephemeral=True)
            else:
                await interaction.response.send_message(content="Error: Role not found.", ephemeral=True)
        else:
            await interaction.response.send_message(content="Error: Invalid selection.", ephemeral=True)


class drop_Down(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Select_Role_Dropdown")

    @app_commands.command(name="setclass", description="Select your class of choice")
    async def select_class(self, interaction: discord.Interaction):
        view = SelectMenu()
        embed = discord.Embed(title="Class Selection", description="Use the dropdown menu to select your class.",
                              color=0x00ff00)
        embed.add_field(name="Note",value="One Role Minimum")
        embed.set_image(url="https://i.ibb.co/zJrqKbf/sgfsdfgfdg.png")
        await interaction.response.send_message(embed=embed, view=view)


async def setup(client):
    client.remove_command("help")
    await client.add_cog(drop_Down(client), guilds=[discord.Object(id="1271649288791003217")])
