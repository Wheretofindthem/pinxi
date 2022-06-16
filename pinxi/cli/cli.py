#!/usr/bin/env python

import click

# https://smxi.org/docs/inxi-man.htm


@click.command()
@click.option(
    "-A",
    "--audio",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show audio/sound device(s) information, including device driver.",
)
def inxi(audio):
    if audio:
        print('Audio')


if __name__ == "__main__":
    inxi()
