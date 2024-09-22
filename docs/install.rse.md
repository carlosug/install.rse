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
