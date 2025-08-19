# TelegramBot

A Telegram bot built with modern technologies and Supabase as the database backend.

## Features

- 🤖 Telegram Bot API integration
- 📊 Supabase database for data persistence
- 🔒 Secure environment configuration
- 📝 Extensible command system
- 🚀 Easy deployment setup

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Telegram Bot Token (from @BotFather)
- Supabase account and project

## Setup

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd TelegramBot
npm install
```

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_KEY=your_supabase_service_role_key

# Optional: Environment
NODE_ENV=development
```

### 3. Supabase Setup

1. Create a new project at [supabase.com](https://supabase.com)
2. Set up your database tables as needed
3. Copy your project URL and API keys to the `.env` file

### 4. Telegram Bot Setup

1. Message @BotFather on Telegram
2. Create a new bot with `/newbot`
3. Copy the bot token to your `.env` file

## Usage

### Development

```bash
npm run dev
```

### Production

```bash
npm start
```

## Project Structure

```
TelegramBot/
├── src/
│   ├── commands/          # Bot command handlers
│   ├── middleware/        # Custom middleware
│   ├── utils/            # Utility functions
│   ├── database/         # Supabase database operations
│   └── bot.js            # Main bot configuration
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── package.json         # Dependencies and scripts
└── README.md           # This file
```

## Available Commands

Document your bot commands here as you build them:

- `/start` - Welcome message and bot introduction
- `/help` - Display available commands
- Add more commands as you develop them...

## Database Schema

Document your Supabase tables here:

```sql
-- Example table structure
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  telegram_id BIGINT UNIQUE NOT NULL,
  username VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Specify your license here]

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Built with ❤️ using Telegram Bot API and Supabase
