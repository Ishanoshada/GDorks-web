from flask import Flask, render_template, request, jsonify
import random
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


class GDorksSelector:
    def __init__(self, repo_owner="Ishanoshada", repo_name="GDorks"):
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GDorks-Selector",
            "Authorization": f"token {os.getenv('GITHUB_PAT')}"
        }

    async def fetch_json(self, session, url):
        """Fetch JSON data from a URL using aiohttp."""
        async with session.get(url, headers=self.headers) as response:
            if response.status == 200:
                return await response.json()
            return None

    async def get_categories(self):
        """Get all available categories (folders) from the repository."""
        async with aiohttp.ClientSession() as session:
            contents = await self.fetch_json(session, self.base_url)
            #print(self.base_url)
            if contents:
                # Filter only directories
                categories = [item["name"] for item in contents if item["type"] == "dir"]
                print(f"Categories: {categories}")  # Log the categories
                return categories
            print("No contents found or unable to fetch contents.")
            return []


    async def get_files_in_category(self, category):
        """Get all `.txt` files in a specific category."""
        async with aiohttp.ClientSession() as session:
            contents = await self.fetch_json(session, f"{self.base_url}/{category}")
            if contents:
                return [item["name"] for item in contents if item["type"] == "file" and item["name"].endswith(".txt")]
            return []

    async def get_random_lines_from_file(self, category, num_lines=10):
        """Fetch random lines from a random `.txt` file in the specified category."""
        files = await self.get_files_in_category(category)
        if not files:
            return []

        random_file = random.choice(files)
        async with aiohttp.ClientSession() as session:
            file_metadata = await self.fetch_json(session, f"{self.base_url}/{category}/{random_file}")
            if file_metadata and "download_url" in file_metadata:
                async with session.get(file_metadata["download_url"]) as file_response:
                    if file_response.status == 200:
                        file_content = await file_response.text()
                        lines = [line.strip() for line in file_content.splitlines() if line.strip()]
                        return random.sample(lines, min(num_lines, len(lines)))
        return []

# Initialize GDorksSelector
selector = GDorksSelector()

@app.route('/')
async def home():
    """Home page to display categories and a form."""
    categories = await selector.get_categories()
    #print(categories)
    return render_template('index.html', categories=categories)

@app.route('/get-dorks', methods=['POST'])
async def get_dorks():
    """Endpoint to fetch random dorks."""
    data = request.json
    category = data.get('category')
    num_dorks = int(data.get('num_dorks', 10))
    
    if not category:
        return jsonify({"error": "Category is required"}), 400
    
    dorks = await selector.get_random_lines_from_file(category, num_dorks)
    if dorks:
        return jsonify({"dorks": dorks})
    return jsonify({"error": "No dorks found or error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
