from rich.console import Console
from rich.table import Table


def make_table():
    table = Table(title="YouTube Comments", show_lines=True)

    table.add_column("commentId", style="cyan3", no_wrap=True)
    table.add_column("textOriginal", style="bright_magenta")
    table.add_column("testDisplay",  style="spring_green2")
    table.add_column("authorDisplayName",  style="light_cyan1")
    table.add_column("viewerRating",  style="light_pink3")
    table.add_column("likeCount", style="yellow3")
    table.add_column("publishedAt",   style="light_steel_blue1")

    return table


def add_rows(table, id, textOriginal, textDisplay, authorDisplayName, viewerRating, likeCount, publishedAt):
    table.add_row(id, textOriginal, textDisplay, authorDisplayName,
                  viewerRating, likeCount, publishedAt)


def main():
    table = make_table()
    add_rows(table, "1", "Original text", "Display text",
             "Author", "Rating", "Likes", "Published")
    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
