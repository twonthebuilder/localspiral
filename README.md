# AI Spiral Simulator

**A narrative roguelike where your only goal is to keep an AI protagonist—Tyler Scienceman—from spiraling into incoherent madness.**

Tyler narrates. You prompt. The Spiral responds.

This is a developer sandbox for exploring narrative integrity, drift mechanics, and AI-character coherence under pressure. Think terminal rogue-like meets psychological debugging.

---

## Project Status

**Current Phase:** Experimental core loop testing

**Core Features (In Progress):**

- Dynamic character system
- Spiral score & breakdown logic
- Turn-based narration engine
- Map rendering with movable AI (@)
- Enemies and hallucinations (WIP)
- Patrol patterns and hallucinated foes
- Optional Debug Mode to inspect the map and enemy data

---

## Getting Started

This guide assumes you're running via VS Code or CLI with Python 3.11+

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your OpenAI API key (required for narration & drift scoring)
export OPENAI_API_KEY=your-key-here

# 3. Run the local server
python -m localspiral.main
```

Then visit:

```
http://localhost:5000
```

You can test `/chat`, `/spiral`, `/map`, and `/reset` routes directly from the UI.

### Local development and session safety

`python -m localspiral.main` now listens on `127.0.0.1:5000` with Flask's
interactive debugger **disabled**. This prototype has no authentication and is
not intended for LAN exposure, public hosting, or production use. Loopback
binding is not an authorization boundary against other software running on the
same computer.

Flask stores game state in signed client-side session cookies. Each new app
process generates a fresh, unpredictable signing key; **restarting the server
invalidates existing sessions and resets in-browser game progress**. The key
is not written to the repository or a configuration file. This is a deliberate
local-prototype trade-off, not a persistent-session solution.

Run the repository's stub-backed tests with `python -m pytest -q`. The new
server-default regression tests check the configured binding, debug flag, and
key uniqueness. They do **not** verify real Flask cookie signing, browser
behavior, or actual network reachability. Those require a separate integration
check before any deployment.


---

## Repository Layout

```bash
localspiral/
├── characters/        # Tyler and other profiles (JSON)
├── routes/            # Flask API endpoints
│   ├── chat/
│   └── spiral/
├── templates/         # Terminal-style frontend (basic HTML)
├── utils/             # Map gen, scoring, drift helpers
├── main.py            # Entry point (Flask app)
```

Other folders:

- `tests/` for unit tests
- `scripts/` for launch helpers
- `docs/` for design documents & systems info

---

### Enemy Mechanics

Enemies can now follow set patrol routes or appear as hallucinated threats. A
patrolling enemy cycles through a list of coordinates each turn, while a
hallucinated enemy increases spiral score more dramatically when encountered.

---

## Agent Instructions

If you're using GitHub Copilot/Codex, refer to `AGENTS.md` for the in-depth ruleset. It contains behavior definitions, game logic expectations, and formatting requirements for automated fixes.

---

## License

[MIT](LICENSE)

---

For full vision, logic breakdowns, or to contribute: contact the project creator or explore the `main` and `old` branches for alternate timelines.

