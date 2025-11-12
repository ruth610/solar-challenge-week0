# Cross-country solar comparison

## Notebooks
- `compare_countries.ipynb` — loads cleaned CSVs from `data/`, produces summary table and boxplots, runs ANOVA/Kruskal–Wallis on GHI.

## Streamlit app
- Branch: `dashboard-dev`
- Run: `streamlit run app/main.py`
- Notes: keep `data/` directory locally and in `.gitignore`.

## Outputs
- `outputs/summary_table.csv`
- `outputs/boxplot_GHI.png`, `outputs/boxplot_DNI.png`, `outputs/boxplot_DHI.png`
- `outputs/ghi_ranking.png`
- `outputs/stats_summary.txt`
