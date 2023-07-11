# geoengineer
manage cloud infrastructure through one visual tool

A visual studio to manage docker, terraform and ansible files
your project structure will be saved in a structure like this
### A typical top-level directory layout

    .
    ├── terraform               # terraform files
    ├── ansible                 # ansible files
    ├── docker                  # docker images and scripts
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md

###todo
-terraform node set up

terraform
easier, faster with a visual tool to create providers of any kind.

personal notes

4/jul/2023
-added .gitignore before unity project was created, git large filesystem wasn't supporing files > 100mb


9/jul/2023
-uninstalled all dotnet sdk, visual studio, net frameworks and reinstalled since unity was giving errors at compile time for using a C# <= 8.0

10/jul/2023
-trying xNode framework through unity package manifest (see geogui/pacakges/manifest)

11/jul/2023
-nodes working now on context menu... investigating how to edit properties
thanks to https://www.youtube.com/watch?v=yJezNp4PVpo  

![Alt text](screenshot.png?raw=true "screenshot of nodes working")

