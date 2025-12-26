# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Changed
- Major redesign of `index.html` to match "Creamind" mockup.
- Updated color palette to Creamind Pink (`#ff6b6b`) and Purple (`#a06cd5`).
- Updated Navbar to be floating, pill-shaped, with "Login / Register" CTA.
- Updated Hero section with new copy ("Turn Admiration Into Interaction") and gradient background.
- Replaced "Popular Skills" section with "Popular Users" card layout.
- Added "What Makes Creamind Special!" feature section.
- Added custom SASS styles for `.user-card`, `.feature-card`, and gradients in `_custom.scss`.

## [1.2.0] - 2023-10-27

### Added
- Created `blog-post.html` as a dedicated page for individual blog posts.
- Added content for the blog post "Understanding Color Theory".

### Changed
- Updated `index.html` start page content with new bio details.
- Updated `index.html` header layout to position the image at the bottom and removed image shadow/rounded styling.
- Updated `index.html` header image to use the local `arsi.png` file instead of a remote URL.
- Created `components.html` to showcase custom components (buttons, cards, alerts, etc.).
- Added "Components" link to the navigation bar on all pages.
- Removed Animated SVG wave header and associated script (`header-animation.js`).
- Updated Navbar styling to be fixed to top and visually "floating" (detached with margins and rounded corners).
- Updated Navigation Examples page (`navigation.html`) with consistent menu and styling.

## [1.1.0] - 2023-10-27

### Changed
- Updated color palette to Vibrant Teal (`#1ABC9C`) and Pink (`#E91E63`) to add more color.
- Changed fonts to "Kelly Slab" (headings) and "Montserrat" (body) for a more artistic look.
- Modified `index.html` hero section to be centered, resembling the "Kelly" theme layout.
- Updated `theme.scss` to import Google Fonts.

## [1.0.0] - 2023-10-27

### Added
- Initial project setup with `npm`.
- Bootstrap 5 and SASS dependencies.
- Custom SASS theme setup:
    - Orange-based color palette (`$primary: #fd7e14`).
    - Custom fonts: Georgia for headings, Segoe UI for body.
    - Custom components: `.artistic-divider`, custom button styles, soft shadows.
- HTML pages for the personal website:
    - `index.html`: Homepage / About Me.
    - `cv.html`: Curriculum Vitae.
    - `portfolio.html`: Portfolio showcase.
    - `podcast.html`: Podcast episode listing.
    - `blog.html`: Blog posts.
    - `contact.html`: Contact form.
    - `typography.html`: Showcase of typography and Bootstrap components.
- Build scripts in `package.json` for compiling SASS.
- Generated screenshots for all pages.
