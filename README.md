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

-added .gitignore before unity project was created, git large filesystem wasn't supporing files > 100mb

-uninstalled all dotnet sdk, visual studio, net frameworks and reinstalled since unity was giving errors at compile time for using a C# <= 8.0

-trying xNode framework through unity package manifest (see geogui/pacakges/manifest)

-nodes working now on context menu... investigating how to edit properties


![Alt text](screenshot.png?raw=true "screenshot of nodes working")

