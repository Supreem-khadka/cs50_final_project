import argparse
from bs4 import BeautifulSoup
import pandas as pd
import pyfiglet
import requests
from requests.exceptions import Timeout, RequestException
import sys

# An empty list for storing all the information related to the projects
info = []


def main():
    ascii_art = pyfiglet.figlet_format("Scrapping", font="slant")
    print(ascii_art)
    parser = argparse.ArgumentParser(
        description="Scrapes the CS50p Project Gallery and displays or writes the output to a file of choice"
    )
    parser.add_argument(
        "-t", "--text", type=str, help="The text file to save the output to"
    )
    parser.add_argument(
        "-x", "--xlsx", type=str, help="The xlsx file to save the output to"
    )
    args = parser.parse_args()

    project_gallery: str = (
        "https://cs50.harvard.edu/python/2022/gallery/"  # cs50p project gallery
    )
    response: str = req(project_gallery)
    parse_html(response)

    if args.text and args.xlsx:
        write_text(args.text)
        write_xlsx(args.xlsx)

    else:
        if args.text:
            write_text(args.text)

        elif args.xlsx:
            write_xlsx(args.xlsx)

        else:
            display()


def req(addr: str) -> str:
    """
    sends requests to the address provided and return the reponse

    Args:
        addr (str): The address whose data has to be scrapped

    Returns:
        str: response of the request

    Raises:
        Exception: for any status code except 200
    """
    try:
        res = requests.get(addr, timeout=(3, 5))
        if res.status_code == 200:
            return res.text

        else:
            raise Exception(f"Non-success status code: {res.status_code}")

    except Timeout:
        print("The request timed out")
        sys.exit(1)

    except RequestException as err:
        print(err)
        sys.exit(1)

    except Exception as err:
        print(err)
        sys.exit(1)


def parse_html(response: str) -> None:
    """
    Parses through the passed html reponse

    Args:
        response (str): The html from the response

    Returns:
       None
    """
    # parse through the html using beautiful soup
    parse = BeautifulSoup(response, "html.parser")

    # find the class project
    project = parse.find_all("div", class_="project")

    for projects in project:
        this_project = {}  # for storing information of the current project
        link_html = projects.find("a")
        paragraphs: list = projects.find_all("p", class_="mb-0")
        title_and_creator = paragraphs[0].text.strip().split(" by")
        # strings
        link: str = link_html.get("href")
        description: str = paragraphs[1].text.strip()
        title: str = title_and_creator[0]
        creator: str = title_and_creator[1].strip()
        # populating the dictionary with key value pairs
        this_project["title"] = title
        this_project["creator"] = creator
        this_project["description"] = description
        this_project["link"] = link
        info.append(this_project)

    return 0


def display() -> int:
    """
    Displays the scraped information

    Args:
        None

    Returns:
       None
    """
    print("\t\t\t\t\tCS50P PROJECT GALLERY")
    print("-" * 100)
    print(f"Total Projects: {len(info)}")

    if len(info) == 0:
        return 1

    num = 1
    for projects in info:
        print(f"{num}. {projects['title']} by {projects['creator']}")
        print(f"\tYoutube link: {projects['link']}")
        print(f"\tProject description: {projects['description']}\n")
        num += 1

    print("-" * 130)
    print("\t\t\t\tEND")
    print("-" * 130)

    return 0


def write_text(fileName: str) -> None:
    """
    Store the scrapped data to a text a file

    Args:
        fileName (str): the filename for the new text file

    Returns:
       None
    """
    filename = fileName + ".txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\t\t\t\t\tCS50P PROJECT GALLERY\n")
        file.write("-" * 170)
        file.write(f"\n\nTotal Projects: {len(info)}\n\n")

        if len(info) == 0:
            return 1

        num = 1
        for projects in info:
            file.write(f"{num}. {projects['title']} by {projects['creator']}\n")
            file.write(f"\tYoutube link: {projects['link']}\n")
            file.write(f"\tProject description: {projects['description']}\n\n")
            num += 1
        file.write("-" * 170)
        file.write("\n\t\t\t\t\t\t\tEND\n")
        file.write("-" * 170)

        print(f"Data written successfully -> {filename}")

        return 0


def write_xlsx(fileName: str) -> None:
    """
    Store the scrapped data as spreadsheet

    Args:
        fileName (str): the filename for the new text file

    Returns:
       None
    """
    filename = fileName + ".xlsx"
    # Create a data frame
    df = pd.DataFrame(info)

    # Write the dataframe to an excel file
    df.to_excel(filename)
    print(f"Data written successfully -> {filename}")


if __name__ == "__main__":
    main()
