# **5.1. Validation**

## **5.1.1. Table of Content - Validation**
- [5.1.1. Table of Content - Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#511-table-of-content---validation)
- [5.1.2. PEP8 Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#512-pep8-validation)
- [5.1.3. HTML Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#513-html-validation)
- [5.1.4. CSS Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#514-css-validation)
- [5.1.5. JS Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#515-js-validation)
- [5.1.6. WAVE Validation](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#516-wave-validation)
- [5.1.7. Lighthouse](https://github.com/FeruzaShokirjonovna/Blog/blob/main/docs/validation.md#517-lighthouse)

## **5.1.2. PEP8 Validation**

- **Task :** To ensure `*.py` files are compliant with PEP8 standards.
- **Tools :** 
  - [Black](https://black.readthedocs.io/en/stable/) - PY linter and formatter
  - [CI Python Linter](https://pep8ci.herokuapp.com/) - Visualizing PY linter
- **Method :** 
   - Install `Black` using `pip install black` in terminal
   - Use command `black --line-length 79 DIRECTORY_NAME/` to format `*.py` files in the selected directory or use `black --line-length 79 .` to format all files
   - See in the terminal window result of this operation *( Appendix 51 )*
   - Double check the results in `CI Python Linter` by copying and pasting the Python code as black doesn't wrap lines of comments. See result on the right hand side of the input field 
- **Results :**

![Linter Result](/docs/validation/linter_validation.png)

## **5.1.3. HTML Validation**

- **Task :** To ensure source code generated from all `*.html` templates is compliant with W3C standards.
- **Tools :** 
  - [W3C HTML Validator](https://validator.w3.org/) - HTML Validator
- **Method :** 
   - Open each page of the project
   - In Chrome : Right click on page background and select `View Page Source`
   - Copy and Paste the generated code from browser to validator
   - See results 
   - Please note this needs to be done for all states of the templates (i.e. Logged In / Logged Out, etc.)
- **Results :**

## **5.1.4. CSS Validation**

- **Task :** To ensure the code in `style.css` is compliant with W3C standards.
- **Tools :** 
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validator
- **Method :** 
   - Open the `style.css` file
   - Copy and Paste the code from IDE to validator
   - See results
- **Results :**
![CSS Validation](/docs/validation/css_validation.png)