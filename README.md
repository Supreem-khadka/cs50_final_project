# CS50_final_project
Final project for CS50 introduction to programming with python

## CS50P Project Gallery Scrapper
#### Video Demo: https://youtu.be/P4FYmN1oW9Q
#### Description: While trying to do my Final Project I was interested in looking at other students project as well, so I visited the Project gallery, but the web page was not working properly and trying to keep record of the projects was also hard, so I thought may be I should solve this and created by final project a web scrapper. My project is a simple Web Scrapper that scrapes the CS50p project gallery page and provides the details of every listed projects and also saves the output is text or spreadsheet form as specified to command-line arguments

## TODO
#### git clone https://repository_link/
#### cd repo/
#### pip install -r requirement.txt
#### Now it is ready to be executed

## EXECUTION
### To display the output to the terminal
#### python project.py

### To save the output to a txt file
##### python project.py -t filename

### To save the output to an xlsx file
##### python project.py -x filename

### To save the output to a txt file and an xlsx file as well
##### python project.py -t filename -x filename

## Project Details
#### The project send a request to the project gallery page, takes the html from the response and parses through the html for project title, creators name, project description, and the link for the youtube video. It also makes use of command-line arguments. If no arguments are provided, then the ouput displayed in the terminal, but the user can provide text or xlsx file or both to store the output. The output is formatted so that it could easily be understood before being displayed or stored.

