import pathlib

IMAGE_DIRECTORY = pathlib.Path.cwd().joinpath('images')


def main(filename):
    return IMAGE_DIRECTORY.joinpath(filename).with_suffix('.jpg')
