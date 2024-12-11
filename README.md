# Introduction
For the final project of the CSC-323 course, we were given the choice to continue the work of a previous project or to recreate one of the papers which we read throughout the term. I chose the latter, and the specific paper I wanted to replicate was the work of Robert Axelrod in using genetic algorithms to solve the iterative prisoner's dilemma problem. In this problem, the prisoner's dilemma is treated as a game that spans multiple rounds, and players are awarded points based on the outcome of each round. The genetic algorithm can see up to three previous inputs, and bases its next move off of a hard coded response in its genome in response to these three inputs. The genetic algorithm's goal is to maximize the points it can get against varying opponents over 151 round games.

## Helpful links

For more detailed info, read my [Final Project Paper](https://github.com/gradybos/GeneticAlgIPD/blob/main/Bosanko___Final_Project_Paper.pdf).

To see the results I was able to achieve, see the [Main Notebook](https://github.com/gradybos/GeneticAlgIPD/blob/main/project_files/final_project.ipynb).

All files relevant to recreating the experiment are located in the [Project Files Folder](https://github.com/gradybos/GeneticAlgIPD/tree/main/project_files).

## Setup

* Cloned this repo and made it your own 
* navigate to the directory containing this repo
* (optional) create a new virtual environment for this demo:  `python -m venv myvenv`
* launch the new virtual environment if it hasn't auto-launched: `source myvenv/bin/activate`
* install requirements: `python -m pip install -r requirements.txt`

After setting up the virtual environment (or just downloading all packages into the project directory) the main notebook file will work out of the box. This is where the experimentation with the iterative prisoner's dilemma takes place. There are MANY player files to choose from and experiment with.

## Using a player file

* The PDPlayer class represents a general player wrapper
    * The game only ever interfaces with this class
    * The player type, which determines the actual inputs, is passed as an argument when constructing this player
* The other player classes are to be used as arguments for the PDPlayer
    * There are many existing examples of this in the code