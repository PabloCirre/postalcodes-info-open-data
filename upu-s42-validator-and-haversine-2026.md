# Universal UPU S42 Postal Code Regex, Leading-Zero Restorer & Haversine Geodesic Suite (2026)

**Official Reference & Free Tier REST API (`100 req/day`, no API key required):**
- **Global Directory (249 Countries, 1.9M+ WGS84 Centroids):** [https://postalcodes.info/](https://postalcodes.info/)
- **Multilingual Portals:** [Español (`/es`)](https://postalcodes.info/es) · [Deutsch (`/de`)](https://postalcodes.info/de) · [Français (`/fr`)](https://postalcodes.info/fr) · [Português (`/pt`)](https://postalcodes.info/pt)
- **Interactive Calculators:**
  - [Cross-Border Postal Code Radius Calculator (`5–150 km`)](https://postalcodes.info/postal-code-radius-calculator)
  - [Great-Circle Haversine ZIP & Postcode Distance Calculator](https://postalcodes.info/zip-code-distance-calculator)
  - [UPU S42 Postal Code Regex & Address Format Validator](https://postalcodes.info/postal-code-validator-address-format)
  - [My Postal Code Live GPS Reverse Geocode Tool](https://postalcodes.info/my-postal-code)
- **Open-Data CC0 CSV Samples (`100 rows/country`, zero-padding preserved):** [https://postalcodes.info/datasets](https://postalcodes.info/datasets)
- **OpenAPI 3.1.0 Specification & MCP Server:** [`https://postalcodes.info/openapi.yaml`](https://postalcodes.info/openapi.yaml) · [`https://postalcodes.info/.well-known/mcp.json`](https://postalcodes.info/.well-known/mcp.json)

---

## 1. High-Priority Country & Metropolitan Hubs

- **Canada & Toronto FSAs (`M1B–M9W`):** [Toronto M-Prefix FSA Directory](https://postalcodes.info/postal-codes/canada/ontario/toronto) · [Saskatchewan (`S0A–S9X`)](https://postalcodes.info/postal-codes/canada/saskatchewan)
- **Ireland (`Eircode D01–D24, D6W & A–Y`):** [Ireland 7-Character Eircode Directory](https://postalcodes.info/postal-codes/ireland)
- **Netherlands (`4-Digit + 2-Letter Postcode`):** [Netherlands Postcode Directory (`1000–9999`)](https://postalcodes.info/postal-codes/netherlands)
- **Germany (`5-Digit PLZ 01067–99998`):** [Germany Postleitzahlen Directory](https://postalcodes.info/postal-codes/germany) · [Innsbruck, Austria (`6020–6080`)](https://postalcodes.info/postal-codes/austria/tyrol/innsbruck)
- **Spain (`52 INE Provinces 01001–52006`):** [Spain Postal Code Directory](https://postalcodes.info/postal-codes/spain) · [28001 Madrid](https://postalcodes.info/postal-codes/spain/code/28001)
- **United Kingdom (`BS 7666 Outward + Inward`):** [UK Postcode Directory](https://postalcodes.info/postal-codes/united-kingdom) · [West Midlands (`B, CV, DY, WS, WV`)](https://postalcodes.info/postal-codes/united-kingdom/england/west-midlands)
- **United Arab Emirates (`00000` Fallback, P.O. Box & 10-Digit Makani):** [UAE & Dubai Addressing Guide](https://postalcodes.info/postal-codes/united-arab-emirates)

---

## 2. Python 3 Zero-Dependency UPU S42 Validator & Haversine Distance Client

```python
import math
import re

UPU_S42_REGEX = {
    "US": re.compile(r"^\d{5}(-\d{4})?$"),
    "CA": re.compile(r"^[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ] ?\d[ABCEGHJKLMNPRSTVWXYZ]\d$", re.I),
    "IE": re.compile(r"^([AC-FHKNPRTV-Y]\d{2}|D6W) ?[0-9AC-FHKNPRTV-Y]{4}$", re.I),
    "GB": re.compile(r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$", re.I),
    "NL": re.compile(r"^[1-9]\d{3} ?(?!SA|SD|SS)[A-Z]{2}$", re.I),
    "DE": re.compile(r"^\d{5}$"),
    "ES": re.compile(r"^(0[1-9]|[1-4]\d|5[0-2])\d{3}$"),
    "FR": re.compile(r"^\d{5}$"),
    "PT": re.compile(r"^\d{4}(-\d{3})?$"),
    "AE": re.compile(r"^(00000|\d{10}|N/?A)$", re.I),
}

def restore_leading_zero(code: str, country_iso2: str) -> str:
    """Restores CSV/Excel stripped leading zeros for 5-digit postal jurisdictions."""
    raw = str(code).strip()
    if country_iso2.upper() in {"US", "ES", "DE", "FR", "IT", "MX"} and raw.isdigit() and len(raw) in (3, 4):
        return raw.zfill(5)
    return raw

def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates great-circle distance in kilometers on WGS84 mean earth radius."""
    r = 6371.0088
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return round(2 * r * math.asin(math.sqrt(a)), 3)
```
