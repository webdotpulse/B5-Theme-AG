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
-   `about.html`: Detailed "About Me" page with bio, career journey, and media appearances.
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
-   `gallery.html`: Image gallery with Lightbox functionality.
-   `admin.html`: Advanced admin dashboard with sidebar navigation.
-   `maintenance.html`: "Under Maintenance" page for site downtime.
-   `example-page.html`: A rich example page demonstrating the use of new custom components in a real-world layout.

## New Custom Components

The following custom components have been added to the theme (`src/scss/_custom.scss`) and are showcased in `components.html` and `example-page.html`:

1.  **Flip Card** (`.flip-card`): Cards that flip on hover to reveal content on the back.
2.  **Process Steps** (`.process-steps`): A visual step-by-step indicator.
3.  **Skill Bar** (`.skill-bar-wrapper`): Fancy progress bars with labels and gradient fills.
4.  **Avatar Group** (`.avatar-group`): Overlapping user avatars for community or team sections.
5.  **Chat Widget** (`.chat-widget`): A static representation of a chat interface.
6.  **Image Overlay Card** (`.image-overlay-card`): Images with a text overlay that slides up on hover.
7.  **Breadcrumb Custom** (`.breadcrumb-custom`): Styled breadcrumb navigation.
8.  **Pagination Custom** (`.pagination-custom`): Styled pagination links.
9.  **Floating Action Button** (`.fab-container`): A main action button that expands to show more options.
10. **Notification Toast** (`.toast-custom`): A custom-styled toast notification.

## Development

To make changes to the styles:
1.  Edit the files in `src/scss/`.
2.  Run `npm install` to install dependencies (if not already done).
3.  Run `npm run build-css` to compile SCSS to CSS.

## Screenshots

Screenshots of the pages are generated in the `screenshots/` directory using `python3 take_screenshots.py`.

## New Additions

- **About Page**: `public/about.html` - Comprehensive personal profile.
- **Doodles Page**: `public/doodles.html` - All 7 doodle variations in one place.
- **Carousel Example**: `public/carousel.html` - Standard carousel implementation.
- **Cheatsheet**: `public/cheatsheet.html` - Sidebar navigation with component examples.
- **Masonry Layout**: `public/masonry.html` - Grid layout using Masonry.js.
- **Gallery**: `public/gallery.html` - Responsive image grid with Bootstrap Modal Lightbox.
- **Admin Dashboard**: `public/admin.html` - Responsive admin interface with collapsible sidebar.
- **Maintenance Page**: `public/maintenance.html` - A user-friendly "Under Maintenance" page.
- **File-based Doodles**: Additional doodle backgrounds loaded from SVG files (`.section-doodle-blob`, etc.) have been added to the theme and showcased on `public/doodles.html`.
