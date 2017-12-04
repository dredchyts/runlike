#!/usr/bin/env python

import click
from inspector import Inspector



@click.command(
    help="Shows command line necessary to run copy of existing Docker container.")
@click.argument("container")
@click.option("-n", "--no-name", is_flag=True, help="Do not include container name in output")
@click.option("-p", "--pretty", is_flag=True, help="Pretty print")
@click.option("-a", "--publish-all", is_flag=True, help="Publish all ports instead of currents")
def cli(container, no_name, pretty, publish_all):

    # TODO: -i, -t, -d as added options that override the inspection
    ins = Inspector(container, no_name, pretty, publish_all)
    ins.inspect()
    print(ins.format_cli())


def main():
    cli()

if __name__ == "__main__":
    main()
