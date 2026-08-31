# Financial Inclusion Gap Map & Branch Expansion Site Selection
## Democratic Republic of Congo

A geospatial analysis identifying underserved populations relative to formal financial access points in DR Congo, and recommending specific new branch/agent locations using a facility-location optimization algorithm — not just a map, an actual decision-support tool.

**Headline finding:** 76.5% of DR Congo's population (~68.5 million people) live more than 10km from the nearest bank, ATM, or financial office. This gap is highly uneven: Kinshasa is only 5.7% underserved, while 5 provinces are 100% underserved.

**[View the interactive map](https://jbx-p.github.io/financial-inclusion-gap-map/maps/financial_inclusion_gap_map.html)**

## Why This Project

Most portfolio geospatial projects stop at "here's a map." This one produces a ranked, defensible list of 10 specific candidate branch locations — the kind of decision-support output a real microfinance institution's commercial/marketing team could act on directly. It's built entirely on free, open, real data — no synthetic or simulated inputs.

## Data Sources

- **Population:** WorldPop DRC gridded population estimates, 2020, UN-adjusted (~100m resolution) — CC BY 4.0, via data.humdata.org
- **Financial access points:** OpenStreetMap contributors, via the Humanitarian OpenStreetMap Team's pre-built DRC financial services export (data.humdata.org) — used in place of a live Overpass API query, since OpenStreetMap's live API infrastructure is blocked in mainland China without a VPN
- **Administrative boundaries:** geoBoundaries, ADM1 (province) level

## Methodology

1. Downsampled the population raster (~100m to ~1km) for tractability, validating the total against DRC's known population (~90-110M).
2. Computed nearest-neighbor distance from every populated grid cell to the closest financial access point, in a metric (Africa Albers Equal Area) projection.
3. Validated results against known geography (Kinshasa shows sub-2km distances; population-weighted vs. raw-cell-count distances confirmed people cluster nearer access points than average land area, as expected).
4. Defined "underserved" as >10km from the nearest access point (a documented modeling assumption).
5. Applied a greedy facility-location algorithm to recommend 10 new branch sites, each selected to maximize NEWLY covered underserved population (previously-covered population is removed before each subsequent selection, so sites represent genuinely additional coverage).
6. Built an interactive map (population heatmap, existing access points, recommended new sites) and static supporting charts.

## Key Limitation (stated plainly, not buried)

OpenStreetMap shows only 8 mapped mobile money agents nationwide against 313 banks. Mobile money is widely understood to be a primary financial access channel in DRC day-to-day, and its near-absence from this data source means this analysis likely OVERSTATES the true financial access gap — it can only see formal/bank-centric infrastructure. See the full memo for this and other limitations (travel distance vs. straight-line distance, modeled vs. census population data).

## Repo Structure

```
financial-inclusion-gap-map/
├── data/
│   ├── raw/              # source files (not committed - see Setup)
│   └── processed/        # financial_access_points.geojson, drc_provinces.geojson,
│                         # province_summary.csv, candidate_branch_locations.csv
│                         # (large population grid files regenerated locally, not committed)
├── notebooks/
│   ├── 01_data_acquisition.ipynb       # financial points + province boundaries
│   ├── 02_population_processing.ipynb  # raster processing, downsampling
│   └── 03_distance_analysis.ipynb      # distance calc, underserved score, facility location, map, charts
├── maps/                  # interactive HTML map
├── outputs/               # business memo, static charts
├── README.md
└── requirements.txt
```

## Reproducing This

1. Download WorldPop's DRC population data (`cod_ppp_2020_UNadj.tif`) from [data.humdata.org](https://data.humdata.org/dataset/worldpop-population-counts-for-democratic-republic-of-the-congo) into `data/raw/drc_population.tif`
2. Download the financial services export from [data.humdata.org](https://data.humdata.org/dataset/hotosm_cod_financial_services) into `data/raw/financial_services/`
3. Download DRC ADM1 boundaries from [geoboundaries.org](https://www.geoboundaries.org/countryDownloads.html) into `data/raw/boundaries/`
4. `python -m venv venv`, activate it, `pip install -r requirements.txt`
5. Run notebooks in order: `01_data_acquisition.ipynb` → `02_population_processing.ipynb` → `03_distance_analysis.ipynb`

Note: the large intermediate population grid files (500MB-900MB) are regenerated locally by the notebooks and are not committed to this repo.

## Business Memo

See [`outputs/business_memo.md`](outputs/business_memo.md) for the full write-up: methodology, candidate site recommendations, province priorities, and limitations.

## Author

Joel Bumba - [github.com/jbx-p](https://github.com/jbx-p) - [jbx-p.github.io](https://jbx-p.github.io)
