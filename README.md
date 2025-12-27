# Arsela Gjonaj (formerly Creamind) Website

This repository contains the source code for the Arsela Gjonaj personal website (rebranded from Creamind), a platform connecting creators and fans.

## Theme

The website uses a custom Bootstrap 5 theme with the following characteristics:
-   **Primary Color:** Pink (`#ff6b6b`)
-   **Secondary Color:** Purple (`#a06cd5`)
-   **Font:** Montserrat and Caveat Brush (imported via Google Fonts)
-   **Design Style:** Rounded corners, pill-shaped buttons, gradients, and a clean, modern look.
-   **Doodles:** Decorative SVG background patterns (`.section-doodle` variants) are used extensively for visual interest.

## Directory Structure

-   `public/`: Contains the compiled HTML, CSS, JS, and image files. This is the web root.
    -   `js/main.js`: Contains frontend logic (Go to Top, Language Changer).
-   `src/scss/`: Contains the SCSS source files.
    -   `theme.scss`: The main entry point that imports Bootstrap and custom styles.
    -   `_custom.scss`: Custom styles and overrides.
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
-   `backgrounds.html`: Showcase of available background styles and gradients.
-   `doodles.html`: Comprehensive showcase of all decorative background doodles.
-   `documentation.html`: Project documentation and guidelines.
-   `typography.html`: Typography and basic element showcase.
-   `navigation.html`: Examples of different navigation bar styles.
-   `carousel.html`: Example page featuring a Bootstrap carousel.
-   `cheatsheet.html`: Reference page modeled after Bootstrap's cheatsheet, showing various elements.
-   `masonry.html`: Example page showcasing a Masonry layout using Bootstrap cards.
-   `code-examples.html`: Provides styled code snippets for developers.
-   `icons.html`: Displays available icons and style variations.
-   `login.html`: User login page.
-   `register.html`: User registration page.
-   `forgot-password.html`: Password recovery page.
-   `404.html`: Custom Error page.

## Development

To make changes to the styles:
1.  Edit the files in `src/scss/`.
2.  Run `npm install` to install dependencies (if not already done).
3.  Run `npm run build-css` to compile SCSS to CSS.

## Screenshots

Screenshots of the pages are generated in the `screenshots/` directory using `python3 take_screenshots.py`.

## New Additions

- **Doodles Page**: `public/doodles.html` - All 7 doodle variations in one place.
- **Carousel Example**: `public/carousel.html` - Standard carousel implementation.
- **Cheatsheet**: `public/cheatsheet.html` - Sidebar navigation with component examples.
- **Masonry Layout**: `public/masonry.html` - Grid layout using Masonry.js.
