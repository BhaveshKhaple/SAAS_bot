# Telegram Marketplace Bot - Project Structure

**Last Updated**: November 9, 2025

## 📁 Directory Structure

```
telegram-marketplace-bot/
│
├── 📄 Core Configuration Files
│   ├── bot.py                          # Main bot entry point
│   ├── main.py                         # Alternative entry point
│   ├── config.py                       # Configuration and environment variables
│   ├── database.py                     # Database connection and schema
│   ├── pyproject.toml                  # Python dependencies (uv/pip)
│   ├── uv.lock                         # Locked dependencies
│   │
├── 🐳 Docker & Deployment
│   ├── Dockerfile                      # Production Docker image
│   ├── docker-compose.yml              # Multi-container orchestration
│   ├── .dockerignore                   # Docker build exclusions
│   ├── .env.example                    # Environment variables template
│   │
├── 👤 Seller Features (Account Selling)
│   ├── account_seller.py               # Account selling conversation flow
│   ├── seller_profile.py               # Seller profile management
│   ├── seller_withdrawals.py           # Withdrawal requests
│   │
├── 💎 Buyer Features (SaaS Services)
│   ├── buyer_menu.py                   # Buyer interface
│   ├── buy_plan.py                     # Plan purchase system
│   ├── deposit_menu.py                 # Deposit & payment system
│   ├── plan_management.py              # Active plan management
│   ├── buyer_referral_program.py       # Buyer referral system
│   ├── buyer_referral_withdrawals.py   # Buyer referral payouts
│   ├── reseller_panel.py               # Reseller interface
│   │
├── 👔 Admin Features
│   ├── admin_controls.py               # Core admin commands
│   ├── admin_reporting.py              # User statistics & reports
│   ├── admin_rate_management.py        # SaaS pricing management
│   ├── admin_deposit_management.py     # Payment verification
│   ├── admin_reseller_management.py    # Reseller approval
│   ├── saas_admin_reports.py           # SaaS analytics
│   ├── broadcast_admin.py              # Broadcast messaging
│   ├── promo_code_management.py        # Promo code system
│   │
├── 🤖 Account Pool & Automation
│   ├── account_pool_manager.py         # Account inventory management
│   ├── account_status_checker.py       # Account ban detection
│   ├── account_monitor_scheduler.py    # Scheduled monitoring
│   ├── service_delivery_worker.py      # Engagement delivery engine
│   ├── plan_expiry_handler.py          # Plan expiration automation
│   │
├── ⏰ Background Workers
│   ├── daily_report.py                 # Daily statistics report
│   ├── run_scheduler.py                # Scheduler runner
│   ├── notification_system.py          # Consolidated notifications
│   │
├── 🛠️ Utilities
│   ├── setup_admin.py                  # Admin setup utility
│   │
├── 📚 Documentation
│   ├── README.md                       # Project overview & setup
│   ├── replit.md                       # Complete project documentation
│   ├── TESTING_GUIDE.md                # Comprehensive testing procedures
│   ├── FEATURE_STATUS.md               # Feature implementation status
│   ├── PROJECT_STRUCTURE.md            # This file
│   ├── fixtodo.md                      # Bug tracking & issues log
│   ├── PHASE_4_SUMMARY.md              # Phase 4 completion summary
│   ├── PHASE_5_SUMMARY.md              # Phase 5 completion summary
│   ├── PHASE_10_GUIDE.md               # Phase 10 implementation guide
│   │
├── 📂 Created Directories
│   ├── src/                            # Source code (for future refactoring)
│   │   ├── handlers/                   # Handler modules
│   │   ├── admin/                      # Admin modules
│   │   ├── database/                   # Database modules
│   │   ├── services/                   # Business logic services
│   │   └── utils/                      # Utility functions
│   ├── docs/                           # Additional documentation
│   ├── logs/                           # Application logs (gitignored)
│   ├── sessions/                       # Telegram session files (gitignored)
│   ├── backups/                        # Database backups (gitignored)
│   │
└── 📦 Replit & Development
    ├── .replit                         # Replit configuration
    ├── replit.nix                      # Nix environment (if exists)
    ├── .local/                         # Local state & tracking
    └── attached_assets/                # Pasted files & attachments
```

## 🗂️ File Organization by Feature

### Account Selling Workflow
```
account_seller.py           → Phone submission, OTP, 2FA
seller_profile.py           → Balance, stats, payout info
seller_withdrawals.py       → Withdrawal requests
```

### SaaS Buyer System
```
buyer_menu.py               → Main buyer interface
buy_plan.py                 → Plan selection & purchase
deposit_menu.py             → Payment methods (UPI, Promo, etc.)
plan_management.py          → View, renew, cancel plans
buyer_referral_program.py   → Referral link generation
buyer_referral_withdrawals.py → Referral earnings withdrawal
reseller_panel.py           → Custom plan links & margins
```

### Admin Management
```
admin_controls.py           → User management (ban, unban, etc.)
admin_reporting.py          → User stats, system stats
admin_rate_management.py    → Set SaaS rates (views, reactions)
admin_deposit_management.py → Verify payments (UPI, etc.)
admin_reseller_management.py → Approve resellers
saas_admin_reports.py       → Revenue, sales, CSV exports
broadcast_admin.py          → Broadcast messages to users
promo_code_management.py    → Create/delete promo codes
```

### Automation & Workers
```
account_status_checker.py      → Check accounts for bans (Telethon)
account_monitor_scheduler.py   → Schedule checks every 6 hours
service_delivery_worker.py     → Deliver views/reactions
plan_expiry_handler.py         → Handle expired plans
daily_report.py                → Generate daily admin reports
run_scheduler.py               → Run scheduled tasks
notification_system.py         → Send notifications to users/admins
```

## 📊 Database Schema (database.py)

### Tables
1. **users** - User accounts, balances, referrals
2. **admins** - Administrator accounts
3. **sold_accounts** - Telegram account pool
4. **withdrawals** - Seller withdrawal requests
5. **settings** - System configuration
6. **saas_orders** - Service orders (views/reactions)
7. **saas_rates** - Pricing configuration
8. **promo_codes** - Discount codes
9. **promo_code_usage** - Redemption tracking
10. **buyer_referrals** - Buyer referral tracking
11. **resellers** - Reseller program
12. **deposits** - Payment tracking
13. **account_usage_logs** - Account delivery tracking
14. **admin_logs** - Admin action audit trail

## 🐳 Docker Deployment

### Files
- **Dockerfile** - Production-ready multi-stage build
- **docker-compose.yml** - Full stack deployment (bot + database + workers)
- **.dockerignore** - Exclude unnecessary files from image
- **.env.example** - Environment variables template

### Services (docker-compose.yml)
1. **postgres** - PostgreSQL database
2. **bot** - Main Telegram bot
3. **account_checker** - Background account monitor
4. **daily_report** - Scheduled report generator

## 📝 Configuration Files

### Python
- **pyproject.toml** - Dependencies managed by `uv`
- **uv.lock** - Locked dependency versions

### Environment
- **.env.example** - Template for environment variables
- **config.py** - Load and validate environment variables

### Replit
- **.replit** - Workflow configuration
- **replit.nix** - Nix package specification (if exists)

## 🚀 Deployment Options

### Option 1: Replit (Current)
- Native Nix environment
- Workflow-based execution
- Managed PostgreSQL
- **No Docker support**

### Option 2: Docker (Portable)
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f bot

# Stop services
docker-compose down
```

### Option 3: Manual Deployment
```bash
# Install dependencies
uv sync

# Set environment variables
export BOT_TOKEN="your_token"
export TELEGRAM_API_ID="your_id"
export TELEGRAM_API_HASH="your_hash"
export ADMIN_IDS="123456789"
export DATABASE_URL="postgresql://..."

# Run bot
python bot.py
```

## 🔄 Future Refactoring Plan

### Proposed Structure (src/)
```
src/
├── __init__.py
├── bot/
│   ├── __init__.py
│   ├── main.py                 # Entry point
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── seller_handlers.py
│   │   ├── buyer_handlers.py
│   │   └── admin_handlers.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── account_service.py
│   │   ├── payment_service.py
│   │   └── notification_service.py
│   └── models/
│       ├── __init__.py
│       ├── user.py
│       ├── account.py
│       └── order.py
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── migrations/
│   └── queries/
├── workers/
│   ├── __init__.py
│   ├── account_checker.py
│   ├── delivery_worker.py
│   └── report_scheduler.py
└── utils/
    ├── __init__.py
    ├── validators.py
    └── formatters.py
```

## 📌 Notes

- **Current Structure**: All files in root directory (working and tested)
- **Docker Support**: Created but **won't run in Replit** (use for external deployment)
- **Future Refactoring**: Move to `src/` structure when time permits
- **Documentation**: Keep up-to-date with every major change

---

**Recommendation**: The current flat structure works well for the project size. Consider refactoring to `src/` structure if the project grows beyond 30-40 modules.
