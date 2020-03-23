# -*- coding: utf-8 -*-

"""Console script for example_cookie_cutter_ceda."""

__author__ = """Elle Smith"""
__contact__ = "eleanor.smith@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD"

import sys
import click


@click.command()
def main(args=None):
    """Console script for example_cookie_cutter_ceda."""
    click.echo("Replace this message by putting your code into "
               "example_cookie_cutter_ceda.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
