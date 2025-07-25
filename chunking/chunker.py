# chunking/chunker.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class RouteChunk:
    route: str
    method: str
    file: str
    function_name: str
    docstring: Optional[str]
    logic: str

    def to_text_chunk(self) -> str:
        """
        Format the route chunk as a structured, readable text block
        suitable for embedding or LLM input.
        """
        
        return f"""
[Route] {self.method} {self.route}
[Function] {self.function_name}
[File] {self.file}

[Docstring]
{self.docstring or "No docstring provided."}

[Logic]
{self.logic.strip()}
""".strip()
