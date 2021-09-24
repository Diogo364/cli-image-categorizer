# Image Categorizer

## Description
These CLI programs help speed up and improve the manual image categorization process by providing a simple, but effective workflow. 

## Table of contents
- [Image Categorizer](#image-categorizer)
  - [Description](#description)
  - [Table of contents](#table-of-contents)
  - [How to use](#how-to-use)
    - [Manual Binary Categorizer](#manual-binary-categorizer)
      - [Description:](#description-1)
      - [Commands:](#commands)
      - [CLI Parameters:](#cli-parameters)
      - [Example of usage:](#example-of-usage)
    - [Manual Multiclass Categorizer](#manual-multiclass-categorizer)
      - [Description:](#description-2)
      - [Commands:](#commands-1)
      - [CLI Parameters:](#cli-parameters-1)
      - [Example of usage:](#example-of-usage-1)
    - [Instalation](#instalation)
  - [Technologies](#technologies)
  - [Autor](#autor)

---
## How to use
### Manual Binary Categorizer
#### Description:
CLI application to classify all images from a specific directory into two categories: `A` or `B`.

By calling the CLI application you will define the directory associated with `A` and `B`. When a image is classified, it is automatically moved from the source directory to the target directory assigned.

#### Commands:
- `a`: Move the shown image to directory `A`;
- `b`: Move the shown image to directory `B`;
- `q`: Exit the program;
- `h`: Print all commands and instructions in the terminal;
#### CLI Parameters:
- `images_dir`:
  - Source directory containing all images that should be classified.
  - Kind: Positional argument.
- `-a` or `--dir-a`:
  - Directory associated with the category `A`.
- `b` or `--dir-b`:
  - Directory associated with the category `B`.
- `--create-dir`:
  - If used both ,dir-a and dir-b, are going to be created if already do not exist.

#### Example of usage:
> ```$ python manual_binary_categorizer ./dataset/images -a ./target/classA -b ./target/classB --create-dir```

---
### Manual Multiclass Categorizer
#### Description:
CLI application to classify all images from a specific directory into various categories (Maximum of 34 classes).

By calling the CLI application you will define a list of output directories, corresponding to each class you want to classify. This list o directories will be associated with all digits and lower-case letters, in that order. When a image is classified, it is automatically moved from the source directory to the target directory assigned.

#### Commands:
- `digits` and `letters`: Move the shown image to directory associated;
  - The directories listed are going to be assigned first by numeric order from [0,9] and then in alphabetical order [a, z].
- `q`: Exit the program;
- `h`: Print all commands and instructions in the terminal;
#### CLI Parameters:
- `images_dir`:
  - Source directory containing all images that should be classified.
  - Kind: Positional argument.
- `-d` or `--dir-list`:
  - Output directories separated by space.
- `--create-dir`:
  - If used both ,dir-a and dir-b, are going to be created if already do not exist.

#### Example of usage:
> ```$ python manual_multiclass_categorizer ./dataset/images -d ./target/classA ./target/classB ./target/classC --create-dir```

### Instalation
All requirements are in the `requirements.txt` file. From pip, just run in the terminal the following command and you are ready to go.
> ```$ pip install -r requirements.txt```
## Technologies

- `Python>=3.8`
- `OpenCV>=4.5`

## Autor

<a href="https://github.com/Diogo364" >
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/44041957?s=400&u=44d208aa5d0b6df75c0bb60e2583fe6015cc0ed0&v=4" width="100px;" alt=""/>
</a>
<br>

[Diogo Nascimento](https://github.com/Diogo364)
[![Linkedin Badge](https://img.shields.io/badge/-Diogo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/diogo-telheiro-do-nascimento/)](https://www.linkedin.com/in/diogo-telheiro-do-nascimento/) 
[![Gmail Badge](https://img.shields.io/badge/-diogotnascimento94@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:diogotnascimento94@gmail.com)](mailto:diogotnascimento94@gmail.com)