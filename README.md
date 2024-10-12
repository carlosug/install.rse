# install.rse
Repository that holds the code used for the paper *"detecting installation instructions"* at IEEE MSR 2025

**tl;dr**:

Implementation of research software involves numerous challenges; a rigorous standardized approach is needed to examine software tools prior to their publication.



- [Explanation for Annotation Procedures for Gold Standard Corpus](./data/golden/README.md)


## Folder structure

* `data` folder: 
  - `golden`: `repo_manual_annotations.csv` --> corpus of 100 repos selected with various annotations
  - `processed`:`00_bidir_dataset_unique.csv`: input for SOMEF extractor
* `extractor` folder: invoke SOMEF to extract readme metadata on `00_bidir_dataset_unique.csv`
 - `01-extracted_metadata` folder: the folder created by SOMEF automatically. Its now *empty* but it should contains the json files *(SOMEF got token limitation so I split the process)*
 - `02.1-extractor_install_combined.py` is the script to output the JSON file with installation_instruction readmes `02_combined_installation_readmes.json`.

## Analysis
The analysis for *RQs* described in our paper should be replicated with `.py` files and jupyter notebook `.ipynb` in [results](./results/) with [visuals](./visualisations/)

## Classifier
The models should be saved in [classifier](./classifier/)

## Citation

If you use our provided data or results, please cite our paper:

```
@article{carlosug,
  title={},
  author={Carlos Utrilla Guerrero, Oscar Corcho and Daniel Garijo},
  journal={arXiv preprint arXiv:XXX.XXX},
  year={2024}
}
```