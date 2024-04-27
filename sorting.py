import shutil
import asyncio
import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def read_folder(source_folder, target_folder):
    try:
        for file_path in source_folder.glob('**/*'):
            if file_path.is_file():
                await copy_file(file_path, target_folder)
    except Exception as e:
        logger.error(f"An error occurred while reading the folder: {e}")

async def copy_file(file_path, target_folder):
    try:
        extension = file_path.suffix.lower()
        target_subfolder = target_folder / extension.strip('.')
        target_subfolder.mkdir(parents=True, exist_ok=True)
        shutil.copy(file_path, target_subfolder)
        logger.info(f"Copied {file_path} to {target_subfolder}")
    except Exception as e:
        logger.error(f"An error occurred while copying file {file_path}: {e}")

async def main(source_folder, target_folder):
    await read_folder(Path(source_folder), Path(target_folder))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Asynchronously sort files based on their extensions.')
    parser.add_argument('source_folder', type=str, help='Path to the source folder')
    parser.add_argument('target_folder', type=str, help='Path to the target folder')
    args = parser.parse_args()

    asyncio.run(main(args.source_folder, args.target_folder))
