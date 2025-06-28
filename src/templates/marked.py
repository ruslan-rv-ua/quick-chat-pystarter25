"""
Template module for loading and rendering markdown-based HTML templates.
Provides the Template class for injecting markdown, title, and language into HTML templates.
"""

from pathlib import Path


class Template:
    """
    A class to load and render a template file with provided markdown, title, and language.
    """

    def __init__(self, file_name: str) -> None:
        """
        Initialize the Template with the given template file name.

        Args:
            file_name (str): The name of the template file to load.
        """
        template_path = Path(__file__).parent / file_name
        self.template = template_path.read_text(encoding="utf-8")

    def render(self, markdown: str, title: str = "", lang: str = "en") -> str:
        """
        Render the template with the provided markdown, title, and language.

        Args:
            markdown (str): The markdown content to insert into the template.
            title (str, optional): The title to insert into the template. Defaults to "".
            lang (str, optional): The language code to insert into the template. Defaults to "en".

        Returns:
            str: The rendered template as an HTML string.
        """
        return (
            self.template.replace("{{lang}}", lang)
            .replace("{{title}}", title)
            .replace("{{markdown}}", repr(markdown))
        )

    def render_file(
        self, file_path: Path | str, title: str = "", lang: str = "en"
    ) -> str:
        """
        Render the template using the contents of a file as markdown.

        Args:
            file_path (Path | str): The path to the markdown file.
            title (str, optional): The title to insert into the template. Defaults to "".
            lang (str, optional): The language code to insert into the template. Defaults to "en".

        Returns:
            str: The rendered template as an HTML string.
        """
        file_path = Path(file_path)
        return self.render(file_path.read_text(encoding="utf-8"), title, lang)
