import importlib.metadata
packages = [
    "langchain",    
    "ragas",
    "langchain-mcp-adapters",
    "mcp",
    "ddgs",
    "langchain-openai"
    ]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")