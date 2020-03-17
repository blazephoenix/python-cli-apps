import click
from pyfiglet import Figlet

f = Figlet(font='thick')
print(f.renderText("Madlibs CLI"))

@click.command()
@click.option('--animal', prompt='Enter an animal', help='Name of an animal')
@click.option('--food', prompt='Enter a food', help='Name of a food')
@click.option('--city', prompt='Enter a city', help='Name of a city')
def madlibs(animal, food, city):
    '''
    A CLI application that takes the name of an animal, food and place to make up a madlib.
    '''
    story = f"""
Once upon a time, deep in an ancient jungle,
there lived a {animal.lower()}.  This {animal.lower()}
liked to eat {food.lower()}, but the jungle had
very little {food.lower()} to offer.  One day, an
explorer found the {animal.lower()} and discovered
it liked {food.lower()}.  The explorer took the
{animal.lower()} back to {city.capitalize()}, where it could
eat as much {food.lower()} as it wanted.  However,
the {animal.lower()} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food.lower()}.

The End
            """

    click.echo(story)


if __name__ == "__main__":
    madlibs()