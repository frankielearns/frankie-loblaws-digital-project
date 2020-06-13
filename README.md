# frankie-loblaws-digital-project

Loblaws Digital interview project for comparing image similarities me  in a csv file


## Diagram

![Workflow Diagram](workflow_diagram.png?raw=true "Workflow Diagram")


## Designing and Implementation reasoning

I decided to use Python for designing this applications due to the fact that there is already an Python package available that performs the comparison of images for me. The python package I used to perform the comparison is called [skimage](https://scikit-image.org/) and it uses the algoritim developed by [Wang et al.](https://www.cns.nyu.edu/pub/eero/wang03-reprint.pdf) to compare images. I also decided to Dockerize the application due to the ease of use when transporting between different machines and operating systems. In addition, to using Docker I've also decided to use Makefiles to simplify and organize the way users can run the application. After running the python application, it will generate the input.csv which is a listing of the images in the images directory and the output.csv which is the listing and the similarity rating.

## Installation for Windows
* Install Docker following the instructions on https://docs.docker.com/engine/install/
* Install the Chocolatey package manager for Windows https://chocolatey.org/install
* After installing Chocolatey install the Makefile package
```
choco install make
```
## Installation for Linux/Mac
Install Docker following the instructions on https://docs.docker.com/engine/install/

## Usage for Windows
1. Git clone the repository

2. Change into the repository directory edit the Makefile file

3. Change the IMAGES_DIRECTORY variable in the Makefile to the absolute path of where your repository is
```
IMAGES_DIRECTORY = i:\frankie-loblaws-digital-project
```
4. Run the following make command
```
make compare-images
```

5. After running the make target, there should be two files called input.csv and output.csv in the repository folder

## Usage for Linux/Mac

1. Git clone the repository

2. Change into the repository directory and run the following make command
```
make compare-images
```
3. After running the make target, there should be two files called input.csv and output.csv in the repository folder

## Improvements
Adding a script to bootstrap the prerequisite installations for running the application
