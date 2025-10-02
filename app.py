import os
import random
from flask import Flask, render_template, jsonify
import frontmatter
import markdown2

app = Flask(__name__)

DATA_FOLDER = 'data'
IMAGES_FOLDER = 'images'
VIDEOS_FOLDER = 'videos'

def get_slides():
    """Parse all markdown files from data folder and return slide data."""
    slides = []

    if not os.path.exists(DATA_FOLDER):
        return slides

    # Get all markdown files sorted by name
    md_files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith('.md')])

    for md_file in md_files:
        filepath = os.path.join(DATA_FOLDER, md_file)
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

            # Parse markdown content to HTML
            content_html = markdown2.markdown(post.content)

            slides.append({
                'layout': post.get('layout', 'content'),
                'content': content_html,
                'metadata': post.metadata
            })

    return slides

def get_random_images(count=None):
    """Get random images from images folder."""
    if not os.path.exists(IMAGES_FOLDER):
        return []

    image_files = [f for f in os.listdir(IMAGES_FOLDER)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'))]

    if not image_files:
        return []

    if count:
        return random.sample(image_files, min(count, len(image_files)))

    return image_files

def assign_images_to_slides(slides):
    """Randomly assign images to slides that support images."""
    images = get_random_images()

    if not images:
        return slides

    # Layouts that support images
    image_layouts = ['split', 'image-bg', 'image-focus']

    # Assign a random image to each slide that supports images
    for slide in slides:
        # Only assign if the slide doesn't already specify an image in metadata
        if slide['layout'] in image_layouts and not slide['metadata'].get('image'):
            slide['image'] = f'/images/{random.choice(images)}'
        else:
            slide['image'] = slide['metadata'].get('image')

    return slides

@app.route('/')
def index():
    """Main presentation view."""
    slides = get_slides()
    slides = assign_images_to_slides(slides)

    return render_template('presentation.html', slides=slides)

@app.route('/api/slides')
def api_slides():
    """API endpoint to get slides data."""
    slides = get_slides()
    slides = assign_images_to_slides(slides)
    return jsonify(slides)

# Serve images from images folder
@app.route('/images/<path:filename>')
def serve_image(filename):
    """Serve images from the images folder."""
    from flask import send_from_directory
    return send_from_directory(IMAGES_FOLDER, filename)

# Serve videos from videos folder
@app.route('/videos/<path:filename>')
def serve_video(filename):
    """Serve videos from the videos folder."""
    from flask import send_from_directory
    return send_from_directory(VIDEOS_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
