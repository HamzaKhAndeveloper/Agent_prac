def research(query: str):
    return "reseach succeflly and output is data about"+query


def generate(prompt: str):
    return "generate succeflly and output is data about "+prompt

Toolss = {
    "research": research,
    "generate": generate
}