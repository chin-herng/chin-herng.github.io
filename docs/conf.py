# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Chin Herng'
copyright = '2026, Chin Herng'
author = 'Chin Herng'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_math_dollar',
    'sphinx_design'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    'card-grid.css',
    'center-table.css',
    'contact-list.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/brands.min.css"
]
html_title = 'Chin Herng'
html_theme_options = {
    "footer_icons": [
        {
            "name": "Email",
            "url": "mailto:chinherng@u.nus.edu",
            "html": "",
            "class": "fa-solid fa-envelope fa-2x",
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com/in/chong-chin-herng",
            "html": "",
            "class": "fa-brands fa-solid fa-linkedin fa-2x",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/chin-herng",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com/chongahzong",
            "html": "",
            "class": "fa-brands fa-solid fa-instagram fa-2x",
        }
    ]
}
html_scaled_image_link = False
