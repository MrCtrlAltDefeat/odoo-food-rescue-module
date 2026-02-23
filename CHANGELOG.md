# Changelog

All notable changes to this project will be documented in this file.

## [19.0.0.1] - 2025

### Added
- `food_batch` model: log incoming food with type, quantity, expiry date, and kitchen location
- Auto-update of `stock.quant` on food batch creation — no manual warehouse entry needed
- `receiver` model: register NGOs and employees as redistribution receivers
- `pickup_request` model: schedule and assign food pickups
- `impact_log` model: track meals saved, kg waste avoided, CO₂ emissions prevented
- Impact KPI dashboard view
- Website/e-commerce product integration for available food listings
- Email notification templates for pickup scheduling
- Scheduled action (cron) to auto-confirm $0 redistribution orders
- Printable PDF report for pickup requests
- Role-based security groups (User / Manager)
- Demo data for out-of-the-box testing
