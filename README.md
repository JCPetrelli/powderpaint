# PowderPaint

A Flask-based presentation web application that generates beautiful, dynamic slideshows from markdown files with frontmatter metadata. Features multiple slide layouts, random image assignment, and smooth keyboard navigation.

## Features

- **Markdown-Based Content**: Write slides in simple markdown with frontmatter metadata
- **Multiple Layout Types**: 7 different slide layouts (title, content, split, image-bg, image-focus, hero, video)
- **Dynamic Image Assignment**: Randomly assigns images to slides on each page load
- **Video Support**: Embed local videos or YouTube/Vimeo URLs
- **Keyboard Navigation**: Full keyboard controls with arrow keys, spacebar, and more
- **Fullscreen Mode**: Toggle fullscreen with F key
- **Progress Tracking**: Visual progress bar and slide counter
- **Smooth Animations**: CSS-based slide transitions
- **Responsive Design**: Built with Tailwind CSS for modern, responsive layouts

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd powderpaint
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage

### Running the Application

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Run the Flask development server
python3 app.py
```

The application will be available at `http://localhost:5000`

### Creating Slides

1. Create markdown files in the `data/` folder
2. Files are sorted alphabetically (e.g., `slide1.md`, `slide2.md`, etc.)
3. Each file should have frontmatter metadata and markdown content

#### Example Slide

```markdown
---
layout: content
---

## Your Slide Title

Your markdown content here with **bold** and *italic* text.

- Bullet points
- Are supported
- Too!
```

## Slide Layouts

### 1. Title Layout
Full-screen title slide with gradient background
```markdown
---
layout: title
---

# Main Title
## Subtitle
```

### 2. Content Layout
Standard content slide with prose styling
```markdown
---
layout: content
---

## Slide Title

Your content here
```

### 3. Split Layout
Two-column layout with text on the left and image on the right
```markdown
---
layout: split
image: /images/your-image.jpg
---

## Split Content

Text appears on the left, image on the right
```

### 4. Image Background Layout
Full-screen background image with overlay text
```markdown
---
layout: image-bg
image: /images/background.jpg
---

## Text Over Image

Content appears over the background image
```

### 5. Image Focus Layout
Large centered image with caption below
```markdown
---
layout: image-focus
image: /images/focus.jpg
---

## Image Caption

Optional description text
```

### 6. Hero Layout
Extra large text display (12rem font)
```markdown
---
layout: hero
---

# BIG TEXT
```

### 7. Video Layout
Video player supporting local files and embedded URLs
```markdown
---
layout: video
video_url: /videos/your-video.mp4
---

## Video Title

Optional caption
```

For YouTube/Vimeo:
```markdown
---
layout: video
video_url: https://www.youtube.com/embed/VIDEO_ID
---
```

## Keyboard Controls

- **Arrow Keys** (←/→): Navigate between slides
- **Spacebar**: Next slide
- **Home**: Jump to first slide
- **End**: Jump to last slide
- **F**: Toggle fullscreen mode

## Project Structure

```
powderpaint/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── data/                   # Markdown slide files
├── images/                 # Image assets for slides
├── videos/                 # Video files for video slides
├── static/                 # Static assets
├── templates/
│   ├── base.html          # Base template with Tailwind CSS
│   └── presentation.html  # Main presentation template
└── README.md              # This file
```

## Image Handling

- Place images in the `images/` folder
- Images are randomly assigned to slides with image-supporting layouts on each page load
- Supported formats: PNG, JPG, JPEG, GIF, SVG, WEBP
- Override random assignment by specifying `image: /images/filename.ext` in frontmatter

## Video Handling

- Place local video files in the `videos/` folder
- Supported formats: MP4, WebM, OGG
- Use `video_url` in frontmatter to specify video source
- Supports both local files and embedded URLs (YouTube, Vimeo)

## API Endpoints

- `GET /` - Main presentation view
- `GET /api/slides` - JSON API endpoint returning slide data
- `GET /images/<filename>` - Serve images from images folder
- `GET /videos/<filename>` - Serve videos from videos folder

## Technologies Used

- **Backend**: Flask 3.0.0
- **Markdown Processing**: python-frontmatter, markdown2
- **Frontend**: Tailwind CSS (via CDN)
- **JavaScript**: Vanilla JS for navigation and fullscreen

## Screenshots

### Title Slide
![Title Slide](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide1.jpg)

### Content Layout
![Content Layout](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide2.jpg)

### Split Layout
![Split Layout](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide3.jpg)

### Image Background
![Image Background](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide4.jpg)

### Image Focus
![Image Focus](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide5.jpg)

### Hero Layout
![Hero Layout](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide6.jpg)

### Video Layout
![Video Layout](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide7.jpg)

### Navigation Controls
![Navigation Controls](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide8.jpg)

### Progress Bar
![Progress Bar](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide9.jpg)

### Fullscreen Mode
![Fullscreen Mode](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide10.jpg)

### Keyboard Navigation
![Keyboard Navigation](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide11.jpg)

### Slide Transitions
![Slide Transitions](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide12.jpg)

### API Response
![API Response](/Users/jacopocastellano/Documents/Scripts/powderpaint/screenshots/slide13.jpg)

## Development

The application uses Flask's development server with debug mode enabled by default. The server automatically reloads when code changes are detected.

### Modifying Templates

- Edit `templates/presentation.html` for slide rendering logic
- Edit `templates/base.html` for global styles and scripts

### Adding New Layouts

1. Define layout in slide frontmatter
2. Add rendering logic in `templates/presentation.html`
3. Add corresponding CSS styles in `templates/base.html`

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
