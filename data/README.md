
## Folder structure

```md
├── golden
    ├── repo_manual_annotations.csv # 100 entities curated for installation methods
├── data
│   ├── raw                 # Unprocessed data, as obtained.
        ├── csAI                 # Unprocessed data, as obtained in https://zenodo.org/records/10975879
            ├──                # XX Entries
        ├── csCSE                 # Unprocessed data, as obtained in https://zenodo.org/records/10988947
            ├── bidir.json       # 1400 Entries    
            |── 00-stats_bidir_dataset.py  # filter repos and output 00_non_github_repositories.csv at processed folder
│   ├── processed           # Cleaned and processed data ready for analysis.
```

