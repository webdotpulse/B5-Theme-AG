# Bootstrap 5 Artistic Theme & Personal Site

This project provides a custom, orange-based, artistic Bootstrap 5 theme and a personal website example using this theme.

## Features

*   **Custom Bootstrap 5 Theme:**
    *   Vibrant Teal and Pink color palette.
    *   Artistic fonts ("Kelly Slab" for headings, "Montserrat" for body).
    *   Rounded corners and soft shadows.
    *   Custom components like an "artistic divider".
*   **Example Pages:**
    *   Start Page (About Me)
    *   CV / Resume
    *   Portfolio
    *   Podcast
    *   Blog
    *   Contact
    *   Typography & Components (Showcase)

## Getting Started

### Prerequisites

*   Node.js and npm

### Installation

1.  Clone the repository.
2.  Install dependencies:

    ```bash
    npm install
    ```

### Building the CSS

To compile the SASS files to CSS, run:

```bash
npm run build-css
```

To watch for changes and automatically rebuild:

```bash
npm run watch-css
```

### Viewing the Site

Open `public/index.html` in your browser.

## Project Structure

*   `src/scss/`: Contains the SASS source files.
    *   `_variables.scss`: Custom variable overrides (colors, fonts, etc.).
    *   `_custom.scss`: Additional custom styles and artistic touches.
    *   `theme.scss`: Main entry point that imports Bootstrap and custom files.
*   `public/`: Contains the static website files.
    *   `css/`: Compiled CSS.
    *   `*.html`: HTML pages for the personal site.
*   `screenshots/`: Screenshots of the generated pages.

## Revision History

See `CHANGELOG.md` for detailed revision history.
