Bailey Butler

Software Engineer @ ANZx

Melbourne, Australia

[linkedin.com/in/baileybutler1](https://linkedin.com/in/baileybutler1) |
[blog.baileys.dev](https://blog.baileys.dev)

---

## Current Projects 

### 🏢 Office Tracker

__[Repo](https://github.com/baely/officetracker) | [Live Service](https://iwasintheoffice.com)__ (requires login via GitHub SSO)

Web app for tracking compliance with RTO mandates. Provides a simple calendar
interface for users to log their office presence, and returns summary stats and
reports for assessing compliance.

Tech: Go, vanilla JS, Postgres (hosted solution)/SQLite (standalone instance), Google Cloud Run.

### 💸 Txn - Financial Transaction Tracker

__[Repo](https://github.com/baely/txn)__

A unified event-driven application that monitors my banking activity through the Up Banking API to provide useful insights and automated notifications:

- **[IsBaileyButlerInTheOffice.Today?](https://isbaileybutlerintheoffice.today)** - Automatically detects coffee purchases to determine my presence in the office.

- **[Bailey Needs Coffee](https://baileyneeds.coffee)** - Tracks my caffeine consumption patterns over time, providing insights into my coffee spending habits and consumption frequency with visual analytics.

- **[Events API](https://events.baileys.dev)** - Serves as the central hub for processing webhook events from Up Banking and distributing transaction data to the other services.

The system instantly updates my office presence status when I buy coffee nearby and sends notifications to Slack, streamlining team coordination without manual input.

Tech:
- Go backend with domain-based routing
- Structured logging and standardized error handling
- PostgreSQL for data persistence
- Dockerised deployment
- Slack integration for real-time notifications

### ⚙️ Infrastructure

__[Repo](https://github.com/baely/infra)__

Self-hosted infrastructure as code. It is mostly Kubernetes manifests for now.
There is more IaaC related to networking - but I am in the process of cleaning
up my ingress.

Tech: Kubernetes

### 📝 Blog

__[Repo](https://github.com/baely/blog) | [Live Blog](https://blog.baileys.dev)__

Blog with a focus on tech and personal projects.

Tech: Hugo (Go)

### 🧩 Advent of Code

__[Repo](https://github.com/baely/advent-of-code)__

My Python solutions to the annual Advent of Code challenges.

## Previous Projects

- [devhou.se jp blog](https://github.com/devhou-se/www-jp) - blogging platform built on github issues /w auto-translation for publishing posts into japanese. (view the blog here: [https://devhou.se](https://devhou.se))
- [sreetcode / sreeifier](https://github.com/devhou-se/sreetcode) - service for proxying web pages and doing basic text find and replaces. service is no longer active due to operational costs
- [msfs](https://github.com/baely/go-msfs) - a set of services for live tracking my sim flights in microsoft flight simulator. (live track my flights here: [https://projects.xbd.au/pilot](https://projects.xbd.au/pilot))
