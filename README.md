# Echo (formerly hGod)

A Discord bot in development for server moderation and management.

## 📝 Project Status
**Work in Progress** - Currently implementing core moderation features.  
This bot is being built as a learning project to practice Python, Discord API, and Git workflow.

## 🎯 Planned Features
- Moderation commands: `/kick`, `/ban`, `/timeout`, `/warn`, `/mute`, `/purge`
- Member management: role assignment, nickname changes
- Server utilities: welcome/leave messages, logging
- Basic fun/utility commands ✅ (ping, hello, roll, 8ball implemented)

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
cd echo
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
- Copy `.env.example` to `.env` (or create new `.env`)
- Add your bot token: DISCORD_TOKEN=your_bot_token_here
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
The bot will connect to Discord, auto-load all commands from the `commands/` folder, and respond in your server.

### Current Commands
- `!ping` - Replies "Pong!"
- `!hello` - Greets the user
- `!roll [sides]` - Rolls a die (defaults to 6 sides)
- `!8ball` - Magic 8-ball style random response

## 📂 Project Structure
echo/
├── main.py # Bot entry point, loads all cogs from commands/
├── requirements.txt # Python dependencies
├── .env # Environment variables (gitignored)
├── .gitignore # Git ignore rules
├── README.md # This file
└── commands/ # Each file is a Cog holding one or more commands
├── init.py
├── ping.py
├── hello.py
├── roll.py
└── eightball.py

## 🔜 Next Steps
1. Add moderation command implementations
2. Add error handling and logging
3. Test in development server
4. Consider adding configuration for customizable prefixes/responses

## 🤝 Contributing
This is a personal learning project, but feedback is welcome!  
If you have suggestions for features or improvements, feel free to open an issue.

## 📄 License
MIT License - see `LICENSE` file for details (to be added).

---
*Echo is created by Hexarion as a learning project. Not affiliated with Discord Inc.*