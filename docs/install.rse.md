## Good practices in Research Software Development and Documentation

List of articles, papers and notes about research software documentation. We seek to answer:

**- RQ1: What are the recommendations for documenting installation methods of research software?**

        * Which rules and best practices exist? Do the given recommendations cover the defined categories?;
        * Which rules and best practices exist? Do the given recommendations cover the defined categories?
        * Which rules and best practices exist? Do the given recommendations cover the defined categories?

**- RQ2: What is the practice of documenting research software?**

### Education
- [eScience Center](https://esciencecenter-digital-skills.github.io/2024-10-22-ds-cr/)
- [Code Refinery](https://coderefinery.org/lessons/)


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

### Domain specific community used software descriptors:
- **Research Sofware community community:**
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

### Installation (Software includes qualified references to how to install the artefact)
- [Makeareadme.com](https://www.makeareadme.com/#installation-1)
- [Installation and Usage](https://awegroup.github.io/developer-guide/docs/documentation.html#installation-and-usage)
- [GovUSA](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md#instructions-for-how-to-develop-use-and-test-the-code)


### Coding standards and conventions on README
- [GNU Coding starndards](https://www.gnu.org/prep/standards/standards.html) - Install command categories [https://www.gnu.org/prep/standards/standards.html#Install-Command-Categories](https://www.gnu.org/prep/standards/standards.html#Install-Command-Categories)


|Article   | Year  | Sections   | Installation methods   |   |
|---|---|---|---|---|
| [Stodden and Miguez](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.ay)  | 2014   |   |   |   |
| [Fehr and Heiland](http://www.aimspress.com/article/10.3934/Math.2016.3.261)  | 2016   |   |   |   |
| [Wilson et al](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)  | 2014   |   |   |   |
| [Wilson et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)  | 2017  |   |   |   |
| [Hastings et al](https://academic.oup.com/gigascience/article/3/1/2047-217X-3-31/2682967)  | 2014  |   |   |   |
| [Sandve et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)  | 2013  |   |   |   |
| [Lee et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006561)  | 2013  |   |   |   |
| [Gil et al](https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015EA000136)  | 2016  |   |   |   |
| [Morgan et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005412)  | 2016  |   |   |   |
| [Karimzadeh et al](https://academic.oup.com/bib/article/19/4/693/2907814?login=false)  | 2018  |   |   |   |


| Title                                                              | Conf year | What is about:                                                                                                                                               | Strategy                                                      | Relevant for us in: |
|--------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------|
| Software ingredients: detection of Third-party Component reuse in JAVA | MSR 2016  | Analysis of reuse activity detection of software reuse define a method to detect multiple third-party components in jar file                                   | query                                                         |                     |
| An empirical analysis of the docker container ecosystem on Github    | MSR 2017  | Analysis of the distribution of the project using Docker by programming lang INSTRUCTIONS/ project size and infrastructure // assess the quality of Dockerfiles by classifying issues // classify changes evolution | query                                                         |                     |
| Cross-project code reuse in Github                                   | MSR 2017  | Construct a Graph with similar RQ                                                                                                                             | query                                                         |                     |
| Bidirectional Paper-Repository Tracing in Software Engineering       | MSR 2024  |                                                                                                                                                              | query                                                         |                     |
| DRMiner: tool for identifying and analysing Dockerfile               | MSR 2024  | Mine docker instead of readme                                                                                                                                 | query                                                         |                     |
| On the executability of R Markdown files                             | MSR 2024  | Similar to readme md - how executable are the R md                                                                                                            | query                                                         |                     |
| Quantifying Security Issues in Reusable JS Actions in Github workflows | MSR 2024  | RQ - to what extent do JS actions rely on NPM packages? What are the characteristics of JS action dependencies? To what extent do JS actions have vulnerabilities with https://codeql.github.com/ | query                                                         |                     |
| Option Matter: Documenting and Fixing Non-reproducible Builds in conf systems | MSR 2024  | Which configuration options if any have an impact on the reproducibility of builds? An approach to automatically identify configuration options causing non-reproducibility of builds | query                                                         |                     |
| Automated Generation of Issue Report Templates                       | MSR 2024  | Similar concept as ours                                                                                                                                      | query                                                         |                     |
| Analysing the evolution of ML models in HF                           | MSR 2024  | Similar RQ - how can we evaluate and categorise the status of ML? K-mean cluster algorithm based on activity patterns resulting in high/low maintenance        | query                                                         |                     |
| A large-scale empirical study of OS licence usage                    | MSR 2024  | Nicely done with the statistical analysis                                                                                                                    | query                                                         |                     |
| How to ML projects use CI?                                           | MSR 2024  | Comparative analysis between ML and non-ML projects                                                                                                           | search engine                                                 |                     |
| Charactering and understanding software security in ML libraries     | MSR 2023  | RQs similar to violations of readme instructions                                                                                                             | search engine                                                 |                     |
| Evaluating Software Documentation quality                            | MSR 2023  | Empirical study to determine what is important in documenting software libraries - selecting metrics and validation with interviews                           | search engine                                                 |                     |
| A large-scale study about quality and reproducibility of jupyter notebooks | MSR 2019  |                                                                                                                                                              | search engine                                                 |                     |
| Predicting good configuration for Github Topic models                | MSR 2019  | Latent Dirichlet allocation as topic model to explain structure of a corpus by grouping text                                                                   | search engine                                                 | Predicting installation instruction errors (method) |
| Automatic classification of software artifacts in OS applications    | MSR 2018  | Identify which types of software artifacts are produced by a wide variety of open-source projects at different levels of granularity. RQ1: how can software be categorised | search engine                                                 |                     |
| Large-scale of commit patterns                                       | MSR 2018  | Analyze the co-commit patterns in the constructed co-authorship networks - check RQ                                                                            | search engine                                                 |                     |
| Open Source Software Development Tool Installation                   | 2024      | Investigate the challenges novice developers face in software development when installing software development tools with interviews (Christoph Treude to follow his research) | search engine                                                 |                     |
| A taxonomy of installation instruction changes                       | 2023      | First research directly on readme - qualitative analysis                                                                                                       | search engine                                                 | Analysing instructions (a taxonomy for installation related changes in readmes) focusing on patterns of behaviours associated with their installation-related section updates |
| Evaluating transfer learning for simplifying READMEs                 | FSE 2023  | Transfer learning to simplify readmes - (Text simplification)                                                                                                  | search engine                                                 | Analysing readmes focusing on updates with longer commit histories |
| How READMe files are structured in open source Java projects         | 2022      | Publication in ScienceDirect Information and Technology - applying Statistics and cluster methods                                                              | search engine                                                 | Analysing readmes (methods) |
| An exploratory study of software artifacts on GH from lens of documentation | 2024      | Qualitative methods to explore useful info in docs                                                                                                            | search engine                                                 | Analysing documentation but not the methods |
| Software documentation issues unveiled                               | 2019 IEEE/ACM | Comprehensive taxonomy consisting of 162 types of documentation issues                                                                                        | search engine                                                 | Analysing documentation issues type (categories) |
| OS software documentation Mining for quality assessment              | 2013 AIST | Assess the quality of non-source code text found in software packages                                                                                         | search engine                                                 | Analysing the quality the method to be checked |
| Why do Software Package Conflict?                                    | MSR 2012  | How to detect conflict in packages similar to how to detect incorrect instructions                                                                            | search engine                                                 | Detecting installation instructions errors (method) |
| Quantifying reproducibility: Quantifying Reproducibility in Computational Biology: The Case of the Tuberculosis Drugome paper |          |                                                                                                                                                              |                                                               |                     |
| Measuring the reusability of software components using static analysis | 2019      | An interpretable methodology for estimating reusability at class and package levels                                                                           | search engine                                                 | Measure reusability |
| A large-scale study on research code quality and execution           | 2022      |                                                                                                                                                              |                                                               |                     |
| On the accuracy of code complexity metrics                           | 2023      |                                                                                                                                                              | search engine                                                 | Complex measurement |
| Ease of adoption of clinical natural language processing software    | 2015      | Assess the ease of adoption of the state-of-the-art clinical NLP systems                                                                                       | search engine                                                 | Complex measurement |
| Model-based test complexity analysis for software installation testing | 2008 SEKE | Test complexity analysis for system installation functions - http://www.wikicfp.com/cfp/program?id=2619                                                       | search engine                                                 | Complex measurement |
| Measuring Installability                                             | 2013 SOCA | http://www.wikicfp.com/cfp/program?id=2718                                                                                                                    | search engine                                                 | Complex measurement |
| A complexity Measure for Textual requirements                        |          | https://www.researchgate.net/publication/312184512_A_Complexity_Measure_for_Textual_Requirements                                                              | search engine                                                 |                     |
