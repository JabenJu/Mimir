import lightbulb
import d20
from generate_wisdom import wisdom

bot=lightbulb.BotApp(token='OTQxNzcyNTA1MTU1MjYwNDI2.Ygaz_g.KG-bN-4e_NYQgiJT7RtWSyRulTw', 
prefix=";")

help_message = """
Commands Avaliable:
;help   - You already used this??
;hello  - Says hello

;r      - Rolls dice

~k	  keep	           -Keeps all matched values.
~p	  drop	           -Drops all matched values.
~rr	  reroll	         -Rerolls all matched values until none match.
~ro	  reroll once	     -Rerolls all matched values once.
~ra	  reroll and add   -Rerolls up to one matched value once, keeping the original roll.
~e	  explode on       -Rolls another die for each matched value.
~mi	  minimum	         -Sets the minimum value of each die.
~ma	  maximum	         -Sets the maximum value of each die.

~hX	  highest X	       -The highest X values in the set.
~lX	  lowest X	       -The lowest X values in the set.
~>X	  greater than X	 -All values in this set greater than X.
~<X	  less than X	     -All values in this set less than X.
"""

@bot.command
@lightbulb.command('hello', 'Says hello')
@lightbulb.implements(lightbulb.PrefixCommand)
async def hello(ctx):
  await ctx.respond('Hello, World!')

@bot.command
@lightbulb.command('drink', 'Drink from the Well of Prophecy')
@lightbulb.implements(lightbulb.PrefixCommand)
async def drink(ctx):
  await ctx.respond(wisdom())

@bot.command
@lightbulb.command('killmyselfface', 'Does so')
@lightbulb.implements(lightbulb.PrefixCommand)
async def killmyselfface(ctx):
  await ctx.respond(':      ^)')

@bot.command
@lightbulb.command('recitebeemovie', 'Does so')
@lightbulb.implements(lightbulb.PrefixCommand)
async def recitebeemovie(ctx):
  await ctx.respond('http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html')

@bot.command
@lightbulb.command('Help', 'Please God help me')
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx):
  await ctx.respond(help_message)

@bot.command
@lightbulb.option('Comments', 'The comments for the roll', required=False, modifier=lightbulb.OptionModifier.GREEDY)
@lightbulb.option('Dice', 'The dice and modifiers of the dice')
@lightbulb.command('r', 'Rolls dice')
@lightbulb.implements(lightbulb.PrefixCommand)
async def r(ctx):
  roll = str(d20.roll(ctx.options.Dice, allow_comments=True))
  if(ctx.options.Comments != None):
    comments = " ".join(ctx.options.Comments)
    await ctx.respond(roll+" ("+comments+")", reply=True, mentions_reply=True)
  else:
    await ctx.respond(roll, reply=True, mentions_reply=True)


bot.run()

