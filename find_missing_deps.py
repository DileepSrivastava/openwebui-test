import os
import pkgutil

def find_imports(path):
    imports = set()
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if line.startswith("import ") or line.startswith("from "):
                            parts = line.replace(",", " ").split()
                            if parts[0] == "import":
                                imports.add(parts[1].split('.')[0])
                            elif parts[0] == "from":
                                imports.add(parts[1].split('.')[0])
    return imports

def find_missing(imports):
    installed = {pkg.name for pkg in pkgutil.iter_modules()}
    return imports - installed

if __name__ == "__main__":
    folder_to_scan = os.path.join(os.getcwd(), "open-webui", "backend")
    all_imports = find_imports(folder_to_scan)
    missing = find_missing(all_imports)

    print("\nAll detected imports:")
    print(sorted(all_imports))

    print("\nMissing modules:")
    print(sorted(missing))
