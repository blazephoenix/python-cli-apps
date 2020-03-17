import click
from pyfiglet import Figlet

f = Figlet(font='thick')
print(f.renderText("Text Match"))

@click.command()
@click.option('--teststring', prompt='Enter sentence (under 64 characters)', help='The string you want to test')
@click.option('--originalstring', prompt='Enter sentence (under 64 characters)', help='The string to test against')
def match(teststring, originalstring):
    '''
    This is a program to match two strings/sentences against each other and output the percentage match.
    '''
    list_test = teststring.replace(".","").split()
    list_original = originalstring.replace(".","").split()

    count = float(len(list_original))
    match_count = 0.0

    for i in range(0, len(list_original)):
        for j in range(0, len(list_test)):
            if list_original[i]==list_test[j]:
                match_count += 1.0
    
    click.echo(f"\nCount of original string: {count}\n")
    click.echo(f"Percent match: {round(match_count/count * 100, 2)}%\n")


if __name__ == "__main__":
    match()

'''
TODO: BETTER MATCHING. fuzzywuzzy package.
'''

