# Docker Deployment Guide

**Telegram Marketplace Bot**  
**Last Updated**: November 9, 2025

## ⚠️ Important Notice

**Docker is NOT supported in Replit** - Replit uses Nix containerization. These Docker files are provided for **external deployment** on:
- AWS EC2, ECS, or Fargate
- Google Cloud Run or Compute Engine
- DigitalOcean Droplets or App Platform
- Your own VPS/dedicated server
- Any Docker-compatible hosting

## 🐳 What's Included

### Docker Files
1. **Dockerfile** - Multi-stage production build
2. **docker-compose.yml** - Complete stack with database and workers
3. **.dockerignore** - Optimized build context
4. **.env.example** - Environment variables template

### Architecture
```
┌─────────────────────────────────────────┐
│         Docker Compose Stack            │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────┐  ┌────────────────────┐  │
│  │PostgreSQL│◄─┤  Telegram Bot App  │  │
│  │ Database │  │  (Main Container)  │  │
│  └──────────┘  └────────────────────┘  │
│       ▲                                 │
│       │                                 │
│       ├─────────┤  Account Checker  │  │
│       │         │  (Worker 1)       │  │
│       │         └──────────────────┘  │
│       │                                 │
│       └─────────┤  Daily Reporter   │  │
│                 │  (Worker 2)       │  │
│                 └──────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker Engine 20.10+
- Docker Compose 2.0+
- Telegram Bot Token (@BotFather)
- Telegram API credentials (my.telegram.org)

### Step 1: Clone & Configure
```bash
# Clone your repository
git clone your-repo-url
cd telegram-marketplace-bot

# Copy environment template
cp .env.example .env

# Edit with your credentials
nano .env
```

### Step 2: Set Environment Variables
Edit `.env` file:
```bash
# Required - Get from @BotFather
BOT_TOKEN=7966652485:AAEHxxxxxxxxxxxxxxxxxx

# Required - Get from my.telegram.org
TELEGRAM_API_ID=12345678
TELEGRAM_API_HASH=abcdef1234567890abcdef1234567890

# Required - Your Telegram user ID (get from @userinfobot)
ADMIN_IDS=123456789,987654321

# Database credentials (change defaults!)
PGUSER=botuser
PGPASSWORD=your_secure_password_here
PGDATABASE=telegram_bot

# Optional settings
ACCOUNT_PRICE=10.00
MIN_WITHDRAWAL=5.00
REFERRAL_COMMISSION=0.10
```

### Step 3: Launch
```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Check status
docker-compose ps
```

### Step 4: Verify
```bash
# Check bot is running
docker-compose logs bot | grep "Bot started successfully"

# Check database connection
docker-compose logs bot | grep "Database connected"

# Test bot on Telegram
# Send /start to your bot
```

## 📦 Service Details

### Main Bot Container
- **Image**: Custom (built from Dockerfile)
- **Purpose**: Handle Telegram bot interactions
- **Port**: None (connects to Telegram API)
- **Dependencies**: PostgreSQL database
- **Auto-restart**: Yes

### PostgreSQL Database
- **Image**: postgres:15-alpine
- **Port**: 5432 (internal network only)
- **Data**: Persistent volume `postgres_data`
- **Backups**: Mounted to `./backups/`
- **Health check**: Every 10 seconds

### Account Checker Worker
- **Purpose**: Monitor account pool for bans
- **Schedule**: Every 6 hours
- **Auto-restart**: Yes

### Daily Reporter Worker
- **Purpose**: Send daily statistics to admins
- **Schedule**: Midnight UTC
- **Auto-restart**: Yes

## 🛠️ Management Commands

### Start Services
```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d bot
```

### Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (DANGER: deletes database!)
docker-compose down -v
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f bot
docker-compose logs -f postgres

# Last 100 lines
docker-compose logs --tail=100 bot
```

### Restart Services
```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart bot
```

### Execute Commands
```bash
# Open shell in bot container
docker-compose exec bot /bin/bash

# Run Python command
docker-compose exec bot python -c "import database; print('OK')"

# Access database
docker-compose exec postgres psql -U botuser -d telegram_bot
```

## 💾 Database Management

### Backup Database
```bash
# Create backup
docker-compose exec postgres pg_dump -U botuser telegram_bot > backups/backup_$(date +%Y%m%d).sql

# Or using the mounted volume
docker-compose exec postgres pg_dump -U botuser telegram_bot > /backups/backup.sql
```

### Restore Database
```bash
# Stop bot first
docker-compose stop bot account_checker daily_report

# Restore from backup
docker-compose exec -T postgres psql -U botuser telegram_bot < backups/backup_20251109.sql

# Restart services
docker-compose start bot account_checker daily_report
```

### Access Database
```bash
# PostgreSQL shell
docker-compose exec postgres psql -U botuser -d telegram_bot

# Run query
docker-compose exec postgres psql -U botuser -d telegram_bot -c "SELECT COUNT(*) FROM users;"
```

## 📊 Monitoring

### Health Checks
```bash
# Check container health
docker-compose ps

# Database health
docker-compose exec postgres pg_isready -U botuser
```

### Resource Usage
```bash
# View resource usage
docker stats

# Specific container
docker stats telegram-bot-app
```

### Logs
```bash
# Real-time logs
docker-compose logs -f

# Filter errors only
docker-compose logs | grep ERROR

# Export logs
docker-compose logs > logs/docker_$(date +%Y%m%d).log
```

## 🔄 Updates & Maintenance

### Update Code
```bash
# Pull latest code
git pull

# Rebuild containers
docker-compose build

# Restart with new code
docker-compose up -d
```

### Update Dependencies
```bash
# Edit pyproject.toml
nano pyproject.toml

# Rebuild
docker-compose build bot

# Restart
docker-compose restart bot
```

### Clean Up
```bash
# Remove stopped containers
docker-compose down

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune
```

## 🔒 Security Best Practices

### 1. Environment Variables
- ✅ Use `.env` file (never commit to git)
- ✅ Strong database passwords
- ✅ Rotate secrets regularly

### 2. Network Security
- ✅ Database not exposed to internet (internal network only)
- ✅ Non-root user in containers
- ✅ Read-only filesystem where possible

### 3. Data Protection
- ✅ Regular database backups
- ✅ Persistent volumes for critical data
- ✅ Logs with size rotation

### 4. Container Security
- ✅ Multi-stage builds (smaller attack surface)
- ✅ Minimal base image (python:3.11-slim)
- ✅ Health checks enabled

## 🌐 Production Deployment

### AWS EC2 Example
```bash
# SSH to EC2 instance
ssh -i key.pem ec2-user@your-instance-ip

# Install Docker
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone and deploy
git clone your-repo
cd telegram-marketplace-bot
cp .env.example .env
nano .env  # Edit credentials
docker-compose up -d
```

### DigitalOcean Droplet
```bash
# Create droplet with Docker pre-installed
# Or install manually:
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Deploy
git clone your-repo
cd telegram-marketplace-bot
cp .env.example .env
nano .env
docker-compose up -d
```

### Google Cloud Run
```bash
# Build image
gcloud builds submit --tag gcr.io/PROJECT-ID/telegram-bot

# Deploy
gcloud run deploy telegram-bot \
  --image gcr.io/PROJECT-ID/telegram-bot \
  --platform managed \
  --set-env-vars BOT_TOKEN=$BOT_TOKEN,TELEGRAM_API_ID=$TELEGRAM_API_ID
```

## 🐛 Troubleshooting

### Bot Not Starting
```bash
# Check logs
docker-compose logs bot

# Common issues:
# - Missing BOT_TOKEN
# - Database not ready
# - Invalid credentials
```

### Database Connection Error
```bash
# Check database is healthy
docker-compose ps postgres

# Check logs
docker-compose logs postgres

# Restart database
docker-compose restart postgres
```

### Container Crashes
```bash
# View crash logs
docker-compose logs --tail=100 bot

# Check health
docker-compose ps

# Restart
docker-compose restart bot
```

## 📞 Support

For issues with:
- **Docker setup**: Check this guide
- **Bot functionality**: See TESTING_GUIDE.md
- **Project structure**: See PROJECT_STRUCTURE.md
- **Bug reports**: See fixtodo.md

## ⚠️ Important Reminders

1. **NOT for Replit** - Use Replit's native workflow instead
2. **Backup regularly** - Database contains critical user data
3. **Secure secrets** - Never commit .env to git
4. **Monitor logs** - Watch for errors and warnings
5. **Update regularly** - Keep dependencies and Docker images current

---

**Note**: For Replit deployment, the bot is already running via the workflow system. Use these Docker files only when deploying to external servers.
