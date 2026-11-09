# PostalCodes.info — Open Data Samples, Free Tier REST API & Geospatial Tools (249 Countries)

[![Zenodo Dataset DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19493709-blue)](https://zenodo.org/records/19493709)
[![OpenAPI 3.1.0](https://img.shields.io/badge/OpenAPI-3.1.0-6ba539)](https://postalcodes.info/openapi.yaml)
[![License: CC0-1.0](https://img.shields.io/badge/Data%20License-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**[PostalCodes.info](https://postalcodes.info/)** maintains an open-access global postal code and administrative hierarchy directory covering **249 ISO-3166 countries and territories**, alongside a **Free Tier JSON REST API**, downloadable **CC0 CSV Country Samples**, and interactive **Haversine geospatial calculators**.

---

## 1. Free Tier REST API & Developer Documentation (`No Credit Card Required`)

Developers, data engineers, and researchers can integrate postal code validation, locality resolution, and coordinate lookup at zero cost using the public Free Tier (**100 requests/day**, JSON over HTTPS, CORS enabled):

- **Interactive Developer Portal & Free API Key Generator:** [https://postalcodes.info/docs](https://postalcodes.info/docs)
- **OpenAPI 3.1.0 Machine-Readable Specification:** [https://postalcodes.info/openapi.yaml](https://postalcodes.info/openapi.yaml)
- **APIs.json Discovery Manifest:** [https://raw.githubusercontent.com/PabloCirre/postalcodes-info-open-data/main/apis.json](https://raw.githubusercontent.com/PabloCirre/postalcodes-info-open-data/main/apis.json)
- **Canonical Web Platform:** [https://postalcodes.info/](https://postalcodes.info/)

### Quickstart API Examples (`curl` & Python)

```bash
# 1. Lookup postal code metadata, administrative hierarchy, and WGS84 centroid
curl -s "https://postalcodes.info/api/v1/lookup?country=ES&code=28001" | jq .

# 2. Cross-border Haversine radius search (e.g., 25 km around 28001 Madrid)
curl -s "https://postalcodes.info/api/v1/radius?country=ES&code=28001&radius_km=25" | jq .
```

See [`examples/postal_radius_client.py`](./examples/postal_radius_client.py) in this repository for a zero-dependency Python 3 client with local Haversine fallback and CSV export.

---

## 2. Free Country CSV Samples (CC0 Public Domain)

Every country in the **[Global Postal Code Datasets Catalog](https://postalcodes.info/datasets)** provides an instant **Free 50-Row CSV Sample** (`UTF-8`, normalized schema: `country_iso2, postal_code, place_name, admin1_name, admin2_name, latitude, longitude`) so engineering teams can test ETL pipelines and database schemas before production deployment:

- **Global Dataset Catalog & Schema Reference:** [https://postalcodes.info/datasets](https://postalcodes.info/datasets)
- **Direct Free CSV Sample Downloads:**
  - [Spain (`ES`) Free CSV Sample](https://postalcodes.info/datasets?sample=ES)
  - [United States (`US`) Free CSV Sample](https://postalcodes.info/datasets?sample=US)
  - [Germany (`DE`) Free CSV Sample](https://postalcodes.info/datasets?sample=DE)
  - [Netherlands (`NL`) Free CSV Sample](https://postalcodes.info/datasets?sample=NL)
  - [United Kingdom (`GB`) Free CSV Sample](https://postalcodes.info/datasets?sample=GB)
  - [Canada (`CA`) Free CSV Sample](https://postalcodes.info/datasets?sample=CA)
  - [France (`FR`) Free CSV Sample](https://postalcodes.info/datasets?sample=FR)

---

## 3. Free Interactive Geospatial & Logistics Calculators

All web calculators on **[PostalCodes.info Tools Hub](https://postalcodes.info/tools)** are 100% free to use and support instant **CSV / JSON result export**:

1. **[Cross-Border Postal Code Radius Calculator](https://postalcodes.info/postal-code-radius-calculator)** — Find all postal codes and localities within a custom kilometer/mile radius (`5 km` to `150 km`), including across international borders (e.g., Benelux, DACH, US–Canada, Spain–Portugal).
2. **[ZIP & Postal Code Distance Calculator](https://postalcodes.info/zip-code-distance-calculator)** — Compute exact great-circle Haversine distance (`km` and `miles`) between any two postal codes worldwide.
3. **[International Postal Code & Address Format Validator](https://postalcodes.info/postal-code-validator-address-format)** — Test postal code regex patterns, check digits, and UPU S42 address templates across 249 countries.
4. **[My Postal Code — GPS Reverse Geolocation Lookup](https://postalcodes.info/my-postal-code)** — Resolve browser GPS coordinates (`latitude, longitude`) to the nearest verified postal code and administrative district.

---

## 4. High-Demand Country & City Reference Hubs

Direct links to the most frequently queried national and metropolitan postal directories:

| Country / Territory | Reference Hub URL | Format / System |
| :--- | :--- | :--- |
| **United States** | [https://postalcodes.info/postal-codes/united-states](https://postalcodes.info/postal-codes/united-states) | 5-digit ZIP / ZIP+4 (`USPS`) |
| **Netherlands** | [https://postalcodes.info/postal-codes/netherlands](https://postalcodes.info/postal-codes/netherlands) | 4 digits + 2 letters (`1011 AA` PostNL) |
| **Germany** | [https://postalcodes.info/postal-codes/germany](https://postalcodes.info/postal-codes/germany) | 5-digit *Postleitzahl* (`PLZ`) |
| **United Kingdom** | [https://postalcodes.info/postal-codes/united-kingdom](https://postalcodes.info/postal-codes/united-kingdom) | Alphanumeric Outward + Inward (`Royal Mail`) |
| **Canada (Toronto FSA)** | [https://postalcodes.info/postal-codes/canada/ontario/toronto](https://postalcodes.info/postal-codes/canada/ontario/toronto) | Forward Sortation Area (`M4B`–`M9W`) |
| **Spain (Madrid 28001)** | [https://postalcodes.info/postal-codes/spain/code/28001](https://postalcodes.info/postal-codes/spain/code/28001) | 5-digit INE / Correos (`28001`) |

### Multilingual Documentation & Regional Portals

- **English (Global):** [https://postalcodes.info/](https://postalcodes.info/)
- **Español:** [https://postalcodes.info/es](https://postalcodes.info/es) · [Calculadora de Radio de Códigos Postales](https://postalcodes.info/es/postal-code-radius-calculator)
- **Deutsch:** [https://postalcodes.info/de](https://postalcodes.info/de) · [PLZ-Umkreissuche](https://postalcodes.info/de/postal-code-radius-calculator)
- **Français:** [https://postalcodes.info/fr](https://postalcodes.info/fr) · [Calculateur de Rayon Code Postal](https://postalcodes.info/fr/postal-code-radius-calculator)
- **Português:** [https://postalcodes.info/pt](https://postalcodes.info/pt) · [Calculadora de Raio de Código Postal](https://postalcodes.info/pt/postal-code-radius-calculator)

---

## 5. Academic & Technical Citations (Zenodo DOIs)

When referencing **PostalCodes.info** in academic papers, GIS benchmarks, or open-data catalogs, please cite the archived Zenodo records:

- **Global Dataset Reference DOI:** [https://zenodo.org/records/19493709](https://zenodo.org/records/19493709) (`10.5281/zenodo.19493709`)
- **Methodology & Normalization Note:** [https://zenodo.org/records/19930578](https://zenodo.org/records/19930578) (`10.5281/zenodo.19930578`)
- **Coverage & Quality Benchmark:** [https://zenodo.org/records/19930688](https://zenodo.org/records/19930688) (`10.5281/zenodo.19930688`)


---

## 📊 2026 Geodata Benchmarks, Regional GIS Guides & AI RAG (`/llms.txt` v3.0)

- **[2026 Global & European Postal Code Database Benchmark (PostalCodes.info vs GeoNames vs Eurostat GISCO)](https://pablocirre.github.io/postalcodes-info-open-data/benchmarks/2026-global-postal-code-database-comparison.html)** — Independent coverage, WGS84 centroid precision, and leading-zero protection audit across 249 ISO countries ([Canonical Dataset Catalog](https://postalcodes.info/datasets)).
- **[Ecuador & Guayaquil 6-Digit Postal Code Directory (`090101–090505` Agencia Nacional Postal)](https://pablocirre.github.io/postalcodes-info-open-data/guides/ecuador-guayaquil-and-latin-america-postal-codes.html)** — Parish-level lookup for Guayaquil (`090150` General, `090505` Tarqui/La Alborada/Urdesa/Kennedy, `090313` Centro) and Quito (`170102–170150`) ([Ecuador Hub](https://postalcodes.info/postal-codes/ecuador)).
- **[European Postal Code Architecture: Netherlands PostNL (`1012 JS`), Sweden `Postnummer` (`Län`), Germany `PLZ` & Ireland `Eircode`](https://pablocirre.github.io/postalcodes-info-open-data/guides/europe-postnl-postnummer-and-deutsche-post-plz-architecture.html)** — Comparative engineering matrix with 2x Retina cartography ([Netherlands](https://postalcodes.info/postal-codes/netherlands) · [Sweden](https://postalcodes.info/postal-codes/sweden) · [Berlin](https://postalcodes.info/postal-codes/germany/berlin) · [Ireland](https://postalcodes.info/postal-codes/ireland)).
- **[PostalCodes.info `/llms.txt` v3.0 AI Grounding Specification](https://postalcodes.info/llms.txt)** & **[Model Context Protocol Manifest (`/.well-known/mcp.json`)](https://postalcodes.info/.well-known/mcp.json)**.
