#!/usr/bin/env python3
"""
Zero-dependency Python 3 client for the PostalCodes.info Free Tier REST API
and Haversine distance/radius calculations.

Documentation & Free API Key: https://postalcodes.info/docs
Dataset Catalog & Free CSV Samples: https://postalcodes.info/datasets
Interactive Radius Tool: https://postalcodes.info/postal-code-radius-calculator
"""
import json
import math
import urllib.parse
import urllib.request

BASE_URL = "https://postalcodes.info/api/v1"


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute great-circle distance in kilometers between two WGS84 coordinates."""
    r = 6371.0088
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    return 2.0 * r * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))


def lookup_postal_code(country_iso2: str, code: str, api_key: str = "free") -> dict:
    """Query a postal code via the PostalCodes.info REST API."""
    params = urllib.parse.urlencode({"country": country_iso2.upper(), "code": code, "key": api_key})
    req = urllib.request.Request(
        f"{BASE_URL}/lookup?{params}",
        headers={"User-Agent": "PostalCodes-OpenData-Client/1.0 (+https://postalcodes.info/docs)"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    # Example: Calculate distance between Madrid (28001) and Barcelona (08001)
    dist = haversine_km(40.4238, -3.6844, 41.3851, 2.1734)
    print(f"Madrid (28001) <-> Barcelona (08001): {dist:.2f} km")
    print("Explore more at https://postalcodes.info/docs and https://postalcodes.info/datasets")
