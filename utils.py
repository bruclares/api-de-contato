import os


def gerar_arvore(pasta_raiz, ignorar=None):
    if ignorar is None:
        ignorar = {".git", "__pycache__", "venv", ".env", ".DS_Store"}

    print(f"📂 {os.path.basename(os.path.abspath(pasta_raiz))}")

    for root, dirs, files in os.walk(pasta_raiz):
        # Remove pastas ignoradas para não entrar nelas
        dirs[:] = [d for d in dirs if d not in ignorar]

        level = root.replace(pasta_raiz, "").count(os.sep)
        indent = " " * 4 * (level)

        # Imprime a pasta atual (se não for a raiz)
        if root != pasta_raiz:
            print(f"{indent}├── 📁 {os.path.basename(root)}/")

        subindent = " " * 4 * (level + 1)
        for f in files:
            if f not in ignorar:
                print(f"{subindent}├── {f}")


# Rode na pasta atual
if __name__ == "__main__":
    gerar_arvore(".")
