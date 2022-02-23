# Mimir
I read Myth-Weavers sheets and roll dice!

Currently, the Myth-Weavers sheet functionality hasn't been implemented (I'm busy with school, sorry!).

The bot uses `;` as it's prefix.

Rolling is handled with the d20 library, giving a lot of utility for rolls. To roll some dice, type `;r` then the dice you want to roll.

![Capture](https://user-images.githubusercontent.com/89491072/155354501-9bb8957b-2bf2-4de5-8b5c-3ec6aa6e7026.JPG)

Beyond basic rolls, the d20 library provides multiple operators to modify the dice. They're listed below.

| Syntax | Name | Description |
| --- | --- | --- |
| k | keep | Keeps all matched values. |
| p |	drop | Drops all matched values. |
| rr |	reroll |	Rerolls all matched values until none match. (Dice only) |
| ro | reroll once |	Rerolls all matched values once. (Dice only) |
| ra | reroll and add | Rerolls up to one matched value once, keeping the original roll. (Dice only) |
| e | explode on | Rolls another die for each matched value. (Dice only) |
| mi | minimum | Sets the minimum value of each die. (Dice only) |
| ma | maximum | Sets the maximum value of each die. (Dice only) |

You can also select specific values from sets of dice using operators.

| Syntax | Name | Description |
| --- | --- | --- |
| X | literal | All values in this set that are literally this value. |
| hX | highest X | The highest X values in the set. |
| lX | lowest X | The lowest X values in the set. |
| >X | greater than X | All values in this set greater than X. |
| <X | less than X | All values in this set less than X. |

The bot can also handle basic math, but who cares about math?
