# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
-   **New Page**:
    -   `example-page.html`: A comprehensive example page demonstrating 10 new custom components in realistic layouts (Services, Process, Skills, Support, etc.).
-   **New Custom Components**:
    -   `Flip Card` (`.flip-card`): Interactive cards that flip on hover.
    -   `Process Steps` (`.process-steps`): Visual step-by-step indicator.
    -   `Skill Bar` (`.skill-bar-wrapper`): Styled progress bars with labels.
    -   `Avatar Group` (`.avatar-group`): Stacked avatars for user groups.
    -   `Chat Widget` (`.chat-widget`): Visual representation of a chat support interface.
    -   `Image Overlay Card` (`.image-overlay-card`): Image cards with sliding text overlays.
    -   `Breadcrumb Custom` (`.breadcrumb-custom`): Styled breadcrumb navigation.
    -   `Pagination Custom` (`.pagination-custom`): Styled pagination controls.
    -   `Floating Action Button` (`.fab-container`): Expandable FAB menu.
    -   `Notification Toast` (`.toast-custom`): Custom styled notification toast.
-   **Component Library**:
    -   Updated `components.html` to include isolated examples of all 10 new components.
    -   Added "Example Page" to the "More" dropdown menu.

### Added (Previous)
-   **New Pages**:
    -   `gallery.html`: An image gallery page featuring a grid of images and a responsive Lightbox modal with carousel navigation.
    -   `admin.html`: An advanced admin dashboard with a collapsible side menu, statistics widgets, and a recent activity table.
    -   `doodles.html`: A dedicated page showcasing all 7 decorative background doodles.
    -   `carousel.html`: A page featuring a standard Bootstrap carousel component.
    -   `cheatsheet.html`: A comprehensive reference page modeled after the Bootstrap cheatsheet, with a sidebar and various component examples.
    -   `masonry.html`: An example page demonstrating a Pinterest-style masonry layout using Bootstrap cards.
    -   `backgrounds.html`: A showcase page for background gradients and styles.
    -   `documentation.html`: A comprehensive documentation page for the project.
    -   `404.html`: A custom error page with a friendly design and home link.
    -   `maintenance.html`: An "Under Maintenance" page to display when the site is down for updates.
-   **Navigation**:
    -   Added "Gallery" and "Admin Dashboard" links to the "More" dropdown in the main navigation bar.
    -   Added "Doodles", "Carousel Example", "Cheatsheet", and "Masonry" links to the "More" dropdown in the main navigation bar.
-   **Doodles & Design**:
    -   Implemented "doodles" (SVG background patterns) extensively across the site (`index`, `components`, `contact`, `portfolio`, `blog`, `podcast`) to enhance visual appeal.
    -   Added support for 20+ file-based SVG doodles (e.g., `blob`, `hex`, `doodle1`...`doodle11`) accessible via new CSS classes (e.g., `.section-doodle-blob`).
    -   Showcased all new file-based doodles on the `doodles.html` page.
    -   Created `cv.html` if missing (verified link integrity).

### Changed
-   **Navigation**:
    -   Restructured the main menu: Added "Podcast", "Blog", "Portfolio", "CV", "Contact" as primary items.
    -   Moved secondary items ("About", "Services", etc.) to a "More" dropdown.
    -   **Login Button**: Styled the login button as a rounded, pill-shaped gradient button and linked it to `login.html`.

### Added (Previous)
-   **Authentication Pages**: Created `login.html`, `register.html`, and `forgot-password.html` with consistent branding and fancy forms.
-   **New Custom Components**:
    -   `Pricing Card` (`.pricing-card`): Highlighted pricing options with badges.
    -   `Team Card` (`.team-card`): Profile cards for team members with social links.
    -   `Stat Counter` (`.stat-counter`): Animated-style statistic counters.
    -   `Fancy Table` (`.fancy-table-wrapper`): A styled table with status badges and actions.
-   **Decorative Doodles**: Added `.section-doodle-2` and `.section-doodle-3` SVG background patterns and applied them to `index.html`.
-   **Updated Components Page**: Updated `components.html` to showcase the new tables, cards, and counters.
-   Added "Go to Top" button to all pages, visible on scroll.
-   Added language changer dropdown (EN/SQ) to the navigation bar on all pages.
-   Added new custom components to `components.html`:
    -   Round buttons with icons (`.btn-round-icon`).
    -   Social media share buttons (`.social-share-buttons`).
    -   Quote/Testimonial card (`.quote-card`).
    -   Timeline component (`.timeline-item`).
-   Added decorative "doodles" (background SVGs) to sections via `.section-doodle`.
-   Created `public/js/main.js` to handle frontend logic.
-   New doodle SVG assets: `star.svg`, `cross.svg`.
-   New CSS classes for doodles: `.section-doodle-6`, `.section-doodle-7`.
-   New custom components: Accordion, Custom Tabs, Custom Alert, Custom Progress.
-   New page: `public/icons.html` showcasing icon variations.
-   New page: `public/code-examples.html` showcasing code blocks.
-   Added "Icons" and "Code Examples" to the main navigation menu.

### Changed (Previous)
-   **Rebranding**: Replaced "CREAMIND" with "Arsela Gjonaj" across all pages and content.
-   Updated `components.html` to showcase new components.
-   Updated `public/components.html` to include new custom components.
-   Updated main navigation in `index.html` and other subpages.

### Fixed
-   Fixed missing interactive elements in static HTML by introducing `main.js`.

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
