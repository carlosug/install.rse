## Good practices in Research Software Development and Documentation

List of articles, papers and notes about research software documentation. We seek to answer:

**- RQ1: What are the recommendations for documenting installation methods of research software?**

        * Which rules and best practices exist? Do the given recommendations cover the defined categories?;

**- RQ2: What is the practice of documenting research software?**

<!-- ### Education
- [eScience Center](https://esciencecenter-digital-skills.github.io/2024-10-22-ds-cr/)
- [Code Refinery](https://coderefinery.org/lessons/) -->


### High level guidelines
- [Introducing FAIR principles for research software](https://www.nature.com/articles/s41597-022-01710-x):
    * I1, I2
    * R3: Software meets domain-relevant community standards.

- [Towards FAIR principles for research software](https://content.iospress.com/articles/data-science/ds190026)
    * 4.2. Accessibility
    * R1.3. Metadata meet domain-relevant community standards: *The software’s documentation should provide information on how to install, run and use a software*

- [FIVE Recommendations for FAIR Software](https://fair-software.eu/)

- Software Engineering practices in academic researchers:
    * Neuroinformatics: [Re-run, Repeat, Reproduce, Reuse, Replicate](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2017.00069/full)
    * [Promoting the 3Rs—Readability, Resilience, and Reuse](https://hdsr.mitpress.mit.edu/pub/f0f7h5cu/release/2)


- Making Biomedical Research Software FAIR: Step by step guidelines
    * [https://www.nature.com/articles/s41597-023-02463-x](https://www.nature.com/articles/s41597-023-02463-x)


**TODO:**
- [https://www.bestpractices.dev/en](https://www.bestpractices.dev/en)
- [https://zenodo.org/records/10723608](https://zenodo.org/records/10723608) - check installability

### Domain specific communities developing research software descriptors:
- **Research Sofware community:**
    1. [CodeMeta Project](https://codemeta.github.io/index.html):
        - `buildInstructions` property
    2. [FAIR4RS WG RDA](https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg/)
- **Software Engineering community:**

- **Bioninformatics - Life Science community:**
    1. Bioschemas
    2. [FAIRSoft ELIXIR](https://academic.oup.com/bioinformatics/article/40/8/btae464/7717992):
        - Openbench (Quantitative monitoring of the technical quality of software in Life Sciences): [https://openebench.bsc.es/](https://openebench.bsc.es/)
    3. Computational biology: [Ten simple rules for making research software more robust](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412):
        - Rule 2 - > provide compilation or installation instructions
        - Rule 6 - > Rely on build tools and package managers for installation
    4. [PHA4GE Proposed Standards for Public Health Bioinformatics Software](https://pha4ge.org/resource/proposed-standards-for-public-health-bioinformatics-software/):
        - *Providing clear local installation and/or remote access instructions for public health bioinformatics*
        - *Installation instructions should include a step-by-step list*

- **Documenting research software in engineering science:**
    1. Examined existing recommendations: [https://www.nature.com/articles/s41598-022-10376-9](https://www.nature.com/articles/s41598-022-10376-9)

- Sharing practices of software artefacts and source code for reproducible research: https://link.springer.com/article/10.1007/s41060-024-00617-7

### Suggestions for a good README
- [Github Guidelines](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Makeareadme 101](https://www.makeareadme.com/)
- [Template for a standard style](https://github.com/RichardLitt/standard-readme)
- [4TUResearchData](https://data.4tu.nl/s/documents/Guidelines_for_creating_a_README_file.pdf)
- [Template for FAIR readme](https://github.com/manuGil/fair-code?tab=readme-ov-file)
- [How-to guidelines of Divio Cloud](https://docs.divio.com/documentation-system/how-to-guides/)
- [Makeareadme.com](https://www.makeareadme.com/#installation-1)
- [Installation and Usage](https://awegroup.github.io/developer-guide/docs/documentation.html#installation-and-usage)
- [GovUSA](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md#instructions-for-how-to-develop-use-and-test-the-code)


### Coding standards and conventions on README
- [GNU Coding starndards](https://www.gnu.org/prep/standards/standards.html) - Install command categories [https://www.gnu.org/prep/standards/standards.html#Install-Command-Categories](https://www.gnu.org/prep/standards/standards.html#Install-Command-Categories)
- [PEP-8 Python]()
...

### Articles focused in installation methods and instructions:
- [Taxonomy of Installation Instruction Changes]()
- [Open Source Software Development Tool Installation-Challenges and Strategies For Novice Developers]()



### Installation method mentioned in the recommendations

**Table: Summary of previous articles about research software and relevant installation methods/types**

|Article   | Year  | Field   |  Scope  | Installation methods  | Summary of findings|
|---|---|---|---|---|---|
| [Stodden and Miguez](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.ay)  | 2014   |   |   |   | |
| [Fehr and Heiland](http://www.aimspress.com/article/10.3934/Math.2016.3.261)  | 2016   |   |   |   ||
| [Wilson et al](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)  | 2014   |   |   |   ||
| [Wilson et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)  | 2017  |   |   |   ||
| [Hastings et al](https://academic.oup.com/gigascience/article/3/1/2047-217X-3-31/2682967)  | 2014  |   |   |   ||
| [Sandve et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)  | 2013  |   |   |   ||
| [Lee et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006561)  | 2013  |   |   |   ||
| [Gil et al](https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015EA000136)  | 2016  |   |   |   ||
| [Morgan et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412)  | 2016  |   |   |   ||
| [Karimzadeh et al](https://academic.oup.com/bib/article/19/4/693/2907814?login=false)  | 2018  |   |   |   ||
| [Barker et al](https://www.nature.com/articles/s41597-022-01710-x)  | 2022  |   |   |   ||
| [Lamprecht et al](https://content.iospress.com/articles/data-science/ds190026)  | 2022  |   |   |   ||
| [Fabien et al](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2017.00069/full)  | 2018  |   |   |   ||
| [Connolly et al](https://hdsr.mitpress.mit.edu/pub/f0f7h5cu/release/2)  | 2023  | Software Engineering   | Accessibility of the tools might differ from project scope e.g., solo or community-based software   |   |Engineering practices that promote 3R software in academia|
| [Patel et al](https://www.nature.com/articles/s41597-023-02463-x)  | 2023  |   |   |   ||
| [Jean-Quartier et al](https://link.springer.com/article/10.1007/s41060-024-00617-7)  | 2023  |   |   |   ||
| [Russell et al](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0205898)  | 2018  | bioinformatic  | software and tools  |  - |Usability refers to ease and transparency of installation and usage.|
| [Gao et al](http://arxiv.org/abs/2312.03250))  | 2024  | software engineer  | updates in readmes about installation  |  Source Code Operations, installation alternatives such as Docker, Published Package Operations |installation-related instructions updates and taxonomy of installation major categories of changes in READMEs.|
| [Aghajani et al.,](https://doi.org/10.1145/3377811.3380405)  | 2019  | software engineer  | issues on documentation in general  |   |installation-related instructions updates and taxonomy of installation major categories of changes in READMEs.|
| [Aghajani et al.,](https://doi.org/10.1145/3377811.3380405)  | 2018  | software engineer  | documentation issues taxonomy: about correctness and completeness in docs  |   |inappropriate installation instructions.|
| [Treude et al.,](https://arxiv.org/abs/2007.10744)  | 2020  | software engineer  | Accuracy of software documentation  |   |inappropriate installation instructions.|
| [Treude et al.,](https://arxiv.org/abs/2007.10744)  | 2020  | software engineer  | large-scale empirical study of code-comment inconsistencies, identifying the taxonomy of inconsistencies fixed by developers  |   |inappropriate installation instructions.|
| [Mangul et al.,](https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3000333&type=printable)  | 2019  | computational biology  | instabillity test  |   |Tools available in well-maintained package managers such as Bioconda were always installable, whereas tools not shipped via package managers were prone to problems|
| [Jimenez et al.,](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5490478/)  | 2017  | ELIXIR |Four simple recommendations to encourage best practices in research software   | Provides easy access for software packagers to deploy your software, thus increasing visibility  |guidelines, best practices, recommendations|
| [Andreas Prlić et al.,](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002802)  | 2012  | general domain |Ten Simple Rules for the Open Development of Scientific Software  |   |Rule 5: Be simple, employ standard package - open-source packaging communities|
| [Gewaltig et al.,](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003376)  | 2014  | computational neuroscience|Ten Simple Rules for the Open Development of Scientific Software  | "easy to install" for "research-ready" software type, but not specified the tpye of installation|   ||
| [Yuyang et al.,](https://linkinghub.elsevier.com/retrieve/pii/S0950584922000775)  | 2022  | computer science|readme files, softwre popularity, clustering  | "easy to install" for "research-ready" software type, but not specified the tpye of installation|  "softwares with installation instructions on readme gets more stars", "Setup, Install, or Installation as a sectionheading used to provide information about installing a repository." ||

### Empirical Studies on Software Documentation: Literature Review

Brief Scoping Literature Review - Paper to include - Criteria:

- On conferences MSR, FSE and ICSE
- Terms “README” and/or “installation instructions”
- Information databases:
       + ACM Digital Library (DONE)
       + IEEE Xplore (TODO)
       + Google scholar (TODO)

#### 1. ACM - MSR: 
[Link Query](https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&ConceptID=120045&expand=all&AllField=Abstract%3A%28best+practices%29+AND+Abstract%3A%28readme%29+AND+Abstract%3A%28research+software%29+AND+Abstract%3A%28installation%29+OR+Abstract%3A%28installation+method*%29+OR+Abstract%3A%28installability%29&startPage=&ContentItemType=research-article)

* MSR (results:7)

```sql
"query": {Abstract:(best practices) OR Abstract:(installation) OR Abstract:(documentation) OR Abstract:(readme) OR Abstract:(research software) OR Abstract:(installability)} "filter": {Conference Collections: MSR: Mining Software Repositories}
```

#### 2. ACM - FSE 
[Link Query](https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&ConceptID=119584&ContentItemType=research-article&expand=dl&AllField=Abstract%3A%28best+practices%29+AND+Abstract%3A%28readme%29+AND+Abstract%3A%28research+software%29+AND+Abstract%3A%28installation%29+OR+Abstract%3A%28installation+method*%29+OR+Abstract%3A%28installability%29)

* FSE (results:25) 

```sql
"query": {Abstract:(best practices) AND Abstract:(readme) AND Abstract:(research software) AND Abstract:(installation) OR Abstract:(installation method*) OR Abstract:(installability)} "filter": {Conference Collections: FSE: Foundations of Software Engineering},{Article Type: Research Article},{ACM Content: DL}
```
#### 3. ACM - ICSE

[Link Query](https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&ConceptID=119230&ContentItemType=research-article&expand=all&AllField=Abstract%3A%28best+practices%29+AND+Abstract%3A%28readme%29+AND+Abstract%3A%28research+software%29+AND+Abstract%3A%28installation%29+OR+Abstract%3A%28installation+method*%29+OR+Abstract%3A%28installability%29)

```sql
"query": {Abstract:(best practices) AND Abstract:(readme) AND Abstract:(research software) AND Abstract:(installation) OR Abstract:(installation method*) OR Abstract:(installability)} "filter": {Conference Collections: ICSE: International Conference on Software Engineering},{Article Type: Research Article}
```

* ICSE (results: 75)


#### Reviewed resources:

| Title                                                              | Conf year | What is about:                                                                                                                                               | Strategy                                                      | Relevant for us in: |
|--------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------|
| [Software ingredients: detection of Third-party Component reuse in JAVA](https://sel.ist.osaka-u.ac.jp/lab-db/betuzuri/archive/1038/1038.pdf) | MSR 2016  | Analysis of reuse activity detection of software reuse define a method to detect multiple third-party components in jar file                                   | query                                                         |                     |
| [An empirical analysis of the docker container ecosystem on Github](https://peerj.com/preprints/2905/)   | MSR 2017  | Analysis of the distribution of the project using Docker by programming lang INSTRUCTIONS/ project size and infrastructure // assess the quality of Dockerfiles by classifying issues // classify changes evolution | query                                                         |                     |
| [Cross-project code reuse in Github](https://sharif.edu/~izadi/papers/msr2017.pdf)                                   | MSR 2017  | Construct a Graph with similar RQ                                                                                                                             | query                                                         |                     |
| [Bidirectional Paper-Repository Tracing in Software Engineering](https://dl.acm.org/doi/pdf/10.1145/3643991.3644876)       | MSR 2024  |                                                                                                                                                              | query                                                         |                     |
| [DRMiner: tool for identifying and analysing Dockerfile](https://dl.acm.org/doi/pdf/10.1145/3643991.3644921)               | MSR 2024  | Mine docker instead of readme                                                                                                                                 | query                                                         |                     |
| [On the executability of R Markdown files](https://dl.acm.org/doi/pdf/10.1145/3643991.3644931)                             | MSR 2024  | Similar to readme md - how executable are the R md                                                                                                            | query                                                         |                     |
| [Quantifying Security Issues in Reusable JS Actions in Github workflows](https://dl.acm.org/doi/pdf/10.1145/3643991.3644899) | MSR 2024  | RQ - to what extent do JS actions rely on NPM packages? What are the characteristics of JS action dependencies? To what extent do JS actions have vulnerabilities with https://codeql.github.com/ | query                                                         |                     |
| [Option Matter: Documenting and Fixing Non-reproducible Builds in conf systems](https://dl.acm.org/doi/pdf/10.1145/3643991.3644913) | MSR 2024  | Which configuration options if any have an impact on the reproducibility of builds? An approach to automatically identify configuration options causing non-reproducibility of builds | query                                                         |                     |
| [Automated Generation of Issue Report Templates](https://dl.acm.org/doi/pdf/10.1145/3643991.3644906)                       | MSR 2024  | Similar concept as ours                                                                                                                                      | query                                                         |                     |
| [Analysing the evolution of ML models in HF](https://dl.acm.org/doi/pdf/10.1145/3643991.3644898)                           | MSR 2024  | Similar RQ - how can we evaluate and categorise the status of ML? K-mean cluster algorithm based on activity patterns resulting in high/low maintenance        | query                                                         |                     |
| [A large-scale empirical study of OS licence usage](https://dl.acm.org/doi/pdf/10.1145/3643991.3644900)                    | MSR 2024  | Nicely done with the statistical analysis                                                                                                                    | query                                                         |                     |
| [How to ML projects use CI?](https://2024.msrconf.org/details/msr-2024-technical-papers/20/How-do-Machine-Learning-Projects-use-Continuous-Integration-Practices-An-Empirical-S)                                          | MSR 2024  | Comparative analysis between ML and non-ML projects                                                                                                           | search engine                                                 |                     |
| [Charactering and understanding software security in ML libraries](https://conf.researchr.org/details/msr-2023/msr-2023-technical-papers/43/Characterizing-and-Understanding-Software-Security-Vulnerabilities-in-Machine-Learnin)     | MSR 2023  | RQs similar to violations of readme instructions                                                                                                             | search engine                                                 |                     |
| [Evaluating Software Documentation quality](https://conf.researchr.org/details/msr-2023/msr-2023-technical-papers/2/Evaluating-Software-Documentation-Quality)                            | MSR 2023  | Empirical study to determine what is important in documenting software libraries - selecting metrics and validation with interviews                           | search engine                                                 |                     |
| [A large-scale study about quality and reproducibility of jupyter notebooks](https://leomurta.github.io/papers/pimentel2019a.pdf) | MSR 2019  |                                                                                                                                                              | search engine                                                 |                     |
| [Predicting good configuration for Github Topic models](https://2019.msrconf.org/details/msr-2019-papers/4/Predicting-Good-Configurations-for-GitHub-and-Stack-Overflow-Topic-Models)                | MSR 2019  | Latent Dirichlet allocation as topic model to explain structure of a corpus by grouping text                                                                   | search engine                                                 | Predicting installation instruction errors (method) |
| [Automatic classification of software artifacts in OS applications](https://veneraarnaoudova.ca/wp-content/uploads/2018/03/2018-MSR-preprint-automatic-classification-software-artifacts.pdf)    | MSR 2018  | Identify which types of software artifacts are produced by a wide variety of open-source projects at different levels of granularity. RQ1: how can software be categorised | search engine                                                 |                     |
| [Large-scale of commit patterns](http://www.cs.toronto.edu/~consens/AnalysisGitHubCoCommit/GitHubCoCommitAnalysisCohenConsensMSR2018.pdf)                                       | MSR 2018  | Analyze the co-commit patterns in the constructed co-authorship networks - check RQ                                                                            | search engine                                                 |                     |
| **[Open Source Software Development Tool Installation](https://arxiv.org/pdf/2404.14637)**                   | 2024      | Investigate the challenges novice developers face in software development when installing software development tools with interviews (Christoph Treude to follow his research) | search engine                                                 |                     |
| **[A taxonomy of installation instruction changes](https://arxiv.org/html/2312.03250v1)**                       | 2023      | First research directly on readme - qualitative analysis                                                                                                       | search engine                                                 | Analysing instructions (a taxonomy for installation related changes in readmes) focusing on patterns of behaviours associated with their installation-related section updates |
| **[Evaluating transfer learning for simplifying READMEs](https://2023.esec-fse.org/details/fse-2023-research-papers/50/Evaluating-Transfer-Learning-for-Simplifying-GitHub-READMEs)**                | FSE 2023  | Transfer learning to simplify readmes - (Text simplification)                                                                                                  | search engine                                                 | Analysing readmes focusing on updates with longer commit histories |
| [How READMe files are structured in open source Java projects](https://www.sciencedirect.com/science/article/pii/S0950584922000775)         | 2022      | Publication in ScienceDirect Information and Technology - applying Statistics and cluster methods                                                              | search engine                                                 | Analysing readmes (methods) |
| [An exploratory study of software artifacts on GH from lens of documentation](https://www.sciencedirect.com/science/article/pii/S0950584924000302?via%3Dihub) | 2024      | Qualitative methods to explore useful info in docs                                                                                                            | search engine                                                 | Analysing documentation but not the methods |
| [Software documentation issues unveiled](https://ieeexplore.ieee.org/abstract/document/8811931?casa_token=-rC8Ramb7XwAAAAA:C2cD3ud4Le4HxSDvhnYWRgyoHs_vLsNe7LnidqYiMnIAP0gRtamLyk-vD-AKlOsk3nz8sp6u1g)                               | 2019 IEEE/ACM | Comprehensive taxonomy consisting of 162 types of documentation issues                                                                                        | search engine                                                 | Analysing documentation issues type (categories) |
| [OS software documentation Mining for quality assessment](https://link.springer.com/chapter/10.1007/978-3-642-36981-0_73#citeas)              | 2013 AIST | Assess the quality of non-source code text found in software packages                                                                                         | search engine                                                 | Analysing the quality the method to be checked |
| [Why do Software Package Conflict?](https://upsilon.cc/~zack/research/publications/msr2012-conflicts.pdf)                                    | MSR 2012  | How to detect conflict in packages similar to how to detect incorrect instructions                                                                            | search engine                                                 | Detecting installation instructions errors (method) |
| Quantifying reproducibility: Quantifying Reproducibility in Computational Biology: The Case of the Tuberculosis Drugome paper |          |                                                                                                                                                              |                                                               |                     |
| [Measuring the reusability of software components using static analysis](https://www.sciencedirect.com/science/article/pii/S0164121219301979?casa_token=JZuReQ9CrHgAAAAA:8zcDnQ_IJY8DqFCjFCcUd_tk0ClYpYmZeHkFheoFCAM_Eg8rp0nzyLtcD7l4BOrrgWrwfm5OjuY) | 2019      | An interpretable methodology for estimating reusability at class and package levels                                                                           | search engine                                                 | Measure reusability |
| [A large-scale study on research code quality and execution](https://www.nature.com/articles/s41597-022-01143-6#Sec3)           | 2022      |                                                                                                                                                              |                                                               |                     |
| [On the accuracy of code complexity metrics](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.1065366/full)                           | 2023      |                                                                                                                                                              | search engine                                                 | Complex measurement |
| [Ease of adoption of clinical natural language processing software](https://www.sciencedirect.com/science/article/pii/S1532046415001483?via%3Dihub)    | 2015      | Assess the ease of adoption of the state-of-the-art clinical NLP systems                                                                                       | search engine                                                 | Complex measurement |
| [Model-based test complexity analysis for software installation testing](https://ecommons.luc.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1036&context=cs_facpubs#page=660) | 2008 SEKE | Test complexity analysis for system installation functions - http://www.wikicfp.com/cfp/program?id=2619                                                       | search engine                                                 | Complex measurement |
| [Measuring Installability](https://www.uni-bamberg.de/fileadmin/pi/Dateien/SOCA13-Installability.pdf)                                             | 2013 SOCA | http://www.wikicfp.com/cfp/program?id=2718                                                                                                                    | search engine                                                 | Complex measurement |
| A complexity Measure for Textual requirements                        |          | https://www.researchgate.net/publication/312184512_A_Complexity_Measure_for_Textual_Requirements                                                              | search engine                                                 |                     |
| [Categorizing the Content of GitHub README File](https://arxiv.org/abs/1802.06997)                        |          | https://www.researchgate.net/publication/312184512_A_Complexity_Measure_for_Textual_Requirements                                                              | search engine                                                 |                     |
| [A large-scale analysis of bioinformatics code on GitHub](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0205898)                        |          | https://www.researchgate.net/publication/312184512_A_Complexity_Measure_for_Textual_Requirements                                                              | search engine                                                 |                     |
| [An Empirical Study of README contents for JavaScript Packages](https://www.jstage.jst.go.jp/article/transinf/E102.D/2/E102.D_2018EDP7071/_article)                        |          | https://www.researchgate.net/publication/312184512_A_Complexity_Measure_for_Textual_Requirements                                                              | search engine                                                 |                     |

| [Automatically assessing code understandability](https://dl.acm.org/doi/10.1145/3196398.3196441) | 2018 | Software Engineering | Combined metrics for code understandability | - | easure of code
understandability (no reference to installation methods) |
