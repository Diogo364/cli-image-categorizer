import os
import argparse
import glob
import cv2
from scripts import utils

def print_instrutions():
    print(f'''
[INFO] Instructions:
- Press `a` to move image to dir a {directory_path["a"]}
- Press `b` to move image to dir b {directory_path["b"]}
- Press `q` to exit program
- Press `h` to see this menu again
''')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Binary Image Classification: It moves an image from a image_dir to dir-a or dir-b')
    parser.add_argument('images_dir', type=str, help='Directory that contains images to classify')
    parser.add_argument('-a', '--dir-a', required=True, type=str, help='Directory corresponding to the first category')
    parser.add_argument('-b', '--dir-b', required=True, type=str, help='Directory corresponding to the second category')
    parser.add_argument('--create-dir', action='store_true', help='Use this parameter to create directory if does not exist')

    args = parser.parse_args()

    directory_path = {
        'a': args.dir_a,
        'b': args.dir_b
    }

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
            print_instrutions()
        
        pressed_key = None
        
        while not finish_program:

            pressed_key = cv2.waitKey(0)
            pressed_char = utils.parse_cv2_pressed_key_to_char(pressed_key)
           
            if pressed_char == 'q':
                print(f'[INFO] Exiting program')
                finish_program = True
            
            elif pressed_char == 'h':
                print_instrutions()

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
        