# Creamind Website

This repository contains the source code for the Creamind website, a platform connecting creators and fans.

## Theme

The website uses a custom Bootstrap 5 theme with the following characteristics:
-   **Primary Color:** Pink (`#ff6b6b`)
-   **Secondary Color:** Purple (`#a06cd5`)
-   **Font:** Montserrat and Caveat Brush (imported via Google Fonts)
-   **Design Style:** Rounded corners, pill-shaped buttons, gradients, and a clean, modern look.

## Directory Structure

-   `public/`: Contains the compiled HTML, CSS, and image files. This is the web root.
-   `src/scss/`: Contains the SCSS source files.
    -   `theme.scss`: The main entry point that imports Bootstrap and custom styles.
    -   `_custom.scss`: Custom styles and overrides for Creamind.
    -   `_variables.scss`: Bootstrap variable overrides.

## Pages

-   `index.html`: The landing page.
-   `blog.html`: Blog listing page.
-   `blog-post.html`: Single blog post template.
-   `contact.html`: Contact form page.
-   `cv.html`: Curriculum Vitae / Resume page.
-   `portfolio.html`: Portfolio showcase page.
-   `podcast.html`: Podcast episodes page.
-   `components.html`: Style guide and component showcase.
-   `typography.html`: Typography and basic element showcase.
-   `navigation.html`: Examples of different navigation bar styles.

## Development

To make changes to the styles:
1.  Edit the files in `src/scss/`.
2.  Run `npm install` to install dependencies (if not already done).
3.  Run `npm run build-css` to compile SCSS to CSS.

## Screenshots

Screenshots of the pages are generated in the `screenshots/` directory using `python3 take_screenshots.py`.
