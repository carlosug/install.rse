# README

## Annotation Procedures for Gold Standard Corpus
The dataset was manually annotated to investigate how researchers report installation instructions in GitHub repositories. The annotation focused on identifying patterns on the installation methods provided in the README files of these repositories. The main steps involved in the annotation process were:
1. **Repo Selection**: A sample of repositories was selected based on specific criteria.
2. **Manual Annotation**: Each repository's README file was examined manually to identify the presence of installation instructions and their respective methods.
3. **Classification of Installation Methods**: The installation methods were categorized into types such as "source" "package manager", "container," "build" and "plugin".
4. **Analysis of Headers**: The headers in the README files (H1 to H6) were analyzed to detect trends and patterns in the structure of installation instructions.

## How to identify a installation method
1. Check whether installation-related information appears in the readme
2. Annotate headers
3. If headers contain information to detect a method e.g., `## With Pip`, then annotate method type `Package_manager`
4. If headers does not contain information to detect a method, check the text under the header and verify its method (*very often researchers use headers for `## Installation` and add text and code commands ```pip install .```*)

> The basic idea of our annotation is that README headers work as an overview of the contents beneath them. By examining the section headers, we can discern whether the sections are relevant to our target method delving into the detailed content. This could also be an strategy for the **classifier**. The idea also is the annontate **[../../extractor/corpus.json](../../extractor/corpus.json)**

## Variable Descriptions

| Variable Name           | Description                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| `repo_name`             | The name of the GitHub repository being analyzed.                                                      |
| `stars`                 | The number of stars the repository has on GitHub, representing its popularity.                         |
| `has_installation`       | A binary variable indicating whether the repository has installation-related information (TRUE, FALSE).   |
| `h1`                    | The H1 header text from the README file.                                                              |
| `h2`                    | The H2 header text from the README file.                                                              |
| `h3`                    | The H3 header text from the README file.                                                              |
| `h4`                    | The H4 header text from the README file.                                                              |
| `h5`                    | The H5 header text from the README file.                                                              |
| `h6`                    | The H6 header text from the README file.                                                              |
| `text`                  | The text under the specific header (*only retrieve when is not possible to identify methods from headers*)                                                                   |  
| `method_type`           | The type of installation method(s) found in the README, e.g., "source," "package manager," etc.        |
| `annotator_comments`     | Additional comments or notes made during the manual annotation process.                                |

## Example Entry

| repo_name  | stars | has_installation | h1             | h2                 | h3           | method_type    | method_count | annotator_comments |
|------------|-------|------------------|----------------|--------------------|--------------|----------------|--------------|-------------------|
| SampleRepo | 1500  | TRUE               | "Installations" | "From Pip" |      | "Package_Manager" | 2            | "Multiple installation options available." |
