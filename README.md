# PeerLens: Nifty 500 peer analysis

Pick an industry in the Nifty 500, choose 2 to 8 peers, and compare their profitability, debt and
efficiency. The app rates every ratio green, amber or red, ranks the peers, writes plain-language
recommendations for a focal company, and exports a live Excel dashboard.

## Run it on your computer
```bash
pip install -r requirements.txt
streamlit run app.py
```

## MCP server — run PeerLens as an agent tool
`mcp_server.py` exposes the same analysis engine, Excel exporter, macro module and synthetic trading
desk as six MCP tools — no Streamlit, no browser. Any MCP-capable chatbot or agent (Claude Desktop,
Claude Code, Claude.ai via a remote connector, Cursor, or anything else that speaks MCP) can call it
directly, which is what makes the "agent does the analyst work" workflow possible: point an agent at
it, ask for an industry comparison, and it chains the calls itself.

**Run it**
```bash
pip install -r requirements.txt
python mcp_server.py              # stdio — for Claude Desktop, Claude Code, most local clients
python mcp_server.py --http --port 8000   # streamable HTTP — for remote/web clients
```

**Tools**
| Tool | What it does |
|---|---|
| `list_industries` | Every Nifty 500 industry and its peer count — call this first |
| `list_companies` | Companies + NSE symbols in one industry |
| `run_peer_analysis` | Full ratio analysis: health score, rank, weaknesses with peer-median context and a recommended action each, strengths |
| `export_excel_workbook` | The same analysis saved as a live Excel workbook (formulas, not static numbers); returns the file path |
| `macro_outlook` | GDP sensitivity per company plus a plain-language headline (synthetic data only) |
| `trading_desk_snapshot` | The synthetic market + all four trading bots' P&L, with the HFT bot's live order log |

Every tool defaults to `mode="synthetic"` — instant, deterministic, fully offline. Pass
`mode="live"` to pull real Yahoo Finance statements instead (needs internet; never invents a missing
number). Excel files are written to `./exports/` by default; set `PEERLENS_EXPORT_DIR` to change that.

**Claude Desktop / Cursor / any client using the standard `mcpServers` config** — add to its config file:
```json
{
  "mcpServers": {
    "peerlens": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"]
    }
  }
}
```
Use the full path to the Python that has `requirements.txt` installed (a venv's `python` if you used
one) and an absolute path to `mcp_server.py` — the server adds its own folder to `sys.path`, so it
works from any working directory the client launches it from.

**Claude Code**
```bash
claude mcp add peerlens -- python /absolute/path/to/mcp_server.py
```

**A remote/browser-based chatbot with no local process access** needs the `--http` server reachable
over the network (a VPS, or a tunnel like `ngrok http 8000` for a quick test), pointed at
`http://<host>:<port>/mcp`.

## Deploy on Streamlit Community Cloud (free)
1. Create a new public GitHub repository and upload everything in this folder (keep the folder structure,
   including `data/`, `peerlens/` and `.streamlit/`).
2. Go to https://share.streamlit.io, sign in with GitHub, click **Create app**.
3. Choose the repository, branch `main`, main file `app.py`, then **Deploy**.

## Light and dark
The app ships its own stylesheet for both themes, so it does not depend on Streamlit's base theme or the
viewer's browser setting. Use the **Dark mode** toggle at the top of the sidebar; every chart repaints with it.

## Data modes
- **Live market data:** annual statements, market caps and prices from Yahoo Finance (via `yfinance`),
  converted to ₹ crore. Yahoo limits how often one server can ask, so if you see a rate-limit
  message, wait a few minutes or switch to demo data.
- **Demo data (offline):** a synthetic generator creates realistic statements for any chosen peers,
  using industry-specific assumptions. Optional planted errors show the data-quality checks at work.
  Demo numbers are not the real financials of these companies.

The Nifty 500 list loads from NSE, then a GitHub mirror, then `data/nifty500.csv` (bundled snapshot).

## Macro sensitivity
Demo mode generates ten years of statements (FY2016 to FY2025) driven by a simulated macro environment:
real GDP growth, CPI inflation, a policy repo rate that follows a Taylor-style rule, and INR per USD. Each
industry has a built-in GDP beta (metals 2.0, cement 1.6, FMCG 0.35, healthcare 0.3). The **Macro sensitivity**
tab estimates every company's beta with OLS (statsmodels), classifies it from defensive to highly cyclical,
correlates year-on-year changes (not trending levels, which correlate spuriously), shows 3-year moving averages,
runs a next-year GDP scenario, and checks the estimate against the built-in beta. Live mode has only about four
years of statements, too few for a reliable slope, so the tab explains this instead of showing a weak estimate.

## Project structure
| File | What it does |
|---|---|
| `app.py` | The Streamlit interface: industry, peers, analysis, export |
| `peerlens/universe.py` | Loads the Nifty 500 constituent list |
| `peerlens/live.py` | Fetches and standardises Yahoo Finance statements |
| `peerlens/synthetic.py` | Synthetic data generator (industry archetypes, macro-driven growth, planted errors) |
| `peerlens/macro.py` | Simulated macro path and the GDP / inflation sensitivity analysis |
| `peerlens/validator.py` | Data-quality checks and safe fixes |
| `peerlens/ratios.py` | Ratio definitions, ratings, scores, recommendations |
| `peerlens/pipeline.py` | Runs validation → ratios → scores → recommendations |
| `peerlens/charts.py` | All Plotly charts |
| `peerlens/excel_export.py` | Live Excel workbook with formulas, dropdowns and charts |
| `tests/test_core.py` | Edge-case tests (`python -m pytest -q`) |

## Trading desk (second page)
`pages/1_Trading_desk.py` adds a live order book and three automated strategies on a synthetic market
for any Nifty 500 company.

- **Matching engine** (`peerlens/market.py`): a price-time priority limit order book with limit and
  market orders, cancellations, and a depth ladder — the same mechanics as an exchange book.
- **Agents:** a market maker quoting a five-level ladder and skewing against its own inventory,
  uninformed noise flow, a moving-average momentum bot, and a **fundamental bot whose fair value comes
  from the composite health score** produced by the peer analysis. Sound company trading cheap, it
  buys; weak company trading rich, it sells.
- **Deterministic replay:** the session is generated from the seed and the date, replayed from the
  09:15 open to the current tick, so the market looks continuously live during market hours without any
  background process, every viewer sees the same book, and any state can be reproduced exactly.
- The page refreshes every 10 seconds while "Live ticking" is on.

Streamlit lists the main app in the sidebar under its file name (`app`). Rename `app.py` if you want a
different label; Streamlit Cloud's "Main file path" must match whatever you choose.
