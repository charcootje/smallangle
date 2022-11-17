import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    """Adds functions to one group
    """    
    pass

@cmd_group.command()
@click.option("-n", "--number", default=0)
def sin(number):
    """Calculate the sinus of a number of steps

    Args:
        number (integer): number of steps
    """    
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option("-n", "--number", default=pi)
def tan(number):
    """Calculate the tangens of a number of steps

    Args:
        number (integer): number of steps
    """    
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()