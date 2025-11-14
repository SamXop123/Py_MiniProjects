import requests

username = "SamXop123"

# 1. Get all your public repos
repos_url = f"https://api.github.com/users/{username}/repos"
repos = requests.get(repos_url).json()

language_totals = {}       # { "HTML": { "repo": "X", "bytes": 5000 }, ... }

for repo in repos:
    repo_name = repo["name"]
    lang_url = f"https://api.github.com/repos/{username}/{repo_name}/languages"

    langs = requests.get(lang_url).json()

    for lang, bytes_count in langs.items():
        # if language not seen before, add it
        if lang not in language_totals:
            language_totals[lang] = {
                "repo": repo_name,
                "bytes": bytes_count
            }
        else:
            # check if current repo has more of this language
            if bytes_count > language_totals[lang]["bytes"]:
                language_totals[lang] = {
                    "repo": repo_name,
                    "bytes": bytes_count
                }

print("\n📌 Repository with Highest Amount for Each Language\n")
for lang, data in language_totals.items():
    print(f"{lang}: {data['repo']} ({data['bytes']} bytes)")
