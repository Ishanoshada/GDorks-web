# GDorks Web

![Language](https://img.shields.io/badge/language-python-orange) ![License](https://img.shields.io/badge/license-MIT-green) ![GitHub Repo Size](https://img.shields.io/github/repo-size/Ishanoshada/GDorks-web) ![GitHub Issues](https://img.shields.io/github/issues/Ishanoshada/GDorks-web) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Ishanoshada/GDorks-web) ![GitHub Contributors](https://img.shields.io/github/contributors/Ishanoshada/GDorks-web) ![GitHub Last Commit](https://img.shields.io/github/last-commit/Ishanoshada/GDorks-web) ![GitHub Forks](https://img.shields.io/github/forks/Ishanoshada/GDorks-web?style=social) ![GitHub Stars](https://img.shields.io/github/stars/Ishanoshada/GDorks-web?style=social) ![GitHub Watchers](https://img.shields.io/github/watchers/Ishanoshada/GDorks-web?style=social)
[![Dorks](https://img.shields.io/badge/Dorks-Discover%20the%20Internet-blue)](https://img.shields.io/)

Welcome to **GDorks Web** — your gateway to discovering random Google Dorks straight from the [GDorks repository](https://github.com/Ishanoshada/GDorks)! This web application allows you to explore and retrieve Google Dorks (specific search queries) organized into categories, all powered by GitHub's repository contents.


Give us a ⭐️ if you find this project helpful!

### 🚀 [Live Demo](https://gdork-web.vercel.app/)

Check out the live version of **GDorks Web** hosted on Vercel!

## 🧑‍💻 Developed by:

**Ishan Oshada**, a passionate web developer and cybersecurity enthusiast from Sri Lanka. This project is built to combine my skills in Python, Flask, and web security!

Feel free to check out my GitHub: [@Ishanoshada](https://github.com/Ishanoshada).

## 🔑 Main GitHub Repository

The core data for the dorks is fetched from the official GDorks repository: [GDorks GitHub Repo](https://github.com/Ishanoshada/GDorks).

## 🌟 Features

- **Browse Categories**: View all available categories (folders) from the GDorks repository.
- **Get Random Dorks**: Select a category and retrieve random dorks from files within that category.
- **GitHub Integration**: Uses GitHub API to fetch data from the GDorks repository.
- **Asynchronous Requests**: Non-blocking requests using `aiohttp` for fetching data, ensuring a smooth user experience.

## ⚙️ Technologies Used

- **Flask**: A lightweight Python web framework for building the backend.
- **aiohttp**: Asynchronous HTTP client for making non-blocking requests to GitHub.
- **GitHub API**: Fetching dorks directly from the GDorks repository.
- **HTML/CSS/JS**: Frontend for displaying categories and dorks.
- **Python-dotenv**: Loading environment variables like GitHub Personal Access Token (PAT).
- **Vercel**: Deployment platform for hosting the web app.

## 💻 Installation

Follow the steps below to get this project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Ishanoshada/GDorks-web.git
```

### 2. Navigate to the Project Directory

```bash
cd GDorks-web
```

### 3. Set Up a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the root directory and add your GitHub Personal Access Token (PAT):

```ini
api/.env
    GITHUB_PAT=your_personal_access_token_here 
```

**Note**: You can create a GitHub Personal Access Token [here](https://github.com/settings/tokens).

### 7. Run the Flask Application

```bash
python api/index.py
```

Open your browser and go to `http://127.0.0.1:5000/` to access the app locally.

## 📱 Usage

1. **Choose a Category**: Type in the category you want (e.g., "CCTV").
2. **Specify the Number of Dorks**: Enter the number of random dorks you wish to retrieve.
3. **Explore Dorks**: View the selected category and the corresponding random dorks from the files in that category.


## Show Your Support

Give us a ⭐️ if GDorks has been your guide in the vast online landscape!

## Disclaimer

This list is for educational purposes only. Use Google dorks responsibly, respect privacy, intellectual property, and abide by all laws and regulations. Let's make the internet safer and more secure together!

Happy dorking! 🌟


**Repository Views** ![Views](https://profile-counter.glitch.me/GDorks/count.svg)

## Star History

<a href="https://star-history.com/#ishanoshada/GDorks&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ishanoshada/GDorks&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ishanoshada/GDorks&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ishanoshada/GDorks&type=Date" />
  </picture>
</a>


## 🤝 Contributing

I welcome contributions to improve this project! If you have ideas for new features or bug fixes, feel free to fork the repository and submit a pull request.

### How to Contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-xyz`).
3. Make your changes.
4. Commit and push your changes to your fork.
5. Submit a pull request.

## 🔒 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
