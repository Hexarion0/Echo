# hGod - Hexarion God

A Discord bot in development for server moderation and management.

## 📝 Project Status
**Work in Progress** - Currently implementing core moderation features.  
This bot is being built as a learning project to practice Python, Discord API, and Git workflow.

## 🎯 Planned Features
- Moderation commands: `/kick`, `/ban`, `/timeout`, `/warn`, `/mute`, `/purge`
- Member management: role assignment, nickname changes
- Server utilities: welcome/leave messages, logging
- Basic fun/utility commands (to be determined)

## 🛠️ Tech Stack
- **Language**: Python 3.8+
- **Library**: [discord.py](https://discordpy.readthedocs.io/)
- **Environment**: [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Version Control**: Git

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Discord account with server management permissions
- Bot token from [Discord Developer Portal](https://discord.com/developers/applications)

### Installation
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd hGod
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Copy `.env.example` to `.env` (or create new `.env`)
   - Add your bot token:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```
   - *Never commit your `.env` file - it's already in `.gitignore`*

4. **Enable required intents**
   - In Discord Developer Portal → your bot → Bot tab
   - Enable:
     - `SERVER MEMBERS INTENT`
     - `MESSAGE CONTENT INTENT` (required for command processing)
     - Other intents as needed for planned features

5. **Invite bot to your server**
   - Use the OAuth2 URL Generator in Developer Portal
   - Select `bot` scope and necessary permissions
   - Authorize in your target server

## ▶️ Usage
```bash
python main.py
```
The bot will connect to Discord and respond to commands in your server.

*Note: Command implementation is in progress - check `main.py` for current functionality.*

## 📂 Project Structure
```
hGod/
├── main.py          # Bot entry point
├── requirements.txt # Python dependencies
├── .env             # Environment variables (gitignored)
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## 🔜 Next Steps
1. Implement basic command structure with `discord.ext.commands`
2. Add moderation command implementations
3. Add error handling and logging
4. Test in development server
5. Consider adding configuration for customizable prefixes/responses

## 🤝 Contributing
This is a personal learning project, but feedback is welcome!  
If you have suggestions for features or improvements, feel free to open an issue.

## 📄 License
MIT License - see `LICENSE` file for details (to be added).

---
*hGod is created by Hexarion as a learning project. Not affiliated with Discord Inc.*
