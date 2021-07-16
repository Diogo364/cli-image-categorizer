import os
import argparse
import glob
import cv2
from string import ascii_lowercase, digits
from scripts import utils

def print_instrutions(directory_path_dict):
    print(f'[INFO] Instructions:')
    for idx, dir in directory_path_dict.items():
        print(f'- Press `{idx}` to move image to dir a {dir}')
    print(f'''- Press `q` to exit program
- Press `h` to see this menu again''')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Binary Image Classification: It moves an image from a image_dir to dir-a or dir-b')
    parser.add_argument('images_dir', type=str, help='Directory that contains images to classify')
    parser.add_argument('-d', '--dir-list', required=True, nargs='+', help='Destination directories separated by space. The number of classes will be assumed as the number of directories.')
    parser.add_argument('--create-dir', action='store_true', help='Use this parameter to create directory if does not exist')

    args = parser.parse_args()

    valid_keys_list = utils.get_valid_keys_for_classes()

    assert len(valid_keys_list) >= len(args.dir_list), f'Exceeded maximum number of classes: {len(valid_keys_list)}'
    directory_path = { idx: dir for idx, dir in zip(sorted(valid_keys_list), args.dir_list) }

    if args.create_dir:
        for dir in directory_path.values():
            print(f'[INFO] Creating directory: {dir}')
            if not utils.is_directory(dir):
                created = utils.create_directory(dir)
                assert created, "Unexpected problem on creation of dir: {dir}"

    
    print(f'[INFO] Loading images from: {args.images_dir}')
    images_path = sorted(os.listdir(os.path.join(args.images_dir)))
    print(f'[INFO] Total of {len(images_path)} images loaded')

    classification_amount = 0
    finish_program = False
    for im in images_path:
        
        image_from_source_path = os.path.join(args.images_dir, im)
        image = cv2.imread(image_from_source_path)
        
        cv2.imshow(f'Image - {im}', image)
        
        # Display instructions on first image
        if not classification_amount:
            print_instrutions(directory_path)
        
        pressed_key = None
        
        while not finish_program:

            pressed_key = cv2.waitKey(0)
            pressed_char = utils.parse_cv2_pressed_key_to_char(pressed_key)
           
            if pressed_char == 'q':
                print(f'[INFO] Exiting program')
                finish_program = True
            
            elif pressed_char == 'h':
                print_instrutions(directory_path)

            elif pressed_char:
                try:
                    print(f'[INFO] Moving image to {directory_path[pressed_char]}')
                    utils.move_to_directory(image_from_source_path, os.path.join(directory_path[pressed_char], im))
                    print(f'[INFO] Image successfully moved')
                    classification_amount += 1
                    cv2.destroyAllWindows()
                    break
                except KeyError:
                    print(f'[INFO] You have entered an invalid key: {pressed_char}. If you need any help press `h`')

        if finish_program:
            break
    
    print(f'[INFO] Classified {classification_amount} images')
    print(f'Done')
        