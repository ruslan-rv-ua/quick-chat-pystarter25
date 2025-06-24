from pathlib import Path


class WebviewMarked:
    def __init__(self) -> None:
        template_path = Path(__file__).parent / "marked.html"
        self.template = template_path.read_text(encoding="utf-8")

    def render(self, markdown: str, title: str = "", lang: str = "en") -> str:
        return (
            self.template.replace("{{lang}}", lang)
            .replace("{{title}}", title)
            .replace("{{markdown}}", repr(markdown))
        )

    def render_file(
        self, file_path: Path | str, title: str = "", lang: str = "en"
    ) -> str:
        file_path = Path(file_path)
        return self.render(file_path.read_text(encoding="utf-8"), title, lang)
