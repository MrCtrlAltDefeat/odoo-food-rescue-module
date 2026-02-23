# 🥗 Food Waste to Food Plate — Odoo Module

> An Odoo 19 module that turns corporate kitchen surplus into community meals — tracking food batches, coordinating NGO pickups, and measuring real environmental impact.

---

## 📌 Overview

**Food Waste to Food Plate** is a custom Odoo module built to solve a real-world problem: businesses (hotels, corporate cafeterias, catering companies) regularly discard edible food that could be redirected to those in need.

This module integrates directly into Odoo's existing Sales, Inventory, and Website e-commerce ecosystem to create a seamless food redistribution pipeline — from batch intake, to NGO/employee receiver matching, to pickup scheduling and impact reporting.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🍱 **Food Batch Tracking** | Log incoming food batches with type, quantity, expiry date, and kitchen location |
| 📦 **Auto Stock Update** | On batch creation, inventory (`stock.quant`) is automatically updated — no manual warehouse entry needed |
| 🤝 **Receiver Management** | Register NGOs or employees as receivers with pickup capacity and contact info |
| 🚗 **Pickup Requests** | Schedule and assign pickups, linking batches to receivers and handlers |
| 📊 **Impact Dashboard** | Visual KPIs tracking meals saved, kg of waste avoided, and CO₂ emissions prevented |
| 🛒 **Website Integration** | Expose available food products on the Odoo e-commerce portal |
| 📧 **Email Notifications** | Automated mail templates notify receivers on pickup scheduling |
| ⏰ **Scheduled Actions** | Cron jobs auto-confirm free orders and process redistribution flows |
| 🖨️ **Pickup Report** | Printable PDF report for each pickup request |
| 🔐 **Role-Based Access** | Separate security groups for staff, NGO coordinators, and admins |

---

## 🏗️ Architecture

```
food_waste_to_food_plate/
├── models/
│   ├── food_batch.py          # Core batch model + auto stock.quant update
│   ├── receiver.py            # NGO/employee receiver profiles
│   ├── pickup.py              # Pickup request scheduling
│   ├── impact.py              # Impact log (meals saved, CO₂, kg waste)
│   ├── product_inherit.py     # Product extension for food tagging
│   └── sale_order_inherit.py  # Sales order extension for $0 redistribution
├── views/
│   ├── food_batch_views.xml   # Batch list/form views
│   ├── receiver_views.xml     # Receiver management UI
│   ├── pickup_views.xml       # Pickup scheduling UI
│   ├── impact_views.xml       # Impact log views
│   ├── dashboards.xml         # KPI dashboard
│   ├── product_template_views.xml
│   ├── website_product_views.xml
│   └── menu.xml               # App menu structure
├── report/
│   └── pickup_report.xml      # Printable pickup PDF
├── data/
│   ├── cron.xml               # Scheduled actions
│   ├── cron_free_orders.xml   # Auto-confirm $0 orders
│   ├── mail_templates.xml     # Email notification templates
│   └── demo_data.xml          # Demo records for testing
├── security/
│   ├── ir.model.access.csv    # Model-level CRUD permissions
│   └── security.xml           # Security groups definition
└── __manifest__.py
```

---

## 🔄 How It Works

```
Corporate Kitchen
      │
      ▼
 [Food Batch Created]
      │  (auto-updates stock.quant)
      ▼
 [Available in Inventory]
      │
      ▼
 [Pickup Request Created]
      │  (email sent to Receiver)
      ▼
 [NGO / Employee picks up food]
      │
      ▼
 [Impact Log recorded]
      │  (meals saved, CO₂, kg waste)
      ▼
 [Dashboard KPIs updated]
```

---

## 🛠️ Tech Stack

- **Platform:** [Odoo 19](https://www.odoo.com) (Community / Enterprise)
- **Language:** Python 3, XML, CSV
- **ORM:** Odoo ORM (PostgreSQL under the hood)
- **Modules Extended:** `sale`, `stock`, `product`, `website_sale`, `mail`

---

## 🚀 Installation

### Prerequisites
- Odoo 19 instance (local or hosted)
- Python 3.10+
- PostgreSQL

### Steps

1. **Clone this repository** into your Odoo addons directory:
   ```bash
   git clone https://github.com/YOUR_USERNAME/food_waste_to_food_plate.git /path/to/odoo/addons/food_waste_to_food_plate
   ```

2. **Restart Odoo** to discover the new module:
   ```bash
   ./odoo-bin -c odoo.conf -u all
   ```

3. **Activate developer mode** in Odoo:  
   Settings → General Settings → Activate Developer Mode

4. **Install the module:**  
   Apps → Search "Food Waste to Food Plate" → Install

5. *(Optional)* Load demo data via Settings → Technical → Sequences & Identifiers → Demo Data

---

## 📸 Screenshots

> *Add screenshots of your Odoo instance here once deployed.*

| Food Batch List | Pickup Scheduling | Impact Dashboard |
|---|---|---|
| ![batch](docs/screenshots/food_batch.png) | ![pickup](docs/screenshots/pickup.png) | ![dashboard](docs/screenshots/dashboard.png) |

---

## 📈 Impact Metrics Tracked

| Metric | How It's Calculated |
|---|---|
| 🍽️ Meals Saved | Quantity redistributed ÷ average meal size |
| ♻️ KG Waste Avoided | Direct weight of food redistributed |
| 🌍 CO₂ Saved | KG waste × CO₂ equivalent factor (food decomposition in landfill) |

---

## 🧪 Demo Data

The module ships with `demo_data.xml` containing sample food batches, receivers, and pickup requests so you can explore the full workflow immediately after installation.

---

## 🔐 Security Model

| Group | Permissions |
|---|---|
| `food_waste.group_user` | Read batches, create pickup requests |
| `food_waste.group_manager` | Full CRUD on all models, access reports |

---

## 🗺️ Roadmap

- [ ] SMS notifications for pickup reminders
- [ ] Mobile-friendly receiver portal (Odoo Website)
- [ ] Integration with Google Maps for pickup route optimization
- [ ] Monthly impact PDF report (auto-emailed to management)
- [ ] Barcode scanning for batch intake
- [ ] Multi-company support

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **LGPL-3.0** license — see [LICENSE](LICENSE) for details.

---

## 👤 Author

Built with ❤️ as part of an Odoo development workshop.

---

*If this module helped you, give it a ⭐ on GitHub!*
