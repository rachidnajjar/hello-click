# -*- coding: utf-8 -*-
'''
Created on 2 févr. 2019

@author: rachid
'''
import click
import pytube

@click.command()
@click.argument('url', default='https://www.youtube.com/watch?v=1k5bmP8wh7g', required=True)
@click.option('--path', default='/home/rachid/Musique', help="Path where to download the file.")
def download(url, path):
    '''
    Un petit script pour télécharger depuis youtube.
    '''
    click.echo('Downloading {0} to {1}'.format(url, path))
    yt = pytube.YouTube(url)
    click.echo('Title : {0}'.format(yt.title))
    
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
    click.echo('Stream : {0}'.format(stream))
    stream.download(path)


if __name__ == '__main__':
    download()