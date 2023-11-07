import urllib.request
import re
from argparse import ArgumentParser
from pathlib import Path
from typing import List
import logging


def fetch_tree_sitter_repositories() -> List[str]:
    """
    Fetch the list of Tree-sitter language repositories from GitHub.

    Returns:
        List[str]: A list of repository URLs.
    """
    url = "https://tree-sitter.github.io/tree-sitter/"
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read().decode("utf-8")
    except Exception as e:
        logging.error(f"Failed to fetch {url}. Error: {e}")
        return []

    # Regex to extract repository URLs
    pattern = r'"(https://github.com/.*?/tree-sitter-.*?)"'
    repo_urls = re.findall(pattern, html_content)
    return repo_urls


def download_node_types(repo_url: str, dest_dir: Path):
    """
    Download the node-types.json file from a Tree-sitter language repository.

    Parameters:
        repo_url (str): The URL of the Tree-sitter language repository.
        dest_dir (Path): The destination directory to save the node-types.json file.
    """
    node_types_url = f"{repo_url}/master/src/node-types.json"
    try:
        response = urllib.request.urlopen(node_types_url)
        content = response.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            logging.warning(f"node-types.json does not exist in {repo_url}")
        else:
            logging.error(f"Failed to download {node_types_url}. HTTP Error: {e.code}")
        return
    except Exception as e:
        logging.error(f"Failed to download {node_types_url}. Error: {e}")
        return

    lang_name = repo_url.split("/")[-1].removeprefix("tree-sitter-")
    dest_path = dest_dir / f"node-types-{lang_name}.json"
    dest_path.write_bytes(content)
    logging.info(f"Successfully downloaded {node_types_url} to {dest_path}")


def main():
    """
    Main function to handle fetching and downloading.
    """
    # Configure logging
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)

    # Parse CLI arguments
    parser = ArgumentParser(description="Download and process node-types.json files.")
    parser.add_argument(
        "--dest-dir",
        type=Path,
        default=Path("./node_types_2"),
        help="Destination directory to store the downloaded node-types.json files.",
    )
    args = parser.parse_args()

    # Ensure the destination directory exists
    args.dest_dir.mkdir(parents=True, exist_ok=True)
    logging.info(f"Destination directory set to {args.dest_dir}")

    # Fetch the list of Tree-sitter repositories
    logging.info("Fetching list of Tree-sitter repositories...")
    repo_urls = fetch_tree_sitter_repositories()
    if not repo_urls:
        logging.error("Could not fetch repository URLs. Exiting.")
        return
    logging.info(f"Fetched {len(repo_urls)} repositories.")

    # Download node-types.json files
    logging.info("Downloading node-types.json files...")
    for repo_url in repo_urls:
        download_node_types(repo_url, args.dest_dir)
    logging.info("Download process completed.")


if __name__ == "__main__":
    main()
