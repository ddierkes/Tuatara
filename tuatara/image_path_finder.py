import os
import pathlib

IMAGE_DIRECTORY = pathlib.Path(
    os.environ.get('TUATARA_IMAGE_PATH', pathlib.Path.cwd().joinpath('images'))
)


def main(filename):
    return IMAGE_DIRECTORY.joinpath(filename).with_suffix('.jpg')
