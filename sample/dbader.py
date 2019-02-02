# -*- coding: utf-8 -*-
'''
Created on 2 févr. 2019

@author: rachid
@see: https://dbader.org/blog/python-commandline-tools-with-click
@see: https://dbader.org/blog/how-to-make-command-line-commands-with-python
'''
import click

@click.command()
@click.argument('name')
@click.option('--count', default=1, help="Number of hello.")
def sayHello(name, count):
    for i in range(count):
        click.echo('Hello {0} ! ({1}x)'.format(name, i+1))

if __name__ == '__main__':
    sayHello()