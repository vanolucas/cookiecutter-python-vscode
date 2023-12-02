from os import path
from shutil import copyfile


PROJECT_DIRECTORY = path.realpath(path.curdir)


if __name__ == '__main__':
    # Create a .env file from the sample
    env_filename = ".env"
    src = path.join(PROJECT_DIRECTORY, f"{env_filename}-sample")
    dst = path.join(PROJECT_DIRECTORY, env_filename)
    copyfile(src, dst)
