# Running Telegram Marketplace Bot Offline

This guide explains how to download, set up, and run this Telegram bot project on your local machine or any server outside of Replit.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your machine:

### 1. **Python 3.10 or higher**
```bash
# Check if Python is installed
python --version
# or
python3 --version

# Should output: Python 3.10.x or higher
```

**Installation:**
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python@3.11`
- **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install python3 python3-pip`
- **Linux (Fedora)**: `sudo dnf install python3 python3-pip`

### 2. **PostgreSQL Database**
You need a PostgreSQL database server (version 12 or higher).

**Installation:**
- **Windows**: Download from [postgresql.org](https://www.postgresql.org/download/windows/)
- **macOS**: `brew install postgresql@15`
- **Linux (Ubuntu/Debian)**: `sudo apt install postgresql postgresql-contrib`
- **Linux (Fedora)**: `sudo dnf install postgresql-server postgresql-contrib`

**After installation, start PostgreSQL:**
```bash
# macOS
brew services start postgresql@15

# Linux (Ubuntu/Debian)
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Windows - PostgreSQL runs as a service automatically
```

### 3. **Git** (to download the project)
```bash
# Check if Git is installed
git --version
```

**Installation:**
- **Windows**: Download from [git-scm.com](https://git-scm.com/download/win)
- **macOS**: `brew install git` or comes with Xcode
- **Linux**: `sudo apt install git` or `sudo dnf install git`

### 4. **pip** (Python package manager)
Usually comes with Python. Verify:
```bash
pip --version
# or
pip3 --version
```

### 5. **Virtual Environment** (recommended)
```bash
# Install virtualenv if not present
pip install virtualenv
```

---

## 📥 Step 1: Download the Project

### Option A: Download from Replit

If you're currently on Replit and want to move offline:

1. **Using Replit's Download Feature** (Explorer/Core users):
   - Click the three dots menu (⋮) in the Files panel
   - Select "Download as ZIP"
   - Extract the ZIP file on your local machine

2. **Using Git** (if you have a Git repository connected):
   ```bash
   git clone <your-repository-url>
   cd <project-folder>
   ```

### Option B: Manual File Download

If downloading individual files:
1. Download all `.py` files from your Replit project
2. Download `pyproject.toml` and `uv.lock`
3. Download all `.md` files (optional, for documentation)
4. Create the same folder structure locally

---

## 🗄️ Step 2: Set Up PostgreSQL Database

### Create a Database

1. **Access PostgreSQL** (as postgres user):
```bash
# Linux/macOS
sudo -u postgres psql

# Windows (in PowerShell or CMD as admin)
psql -U postgres
```

2. **Create Database and User**:
```sql
-- Create a database
CREATE DATABASE telegram_marketplace;

-- Create a user (replace 'yourpassword' with a strong password)
CREATE USER bot_user WITH PASSWORD 'yourpassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE telegram_marketplace TO bot_user;

-- Exit psql
\q
```

3. **Note your database connection details**:
   - Host: `localhost` (or `127.0.0.1`)
   - Port: `5432` (default)
   - Database: `telegram_marketplace`
   - User: `bot_user`
   - Password: (your chosen password)

---

## 🔧 Step 3: Set Up Python Environment

### 1. Navigate to Project Directory
```bash
cd /path/to/your/project
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv
# or
python3 -m venv venv
```

### 3. Activate Virtual Environment

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` prefix in your terminal.

### 4. Install Dependencies

**Option A: Using pip directly**
```bash
pip install python-telegram-bot telethon psycopg2-binary python-dotenv schedule
```

**Option B: Using requirements file**

First, create a `requirements.txt` file:
```txt
python-telegram-bot==20.7
telethon==1.35.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
schedule==1.2.0
```

Then install:
```bash
pip install -r requirements.txt
```

---

## 🔑 Step 4: Configure Environment Variables

### 1. Create `.env` file

In your project root, create a file named `.env`:

```bash
# Linux/macOS
touch .env

# Windows
type nul > .env
```

### 2. Add Configuration to `.env`

Open `.env` in a text editor and add:

```env
# Telegram Bot Configuration
BOT_TOKEN=your_bot_token_here
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here

# Admin Configuration (comma-separated Telegram user IDs)
ADMIN_IDS=123456789,987654321

# Database Configuration
DATABASE_URL=postgresql://bot_user:yourpassword@localhost:5432/telegram_marketplace

# Optional: Bot Configuration
ACCOUNT_PRICE=10.00
MIN_WITHDRAWAL=5.00
REFERRAL_COMMISSION=0.10
```

### 3. Get Required Credentials

#### Get Telegram Bot Token:
1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow instructions to create your bot
4. Copy the token provided

#### Get Telegram API ID and Hash:
1. Visit [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create an app (if you haven't)
5. Copy `api_id` and `api_hash`

#### Get Your Admin User ID:
1. Search `@userinfobot` on Telegram
2. Send `/start`
3. Copy your user ID

---

## 🗃️ Step 5: Initialize the Database

### 1. Run Database Initialization

The database schema will be created automatically when you first run the bot. However, you need to set up the first admin user.

### 2. Add Your First Admin

**Option A: Using SQL directly**
```bash
# Connect to database
psql -U bot_user -d telegram_marketplace -h localhost

# Then run:
INSERT INTO admins (user_id, username, role, is_active)
VALUES (YOUR_TELEGRAM_USER_ID, 'your_username', 'admin', TRUE);

# Exit
\q
```

**Option B: Using the setup script**

If you have `setup_admin.py`, you can modify it to add your admin:
```bash
python setup_admin.py
```

---

## 🚀 Step 6: Run the Bot

### 1. Start the Main Bot

```bash
# Make sure virtual environment is activated
python main.py
# or
python bot.py
```

You should see:
```
Bot started successfully!
Polling for updates...
```

### 2. Test the Bot

1. Open Telegram
2. Search for your bot by username
3. Send `/start`
4. You should see the seller menu

### 3. Keep Bot Running (Production)

For production deployment, you need a process manager to keep the bot running 24/7.

---

## 🔄 Step 7: Set Up Background Services (Optional)

### For Daily Reports and Account Monitoring

You have two background schedulers:
1. `run_scheduler.py` - Daily reports at midnight
2. `account_monitor_scheduler.py` - Account checking every 6 hours

### Option A: Run in Separate Terminal Sessions

**Terminal 1: Main Bot**
```bash
python main.py
```

**Terminal 2: Daily Report Scheduler**
```bash
python run_scheduler.py
```

**Terminal 3: Account Monitor**
```bash
python account_monitor_scheduler.py
```

### Option B: Use `screen` (Linux/macOS)

```bash
# Install screen
sudo apt install screen  # Ubuntu/Debian
brew install screen       # macOS

# Start main bot
screen -S telegram-bot
python main.py
# Press Ctrl+A, then D to detach

# Start daily reports
screen -S daily-reports
python run_scheduler.py
# Press Ctrl+A, then D to detach

# Start account monitor
screen -S account-monitor
python account_monitor_scheduler.py
# Press Ctrl+A, then D to detach

# List all sessions
screen -ls

# Reattach to a session
screen -r telegram-bot
```

### Option C: Use systemd (Linux - Recommended for Production)

Create service files for each process:

**1. Main Bot Service** (`/etc/systemd/system/telegram-bot.service`):
```ini
[Unit]
Description=Telegram Marketplace Bot
After=network.target postgresql.service

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/your/project/venv/bin"
ExecStart=/path/to/your/project/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**2. Daily Reports Service** (`/etc/systemd/system/telegram-reports.service`):
```ini
[Unit]
Description=Telegram Bot Daily Reports
After=network.target postgresql.service

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/your/project/venv/bin"
ExecStart=/path/to/your/project/venv/bin/python run_scheduler.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**3. Account Monitor Service** (`/etc/systemd/system/telegram-monitor.service`):
```ini
[Unit]
Description=Telegram Account Monitor
After=network.target postgresql.service

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/your/project/venv/bin"
ExecStart=/path/to/your/project/venv/bin/python account_monitor_scheduler.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Enable and start services:**
```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable services to start on boot
sudo systemctl enable telegram-bot
sudo systemctl enable telegram-reports
sudo systemctl enable telegram-monitor

# Start services
sudo systemctl start telegram-bot
sudo systemctl start telegram-reports
sudo systemctl start telegram-monitor

# Check status
sudo systemctl status telegram-bot
sudo systemctl status telegram-reports
sudo systemctl status telegram-monitor

# View logs
sudo journalctl -u telegram-bot -f
```

### Option D: Use Supervisor (Cross-platform)

```bash
# Install supervisor
pip install supervisor

# Create supervisor config file
sudo nano /etc/supervisor/conf.d/telegram-bot.conf
```

Add:
```ini
[program:telegram-bot]
command=/path/to/venv/bin/python /path/to/project/main.py
directory=/path/to/project
user=your_username
autostart=true
autorestart=true
stderr_logfile=/var/log/telegram-bot.err.log
stdout_logfile=/var/log/telegram-bot.out.log

[program:telegram-reports]
command=/path/to/venv/bin/python /path/to/project/run_scheduler.py
directory=/path/to/project
user=your_username
autostart=true
autorestart=true
stderr_logfile=/var/log/telegram-reports.err.log
stdout_logfile=/var/log/telegram-reports.out.log

[program:telegram-monitor]
command=/path/to/venv/bin/python /path/to/project/account_monitor_scheduler.py
directory=/path/to/project
user=your_username
autostart=true
autorestart=true
stderr_logfile=/var/log/telegram-monitor.err.log
stdout_logfile=/var/log/telegram-monitor.out.log
```

Then:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
sudo supervisorctl status
```

---

## 🌐 Deployment Options

### 1. **Local Machine / Home Server**
- Best for: Testing, development, personal use
- Pros: Full control, no hosting costs
- Cons: Requires 24/7 uptime, stable internet, IP address changes

### 2. **Virtual Private Server (VPS)**
Popular providers:
- **DigitalOcean** ($6-12/month) - Simple droplets
- **Linode** ($5-10/month) - Good performance
- **Vultr** ($5-12/month) - Global locations
- **AWS EC2** ($5-20/month) - Scalable
- **Google Cloud** ($5-20/month) - Free tier available
- **Hetzner** ($4-10/month) - Cheap in Europe

**Setup on VPS:**
1. Choose Ubuntu 22.04 or Debian 11
2. SSH into server: `ssh root@your-server-ip`
3. Follow all steps above
4. Use systemd for process management
5. Set up firewall: `sudo ufw allow 22/tcp` (SSH only)

### 3. **Cloud Platforms**
- **Heroku** - Easy deployment, has free PostgreSQL
- **Railway** - Modern, simple deployment
- **Render** - Good for Python apps
- **Google Cloud Run** - Serverless option

### 4. **Dedicated Server**
For high-traffic bots:
- More resources
- Better performance
- Higher cost ($30-100+/month)

---

## 🔒 Security Recommendations

### 1. Firewall Configuration
```bash
# Ubuntu/Debian
sudo ufw enable
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 5432/tcp  # PostgreSQL (if remote)
sudo ufw status
```

### 2. PostgreSQL Security
```bash
# Edit PostgreSQL config
sudo nano /etc/postgresql/*/main/pg_hba.conf

# Only allow local connections
# Change:
# host    all             all             0.0.0.0/0            md5
# To:
# host    all             all             127.0.0.1/32         md5

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### 3. Environment Variables
- Never commit `.env` file to Git
- Use strong passwords for database
- Keep API tokens secure
- Rotate credentials regularly

### 4. Regular Updates
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Update Python packages
pip install --upgrade pip
pip list --outdated
```

### 5. Database Backups
```bash
# Create backup script
nano backup.sh
```

Add:
```bash
#!/bin/bash
BACKUP_DIR="/home/your_user/backups"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

# Backup database
pg_dump -U bot_user telegram_marketplace > $BACKUP_DIR/backup_$DATE.sql

# Keep only last 7 days of backups
find $BACKUP_DIR -name "backup_*.sql" -mtime +7 -delete
```

Make executable:
```bash
chmod +x backup.sh
```

Add to crontab (run daily at 2 AM):
```bash
crontab -e
# Add:
0 2 * * * /home/your_user/backup.sh
```

---

## 🐛 Troubleshooting

### Bot doesn't start
```bash
# Check Python version
python --version

# Check if all dependencies installed
pip list

# Check .env file exists and has correct values
cat .env

# Check database connection
psql -U bot_user -d telegram_marketplace -h localhost
```

### Database connection errors
```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql

# Check PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql-*-main.log

# Test connection manually
psql "postgresql://bot_user:password@localhost:5432/telegram_marketplace"
```

### Bot stops unexpectedly
```bash
# Check system logs
journalctl -u telegram-bot -n 100

# Check disk space
df -h

# Check memory usage
free -h

# Check Python errors
python main.py  # Run in foreground to see errors
```

### Dependencies issues
```bash
# Reinstall all dependencies
pip install --force-reinstall -r requirements.txt

# Or install one by one
pip install --upgrade python-telegram-bot
pip install --upgrade telethon
# etc.
```

---

## 📊 Monitoring

### Check Bot Status
```bash
# Using systemd
sudo systemctl status telegram-bot

# Using supervisor
sudo supervisorctl status telegram-bot

# Check if process is running
ps aux | grep python
```

### View Logs
```bash
# Systemd logs
sudo journalctl -u telegram-bot -f

# Supervisor logs
sudo tail -f /var/log/telegram-bot.out.log

# Custom log file (if you added logging)
tail -f bot.log
```

### Database Monitoring
```bash
# Connect to database
psql -U bot_user -d telegram_marketplace

# Check table sizes
SELECT pg_size_pretty(pg_total_relation_size('users')) as users_size,
       pg_size_pretty(pg_total_relation_size('sold_accounts')) as accounts_size;

# Count records
SELECT 'users' as table_name, COUNT(*) FROM users
UNION ALL
SELECT 'sold_accounts', COUNT(*) FROM sold_accounts
UNION ALL
SELECT 'withdrawals', COUNT(*) FROM withdrawals;
```

---

## 🔄 Updating the Bot

```bash
# Pull latest changes (if using Git)
git pull origin main

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart services
sudo systemctl restart telegram-bot
sudo systemctl restart telegram-reports
sudo systemctl restart telegram-monitor
```

---

## 📈 Performance Optimization

### For High Traffic

1. **Use PostgreSQL connection pooling**
2. **Add Redis for caching** (optional)
3. **Increase PostgreSQL max connections**
4. **Use multiple bot instances** with webhooks
5. **Optimize database queries** with indexes

### Database Optimization
```sql
-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_user_id ON users(user_id);
CREATE INDEX IF NOT EXISTS idx_sold_accounts_status ON sold_accounts(status);
CREATE INDEX IF NOT EXISTS idx_withdrawals_status ON withdrawals(status);
CREATE INDEX IF NOT EXISTS idx_saas_orders_user ON saas_orders(user_id);
CREATE INDEX IF NOT EXISTS idx_saas_orders_status ON saas_orders(status);
```

---

## ✅ Quick Start Summary

1. **Install**: Python 3.10+, PostgreSQL, Git
2. **Download**: Clone or download project files
3. **Database**: Create PostgreSQL database and user
4. **Setup**: Create virtual environment, install dependencies
5. **Configure**: Create `.env` file with credentials
6. **Initialize**: Run bot to create database schema
7. **Admin**: Add your first admin user
8. **Run**: Start main bot with `python main.py`
9. **Background**: Start schedulers (optional)
10. **Test**: Open Telegram and test bot

---

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review error logs carefully
3. Verify all prerequisites are installed
4. Ensure database is running and accessible
5. Check that all environment variables are set correctly

---

## 🎉 You're Ready!

Your Telegram Marketplace Bot is now running offline. Make sure to:
- ✅ Keep your server running 24/7
- ✅ Monitor logs regularly
- ✅ Backup database daily
- ✅ Update dependencies periodically
- ✅ Secure your server properly

Happy bot running! 🤖
