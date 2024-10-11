
## Folder structure

```md
├── data
│   ├── raw                 # Unprocessed data, as obtained.
        ├── csAI                 # Unprocessed data, as obtained in https://zenodo.org/records/10975879
            ├──                # XX Entries
        ├── csCSE                 # Unprocessed data, as obtained in https://zenodo.org/records/10988947
            ├── bidir.json       # 1400 Entries    
            |── 00-build-bidir.py  # filter repos and output 00_non_github_repositories.csv at processed folder
│   ├── processed           # Cleaned and processed data ready for analysis.
```

`00-build-bidir.py` script is the `00` step, that remove duplicated and non-github repos found in `bidir_dataset.csv`.
Stats for `bidir_dataset.csv`
- Number of unique repositories: 1441 (results in `processed` folder at `00_bidir_dataset_unique.csv` file)
- Number of duplicate repositories: 44
- Number of rows in the CSV data: 1485

